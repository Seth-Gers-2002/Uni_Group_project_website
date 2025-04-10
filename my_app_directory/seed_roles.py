"""
Used to manually seed roles into terminal so that they may be assigned to users
"""

from app import create_app
from models import db, Role

app = create_app()

with app.app_context():
    roles_to_create = ['Administrator', 'Employee', 'Customer']
    for role_name in roles_to_create:
        if not Role.query.filter_by(role_name=role_name).first():
            new_role = Role(role_name=role_name)
            db.session.add(new_role)
            print(f"Added role: {role_name}")
    db.session.commit()
    print("Seeding completed!")
