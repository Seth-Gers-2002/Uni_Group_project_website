# routes/job_intake.py

from flask import Blueprint, render_template, request, redirect, url_for, flash

job_bp = Blueprint('job', __name__)

@job_bp.route('/job_intake', methods=['GET', 'POST'])
def job_intake():
    if request.method == 'POST':
        # Retrieve form data
        job_title = request.form.get('job_title')
        date = request.form.get('date')
        client_name = request.form.get('client_name')
        phone_number = request.form.get('phone_number')
        email = request.form.get('email')
        address = request.form.get('address')
        # ... retrieve any other fields as needed

        # Basic validation for required fields
        errors = []
        if not job_title:
            errors.append("Job title is required.")
        if not client_name:
            errors.append("Client full name is required.")
        if not phone_number:
            errors.append("Phone number is required.")
        if not email:
            errors.append("Email address is required.")
        if not address:
            errors.append("Address is required.")

        # If errors exist, flash them and re-render the form with previously entered values
        if errors:
            for error in errors:
                flash(error, "error")
            return render_template('job_intake.html', form=request.form)
        else:
            # Placeholder for saving to the database in a future commit
            flash("Job intake submitted successfully!", "success")
            return redirect(url_for('job.job_intake'))

    # GET request renders an empty form
    return render_template('job_intake.html')
