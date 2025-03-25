# --- MFA CHANGE START
from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    """Basic registration form with MFA preference."""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        mfa_enabled = request.form.get('mfa_enabled') == 'on'
        mfa_method = request.form.get('mfa_method')

        # Simple validation
        if not username or not password:
            flash("Username and Password are required.", "error")
            return redirect(url_for('auth.register'))

        # Check if username already exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("Username already taken.", "error")
            return redirect(url_for('auth.register'))

        # Create new user
        new_user = User(
            username=username,
            password_hash=generate_password_hash(password),
            mfa_enabled=mfa_enabled,
            mfa_method=mfa_method
        )
        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful!", "success")
        return redirect(url_for('auth.login'))

    return render_template('register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Step 1: Standard login fields (Username/Password). If MFA is enabled, proceed to MFA verification."""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password_hash, password):
            flash("Invalid username or password.", "error")
            return redirect(url_for('auth.login'))

        # If MFA is enabled, redirect to token verification
        if user.mfa_enabled:
            flash("MFA is enabled. Please verify your token.", "info")
            return redirect(url_for('auth.mfa_verify', user_id=user.id))

        flash("Logged in successfully!", "success")
        return redirect(url_for('index'))

    return render_template('login.html')

@auth_bp.route('/mfa_verify/<int:user_id>', methods=['GET', 'POST'])
def mfa_verify(user_id):
    """Step 2: Token input field for MFA verification."""
    user = User.query.get_or_404(user_id)

    if request.method == 'POST':
        token = request.form.get('token')
        # In real scenario, we compare token with what was sent via Email/Text.
        # For demonstration, assume a static token '123456'.
        if token == '123456':
            flash("MFA token verified!", "success")
            return redirect(url_for('index'))
        else:
            flash("Invalid MFA token.", "error")
            return redirect(url_for('auth.mfa_verify', user_id=user.id))

    # TODO: If user.mfa_method == 'Email', send token via email. If 'Text', send via SMS.
    flash("MFA token sent to your {}!".format(user.mfa_method), "info")
    return render_template('mfa_verify.html')

@auth_bp.route('/login_bypass')
def login_bypass():
    """
    Bypass the login process for testing purposes.
    This route logs in a dummy test user and redirects based on MFA settings.
    """
    # Try to retrieve a test user; create one if not existing
    user = User.query.filter_by(username="testuser").first()
    if not user:
        user = User(
            username="testuser",
            password_hash=generate_password_hash("password"),
            mfa_enabled=True,       # Enable MFA for testing
            mfa_method="Email"        # Set preferred MFA method (e.g., Email)
        )
        db.session.add(user)
        db.session.commit()

    # If MFA is enabled, redirect to the MFA verification page
    if user.mfa_enabled:
        flash("MFA is enabled for this account. Please verify your token.", "info")
        return redirect(url_for('auth.mfa_verify', user_id=user.id))
    else:
        flash("Logged in successfully!", "success")
        return redirect(url_for('index'))

# --- MFA CHANGE END
