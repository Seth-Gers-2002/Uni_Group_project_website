from flask import Blueprint, render_template
from flask_login import login_required

individual_bp = Blueprint('individual', __name__, url_prefix='/individual')

@individual_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('individual/dashboard.html')
