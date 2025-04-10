from flask import Blueprint, render_template, session, redirect, url_for, flash
from models import User

account_bp = Blueprint('account', __name__)

@account_bp.route('/account')
def account():
    # Check if the user is logged in by verifying the session
    if 'user_id' not in session:
        flash("You must be logged in to view your account", "error")
        return redirect(url_for('login'))

    user = User.query.get(session['user_id'])
    if not user:
        flash("User not found", "error")
        return redirect(url_for('login'))

    # Mask the password: display the first character of the stored hash then mask the rest.
    # (Note: In production, passwords are hashed and should never be shown. This is just a demonstration.)
    masked_password = user.password_hash[0] + "*" * (len(user.password_hash) - 1)


    # Retrieve user roles (assuming user.roles is a list of UserRole objects)
    role_names = [user_role.role.role_name for user_role in user.roles] if user.roles else []

    return render_template('account.html', username=user.username,
                           masked_password=masked_password,
                           roles=role_names)
