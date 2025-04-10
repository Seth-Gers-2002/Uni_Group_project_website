# Defines role_required decorator to check user roles
from functools import wraps
from flask import session, redirect, url_for, flash
from models import User

def role_required(*role_names):
    """
    Decorator used to restrict access to users with at least one of the provided role names.
    Example:
        @role_required('Admin', 'Manager')
    """
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            user_id = session.get("user_id")
            if not user_id:
                flash("You must be logged in to view this page", "error")
                return redirect(url_for('auth.login'))
            user = User.query.get(user_id)
            if not user:
                flash("User not found.", "error")
                return redirect(url_for('auth.login'))

            # Get the current user's roles
            user_roles = [ur.role.role_name for ur in user.roles] if user.roles else []

            # Check whether any required role is present in the user_roles list.
            if not any(role in user_roles for role in role_names):
                flash("You do not have permission to view this page.", "error")
                return redirect(url_for('client_home'))
            return f(*args, **kwargs)
        return decorated_function
    return decorator
