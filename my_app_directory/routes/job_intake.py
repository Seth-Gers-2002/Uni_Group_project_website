from flask import Blueprint, render_template, request
from models import db, Job

job_intake_bp = Blueprint('job', __name__)

@job_intake_bp.route('/job_intake', methods=['GET', 'POST'])
def job_intake():
    form = JobIntakeForm()
    if form.validate_on_submit():
        try:
            # Convert the input date from dd/mm/yyyy to ISO format (YYYY-MM-DD)
            formatted_date = form.date.data.strftime('%Y-%m-%d')
        except Exception as e:
            flash("Invalid date format. Please ensure the date is entered as dd/mm/yyyy.", "error")
            return render_template('job_intake.html', form=form)

        new_job = Job(
            job_title=form.job_title.data,
            date=formatted_date,
            client_name=form.client_name.data,
            phone_number=form.phone_number.data,
            email=form.email.data,
            address=form.address.data,
            job_description=form.job_description.data,
            priority=form.priority.data,
            technician_assigned=form.technician_assigned.data,
            status=form.status.data
        )
        db.session.add(new_job)
        try:
            db.session.commit()
        except Exception as commit_error:
            db.session.rollback()
            flash("An error occurred while saving the job: " + str(commit_error), "error")
            print("Commit Error:", commit_error, file=sys.stderr)
            return render_template('job_intake.html', form=form)

        flash("Job successfully submitted!", "success")
        return redirect(url_for('job.job_intake'))
    else:
        if form.errors:
            for field, errors in form.errors.items():
                for error in errors:
                    flash(f"{field}: {error}", "error")
    return render_template('job_intake.html', form=form)

@job_intake_bp.route('/jobs', methods=['GET'])  # New route to display jobs
def list_jobs():
    """
    Retrieve all jobs from the database and display them, with optional filtering.
    """
    assignee_filter = request.args.get('assignee', '')  # Get the selected assignee from the query parameters
    jobs = Job.query.all()
    assignees = db.session.query(Job.technician_assigned).distinct().all()
    assignee_list = sorted(list(set([a[0] for a in assignees if a[0]])))
    if "n/a" not in assignee_list:
        assignee_list.append("n/a")

    if assignee_filter and assignee_filter.lower() != 'all' and assignee_filter:
        # Filter the jobs based on the selected assignee
        jobs = [job for job in jobs if job.technician_assigned.lower() == assignee_filter.lower()]

    return render_template('job_list.html', jobs=jobs, assignees=assignee_list, current_filter=assignee_filter)