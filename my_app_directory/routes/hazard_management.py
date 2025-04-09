from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Hazard

hazard_management_bp = Blueprint('hazard_management', __name__)


@hazard_management_bp.route('/hazard_form', methods=['GET', 'POST'])
def hazard_form():
    if request.method == 'POST':
        hazard_type = request.form['hazard_type']
        hazard_description = request.form['hazard_description']
        hazard_location = request.form['hazard_location']
        risk_level = request.form['risk_level']
        likelihood = request.form['likelihood']
        severity = request.form['severity']
        potential_impact = request.form.get('potential_impact')
        exposure_details = request.form.get('exposure_details')
        recommended_equipment = request.form.get('recommended_equipment')

        new_hazard = Hazard(
            hazard_type=hazard_type,
            hazard_description=hazard_description,
            hazard_location=hazard_location,
            risk_level=risk_level,
            likelihood=likelihood,
            severity=severity,
            potential_impact=potential_impact,
            exposure_details=exposure_details,
            recommended_equipment=recommended_equipment
        )
        db.session.add(new_hazard)
        db.session.commit()
        return redirect(url_for('hazard_management.hazard_form'))

    return render_template("hazard_form.html")
