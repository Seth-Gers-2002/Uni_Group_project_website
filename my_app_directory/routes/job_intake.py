from flask import Blueprint, render_template, request, redirect, url_for, flash

# Define Blueprint before using it
job_bp = Blueprint('job', __name__)

@job_bp.route('/job_intake', methods=['GET', 'POST'])
def job_intake():
    if request.method == 'POST':  # Only validate when submitting
        job_title = request.form.get('job_title')
        date = request.form.get('date')
        client_name = request.form.get('client_name')
        phone_number = request.form.get('phone_number')
        email = request.form.get('email')
        address = request.form.get('address')
        job_description = request.form.get('job_description')
        priority = request.form.get('priority')
        technician_assigned = request.form.get('technician_assigned')
        status = request.form.get('status')

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
        if not job_description:
            errors.append("Job description is required.")
        if not priority:
            errors.append("Priority is required.")
        if not technician_assigned:
            errors.append("Technician assigned is required.")
        if not status:
            errors.append("Job status is required.")

        if errors:
            for error in errors:
                flash(error, "error")
            return render_template('job_intake.html', form=request.form)  # Retain values

        flash("Job successfully submitted!", "success")
        return redirect(url_for('job.job_intake'))  # Redirect after success

    return render_template('job_intake.html', form={})  # Render empty form on GET request
