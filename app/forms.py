from flask_wtf import FlaskForm
from wtforms.fields import BooleanField, DateField, StringField, SubmitField, TextAreaField, TimeField
from wtforms.validators import DataRequired


class AppointmentForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    start_date = DateField("Start_date", validators=[DataRequired()])
    start_time = TimeField("Start_time", validators=[DataRequired()])
    end_date = DateField("End_date", validators=[DataRequired()])
    end_time = TimeField("End_time", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[DataRequired()])
    private = BooleanField("Private")
    submit = SubmitField("Create an appointment")
