from flask import Blueprint, render_template, request, redirect, url_for, flash

# Define Blueprint before using it
job_bp = Blueprint('job', __name__)

@job_bp.route('/job_intake', methods=['GET', 'POST'])
def job_intake():
    if request.method == 'POST':  # Only validate on form submission
        job_title = request.form.get('job_title')
        date = request.form.get('date')
        client_name = request.form.get('client_name')
        phone_number = request.form.get('phone_number')
        email = request.form.get('email')
        address = request.form.get('address')

        # Validation
        errors = []
        if not job_title:
            errors.append("Job title is required.")
        if not date:
            errors.append("Date is required.")
        if not client_name:
            errors.append("Client full name is required.")
        if not phone_number or not phone_number.isdigit() or len(phone_number) != 10:
            errors.append("Phone number must be exactly 10 digits.")
        if not email or "@" not in email:
            errors.append("A valid email address is required.")
        if not address:
            errors.append("Address is required.")

        if errors:
            for error in errors:
                flash(error, "error")
            return render_template('job_intake.html', form=request.form)  # Retain entered values

        flash("Job successfully submitted!", "success")
        return redirect(url_for('job.job_intake'))  # Redirect after success

    return render_template('job_intake.html', form={})  # Render form on GET request
