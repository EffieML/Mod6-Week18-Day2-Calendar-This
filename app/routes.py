from flask import Blueprint, render_template
import os
import sqlite3
# import forms
from .forms import AppointmentForm
from datetime import datetime


bp = Blueprint('main', __name__, url_prefix='/')
DB_FILE = os.environ.get("DB_FILE")


@bp.route('/', methods=["GET", "POST"])
def main():
    form = AppointmentForm()

    if form.validate_on_submit():
        with sqlite3.connect(DB_FILE) as conn:
            curs = conn.cursor()
            curs.execute(
                """
                INSERT INTO appointments(name,start_datetime, end_datetime, description, private)
                VALUES (:name,:start_datetime, :end_datetime, :description, :private)
                """,
                {
                    'name': form.name.data,
                    'start_datetime': datetime.combine(form.start_date.data, form.start_time.data),
                    'end_datetime': datetime.combine(form.end_date.data, form.end_time.data),
                    'description': form.description.data,
                    'private': form.private.data
                })

    with sqlite3.connect(DB_FILE) as conn:
        curs = conn.cursor()
        fetched = curs.execute(
            "SELECT id, name, start_datetime, end_datetime FROM appointments ORDER BY start_datetime;")

    return render_template('main.html', rows=fetched, form=form)

# @bp.route("/hello")
# def hello():
#     return render_template('items.html')


# @bp.route("/new")
# def newAppointment():
#     form = AppointmentForm()
    # with sqlite3.connect(DB_FILE) as conn:
    #     curs = conn.cursor()
    #     fetched = curs.execute(
    #         "SELECT id, name, start_datetime, end_datetime FROM appointments ORDER BY start_datetime;")
    # return render_template('main.html', rows=fetched)
