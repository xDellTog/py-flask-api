from flask import Blueprint, render_template

bp = Blueprint('users', __name__, url_prefix='/users', template_folder='templates')

class HomeCtrl:
    @bp.route("/")
    def index():
        return render_template('users/index.html')

    @bp.route("/<int:id>")
    def users(id):  # sourcery skip: instance-method-first-arg-name
        return render_template('users/index.html', user={'id': id})