from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    """
    Basic registration form for employees.
    This route creates a new user account and saves it to the database.
    MFA settings can be configured at registration.
    """
    if request.method == 'POST':
        # Retrieve form data
        username = request.form.get('username')
        password = request.form.get('password')
        # For basic login, MFA can be enabled later; here we capture these values
        mfa_enabled = request.form.get('mfa_enabled') == 'on'
        mfa_method = request.form.get('mfa_method')

        # Validate required fields
        if not username or not password:
            flash("Username and password are required.", "error")
            return redirect(url_for('auth.register'))

        # Check for existing user
        if User.query.filter_by(username=username).first():
            flash("Username already taken.", "error")
            return redirect(url_for('auth.register'))

        # Create a new user with hashed password
        new_user = User(
            username=username,
            password_hash=generate_password_hash(password),
            mfa_enabled=mfa_enabled,
            mfa_method=mfa_method
        )
        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful! Please log in.", "success")
        return redirect(url_for('auth.login'))

    return render_template('register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password_hash, password):
            flash("Invalid username or password.", "error")
            return redirect(url_for('auth.login'))
        session['user_id'] = user.id
        flash("Logged in successfully!", "success")
        return redirect(url_for('base'))  # Now goes to role-based landing route
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    """
    Logs out the current user by clearing the session.
    """
    session.pop('user_id', None)
    flash("Logged out successfully.", "info")
    return redirect(url_for('index'))
