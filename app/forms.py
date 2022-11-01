from flask_wtf import FlaskForm
from wtforms.fields import BooleanField, DateField, StringField, SubmitField, TextAreaField, TimeField
from wtforms.validators import DataRequired, ValidationError
from datetime import datetime


class AppointmentForm(FlaskForm):
    def validate_end_date(form, field):
     start= datetime.combine(form.start_date.data, form.start_time.data)
     end =datetime.combine(form.end_date.data, form.end_time.data)
     if (start>end):
        raise ValidationError("End date/time must come after start date/time ")
     if(form.start_date.data!=form.end_date.data):
        raise ValidationError("appt must start/end on same day")


    name = StringField("Name", validators=[DataRequired()])
    start_date = DateField("Start_date", validators=[DataRequired()])
    start_time = TimeField("Start_time", validators=[DataRequired()])
    end_date = DateField("End_date", validators=[DataRequired()])
    end_time = TimeField("End_time", validators=[DataRequired(), validate_end_date])
    description = TextAreaField("Description", validators=[DataRequired()])
    private = BooleanField("Private")
    submit = SubmitField("Create an appointment")
