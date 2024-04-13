from bootcamp.models import User
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, SelectField
from wtforms.validators import InputRequired, Length, Email, ValidationError

class RegistrationForm(FlaskForm):
    fname = StringField('First Name', validators=(
        [InputRequired(), Length(min=3, max=22)]))

    lname = StringField('Last Name', validators=(
        [InputRequired(), Length(min=3, max=22)]))

    email = EmailField('Email', validators=([InputRequired(), Email()]))

    program = StringField('Program of Study', validators=(
        [InputRequired(), Length(min=3, max=22)]))

    area_of_interest = SelectField(
        'Area of Interest',
        choices=[
            ('web_dev', 'Web Development'),
            ('ai_ml', 'AI and ML'),
            ('automation_scripting', 'Automation and Scripting'),
            ('data_science', 'Data Science'),
            ('game_dev', 'Game Development'),
            ('data_analysis', 'Data Analysis')
        ]
    )



    submit = SubmitField("Register")


    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Someone already registered with this email!')