from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email

class JobIntakeForm(FlaskForm):
    job_title = StringField("Job Title", validators=[DataRequired()])
    # Update the format to ISO format, which is what HTML date input produces
    date = DateField("Date", format='%Y-%m-%d', validators=[DataRequired()])
    client_name = StringField("Client Full Name", validators=[DataRequired()])
    phone_number = StringField("Phone Number", validators=[DataRequired()])
    email = StringField("Email Address", validators=[DataRequired(), Email()])
    address = StringField("Address", validators=[DataRequired()])
    job_description = TextAreaField("Job Description", validators=[DataRequired()])
    priority = SelectField("Priority", choices=[("Low", "Low"), ("Medium", "Medium"), ("High", "High")], validators=[DataRequired()])
    technician_assigned = StringField("Technician Assigned", validators=[DataRequired()])
    status = SelectField("Job Status", choices=[("Pending", "Pending"), ("In Progress", "In Progress"), ("Completed", "Completed")], validators=[DataRequired()])
    submit = SubmitField("Submit")
