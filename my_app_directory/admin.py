"""
Decorator to restrict access based on user role
"""

from flask import Blueprint, render_template
from access_control import role_required

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin_dashboard')
@role_required('Admin', 'Manager')
def admin_dashboard():
    # This page is accessible only to Admins or Managers.
    return render_template('admin_dashboard.html')

@admin_bp.route('/employee_dashboard')
@role_required('Employee')
def employee_dashboard():
    # Accessible only to Employees.
    return render_template('employee_dashboard.html')

@admin_bp.route('/individual_dashboard')
@role_required('Individual')
def individual_dashboard():
    # Accessible only to Individuals.
    return render_template('individual_dashboard.html')

@admin_bp.route('/customer_dashboard')
@role_required('Customer')
def customer_dashboard():
    # Accessible only to Customers.
    return render_template('customer_dashboard.html')