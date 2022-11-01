from flask import Blueprint, render_template

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def main():
    return render_template('main.html')
# @bp.route("/hello")
# def hello():
#     return render_template('items.html')
