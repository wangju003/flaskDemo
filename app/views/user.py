from flask import Blueprint,jsonify
user = Blueprint('user',__name__)

data = {'flaskDemo':'中文字'}
@user.route('/users')
def index():
    return jsonify(data)