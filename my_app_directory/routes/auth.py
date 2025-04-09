from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    """Employee registration form."""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Basic input validation
        if not username or not password:
            flash("Username and password are required.", "error")
            return redirect(url_for('auth.register'))

        # Check if the username already exists
        if User.query.filter_by(username=username).first():
            flash("Username already exists.", "error")
            return redirect(url_for('auth.register'))

        # Create a new user (MFA is disabled by default in this basic login)
        new_user = User(
            username=username,
            password_hash=generate_password_hash(password),
            mfa_enabled=False,   # Basic login for employees; MFA can be enabled later
            mfa_method=None
        )
        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful!", "success")
        return redirect(url_for('auth.login'))

    return render_template('register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Basic login for employees."""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password_hash, password):
            flash("Invalid username or password.", "error")
            return redirect(url_for('auth.login'))

        # Set the user session and mark user as logged in
        session['user_id'] = user.id
        flash("Logged in successfully!", "success")
        return redirect(url_for('index'))

    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    """Logs out the current user."""
    session.pop('user_id', None)
    flash("Logged out successfully.", "info")
    return redirect(url_for('index'))

@auth_bp.route('/mfa_page/<int:user_id>')
def mfa_page(user_id):
    """
    Displays the MFA verification page.
    This route is used for testing: it shows the MFA page without going through the standard login process.
    """
    user = User.query.get_or_404(user_id)
    return render_template('mfa_verify.html', user=user)
