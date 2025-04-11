from flask import Blueprint, render_template
from flask_login import login_required

individual_cleaner_bp = Blueprint('individual_cleaner', __name__, url_prefix='/individual_cleaner')

@individual_cleaner_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('individual_cleaner/dashboard.html')
