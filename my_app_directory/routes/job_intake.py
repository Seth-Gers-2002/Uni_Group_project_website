# routes/job_intake.py

from flask import Blueprint, render_template, request

job_bp = Blueprint('job', __name__)

@job_bp.route('/job_intake', methods=['GET', 'POST'])
def job_intake():
    if request.method == 'POST':
        # In the next steps, you’ll handle form data here (e.g., validation, saving to DB).
        pass

    # Renders the basic form template
    return render_template('job_intake.html')
