# DISCLAIMER: The following code was developed using the ChatGPT tool to handle generation of the python code
# and sqlalchemy integration. ChatGPT also refined the database schema.

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

# 1. Users Table (Modified)
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)

    # Relationship with UserRole (to access roles)
    roles = relationship('UserRole', back_populates='user')

    # Relationship with Company through CompanyEmployee (an employee can be part of many companies)
    companies = relationship('CompanyEmployee', back_populates='employee')

# 2. Roles Table (No Change)
class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    role_name = Column(String(50), unique=True, nullable=False)

    # Relationship with UserRole (to access users)
    users = relationship('UserRole', back_populates='role')

# 3. UserRoles Table (Join table for user roles, no change)
class UserRole(Base):
    __tablename__ = 'user_roles'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    role_id = Column(Integer, ForeignKey('roles.id'), nullable=False)

    # Relationships to connect to User and Role
    user = relationship('User', back_populates='roles')
    role = relationship('Role', back_populates='users')

# 4. Company Table (New)
class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    location = Column(String(100))  # Additional details about the company
    abn = Column(String(11))  # Australian business number
    acn = Column(String(9)) # Australian company number
    phone_number = Column(String(100))
    number_of_employees = Column(Integer)

    # Relationship with CompanyEmployee (employees who are part of this company)
    employees = relationship('CompanyEmployee', back_populates='company')

# 5. CompanyEmployee Table (Join table for employee-company relationship)
class CompanyEmployee(Base):
    __tablename__ = 'company_employees'

    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, ForeignKey('companies.id'), nullable=False)
    employee_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    is_owner = Column(Integer, default=0)  # If the employee is the owner of the company (0 for false, 1 for true)

    # Relationship to connect to Company and User
    company = relationship('Company', back_populates='employees')
    employee = relationship('User', back_populates='companies')

# Create an SQLite engine and a session for interaction with the database
engine = create_engine('sqlite:///user_management.db')  # The database file will be users.db
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Delete existing data (optional) to avoid conflicts
session.query(User).delete()
session.query(Role).delete()
session.query(UserRole).delete()
session.query(Company).delete()
session.query(CompanyEmployee).delete()
session.commit()

# 1. Create roles (check if they already exist to avoid duplicates)
roles_to_create = ['Administrator', 'Employee', 'Customer']
for role_name in roles_to_create:
    existing_role = session.query(Role).filter_by(role_name=role_name).first()
    if not existing_role:  # Only create the role if it doesn't exist
        new_role = Role(role_name=role_name)
        session.add(new_role)
session.commit()  # Commit to save roles in the database

# 2. Create users
user1 = User(email='admin@example.com', name='Admin User Person', password='password123')
user2 = User(email='employee1@example.com', name='Employee Person', password='password123')
user3 = User(email='individual@example.com', name='Individual Person', password='password123')
user4 = User(email='customer@example.com', name='Customer Person', password='password123')

# Add users to the session
session.add(user1)
session.add(user2)
session.add(user3)
session.add(user4)
session.commit()  # Commit to save users in the database

# 3. Assign roles to users
user_role_admin = UserRole(user_id=user1.id, role_id=1)  # Admin
user_role_employee = UserRole(user_id=user2.id, role_id=2)  # Employee
user_role_employee2 = UserRole(user_id=user3.id, role_id=1)  # Employee Individual, needs admins status
user_role_customer = UserRole(user_id=user4.id, role_id=3)  # Customer

session.add(user_role_admin)
session.add(user_role_employee)
session.add(user_role_employee2)
session.add(user_role_customer)
session.commit()  # Commit to save user roles in the database

# 4. Create companies
company1 = Company(name='Scrubit', location='Brisbane', abn="12345678901",
                   acn="123456789", phone_number="+61298765432", number_of_employees=11)

session.add(company1)
session.commit()  # Commit to save companies in the database

# 5. Assign employees to companies (marking user2 as owner of TechCorp)
company_employee1 = CompanyEmployee(company_id=company1.id, employee_id=user1.id, is_owner=1)
company_employee2 = CompanyEmployee(company_id=company1.id, employee_id=user2.id, is_owner=0)

session.add(company_employee1)
session.add(company_employee2)
session.commit()  # Commit to save employee-company associations in the database

# Verify by printing out the users and their roles along with companies they belong to
users_with_roles_and_companies = session.query(User).all()
for user in users_with_roles_and_companies:
    role_names = [user_role.role.role_name for user_role in user.roles]
    company_names = [company_employee.company.name for company_employee in user.companies]
    print(f"User: {user.name}, Email: {user.email}, Roles: {role_names}, Companies: {company_names}")
