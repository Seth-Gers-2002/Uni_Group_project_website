from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, DateField
from wtforms.validators import DataRequired, Email

class JobForm(FlaskForm):
    job_title = StringField('Job Title', validators=[DataRequired()])
    date = DateField('Date', validators=[DataRequired()])
    client_name = StringField('Client Full Name', validators=[DataRequired()])
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    address = StringField('Address', validators=[DataRequired()])
    job_description = StringField('Job Description', validators=[DataRequired()])
    priority = SelectField('Priority', choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], validators=[DataRequired()])
    technician_assigned = StringField('Technician Assigned', validators=[DataRequired()])
    status = SelectField('Job Status', choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Completed', 'Completed')], validators=[DataRequired()])
    submit = SubmitField('Submit')
