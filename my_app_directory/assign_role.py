import sys
from models import db, User, Role, UserRole
from app import create_app

def assign_role_to_user(username, role_name):
    app = create_app()
    with app.app_context():
        user = User.query.filter_by(username=username).first()
        if not user:
            print(f"User '{username}' not found.")
            return

        role = Role.query.filter_by(role_name=role_name).first()
        if not role:
            print(f"Role '{role_name}' not found.")
            return

        if UserRole.query.filter_by(user_id=user.id, role_id=role.id).first():
            print(f"User '{username}' already has the role '{role_name}'.")
            return

        user_role = UserRole(user_id=user.id, role_id=role.id)
        db.session.add(user_role)
        db.session.commit()
        print(f"Assigned role '{role_name}' to user '{username}'.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python assign_role.py <username> <role>")
    else:
        assign_role_to_user(sys.argv[1], sys.argv[2])

# PYTHONPATH=. python my_app_directory/assign_role.py <username> <role>