from flask import Blueprint

auth = Blueprint(__name__,'auth')

@auth.route('/login')
def home():
    return 'this is login page'