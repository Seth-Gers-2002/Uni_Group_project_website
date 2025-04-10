import sys
from flask import Flask
from models import db, User, Role, UserRole
from app import create_app

app = create_app()

with app.app_context():
    if len(sys.argv) != 3:
        print("Usage: python assign_role.py <username/email> <role_name>")
        sys.exit(1)

    username = sys.argv[1]
    role_name = sys.argv[2]

    user = User.query.filter_by(username=username).first()
    role = Role.query.filter_by(role_name=role_name).first()

    if not user:
        print(f"User '{username}' not found.")
        sys.exit(1)

    if not role:
        print(f"Role '{role_name}' not found.")
        sys.exit(1)

    if any(ur.role_id == role.id for ur in user.roles):
        print(f"User '{username}' already has the role '{role_name}'.")
    else:
        new_user_role = UserRole(user_id=user.id, role_id=role.id)
        db.session.add(new_user_role)
        db.session.commit()
        print(f"Assigned role '{role_name}' to user '{username}'.")
