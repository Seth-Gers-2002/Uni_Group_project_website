from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

# -------------------------
# Primary Application Models
# -------------------------

class Hazard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hazard_type = db.Column(db.String(120), nullable=False)
    hazard_description = db.Column(db.Text, nullable=False)
    hazard_location = db.Column(db.String(120), nullable=False)
    risk_level = db.Column(db.String(50), nullable=False)
    likelihood = db.Column(db.String(50), nullable=False)
    severity = db.Column(db.String(50), nullable=False)
    potential_impact = db.Column(db.Text)
    exposure_details = db.Column(db.Text)
    recommended_equipment = db.Column(db.Text)

    def __repr__(self):
        return f"<Hazard {self.hazard_type}>"

class InventoryItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    quantity = db.Column(db.Integer, default=0)
    location = db.Column(db.String(120))
    job_association = db.Column(db.String(120))
    cleaning_method = db.Column(db.String(120))

    def __repr__(self):
        return f"<InventoryItem {self.name}>"

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(10), nullable=False)  # Stored as string for simplicity
    client_name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    job_description = db.Column(db.Text, nullable=False)
    priority = db.Column(db.String(10), nullable=False)
    technician_assigned = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"<Job {self.job_title}>"

# -------------------------
# User & Authentication Models
# -------------------------

class User(db.Model):
    __tablename__ = 'user'  # Explicit table name to avoid conflict with legacy code
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)  # username or email
    password_hash = db.Column(db.String(255), nullable=False)
    mfa_enabled = db.Column(db.Boolean, default=False, nullable=False)
    mfa_method = db.Column(db.String(20))  # e.g., 'Email' or 'Text'

    # Relationships with roles and companies
    roles = db.relationship('UserRole', back_populates='user', lazy=True)
    companies = db.relationship('CompanyEmployee', back_populates='employee', lazy=True)

    def __repr__(self):
        return f"<User {self.username}, MFA Enabled: {self.mfa_enabled}>"

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(50), unique=True, nullable=False)

    # Relationship to link users via UserRole
    users = db.relationship('UserRole', back_populates='role', lazy=True)

    def __repr__(self):
        return f"<Role {self.role_name}>"

class UserRole(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)

    # Relationships to connect to User and Role
    user = db.relationship('User', back_populates='roles')
    role = db.relationship('Role', back_populates='users')

    def __repr__(self):
        return f"<UserRole user_id={self.user_id} role_id={self.role_id}>"

class Company(db.Model):
    __tablename__ = 'companies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    location = db.Column(db.String(100))
    abn = db.Column(db.String(11))  # Australian business number
    acn = db.Column(db.String(9))   # Australian company number
    phone_number = db.Column(db.String(100))
    number_of_employees = db.Column(db.Integer)

    # Relationship to connect employees via CompanyEmployee
    employees = db.relationship('CompanyEmployee', back_populates='company', lazy=True)

    def __repr__(self):
        return f"<Company {self.name}>"

class CompanyEmployee(db.Model):
    __tablename__ = 'company_employees'
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'), nullable=False)
    employee_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    is_owner = db.Column(db.Integer, default=0)  # 0 for false, 1 for true

    # Relationships to connect to Company and User
    company = db.relationship('Company', back_populates='employees')
    employee = db.relationship('User', back_populates='companies')

    def __repr__(self):
        return f"<CompanyEmployee company_id={self.company_id} employee_id={self.employee_id}>"

# -------------------------
# Optional: Database Seeding (For Testing Purposes)
# -------------------------

if __name__ == '__main__':
    from flask import Flask

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    with app.app_context():
        db.create_all()
        print("Database tables created.")

        # Example seeding (optional):
        # Create roles if they don't exist.
        roles_to_create = ['Administrator', 'Employee', 'Customer']
        for role_name in roles_to_create:
            existing_role = Role.query.filter_by(role_name=role_name).first()
            if not existing_role:
                new_role = Role(role_name=role_name)
                db.session.add(new_role)
        db.session.commit()

        # Example: Create some users.
        if not User.query.filter_by(username='admin@example.com').first():
            admin = User(username='admin@example.com', mfa_enabled=False)
            admin.set_password('password123')
            db.session.add(admin)
            db.session.commit()
            print("Seeded admin user.")

        # (Add additional seeding logic as needed.)
