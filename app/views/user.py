from flask import Blueprint,jsonify
user = Blueprint('user',__name__)

data = {'flaskDemo':'中文字AAAaaa1223456'}
@user.route('/users')
def index():
    return jsonify(data)