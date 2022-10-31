from http.client import NOT_FOUND
from flask import Blueprint, render_template


bp = Blueprint('initial', __name__, url_prefix='/', template_folder='templates')

class InitialCtrl:
    @bp.route("/")
    def index():
        return "Initial"

    @bp.app_errorhandler(NOT_FOUND)
    def not_found(error):  # sourcery skip: instance-method-first-arg-name
        return render_template('not_found.html', error=error)