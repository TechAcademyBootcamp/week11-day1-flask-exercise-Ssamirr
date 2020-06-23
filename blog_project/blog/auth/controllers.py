from flask import Blueprint , render_template
from blog.auth.forms import RegisterForm

auth = Blueprint(__name__,'auth')

@auth.route('/register',methods=['GET','POST'])
def register():
    form = RegisterForm()
    form.validate_on_submit()
    context = {
        'form' : form
    }
    return render_template('auth/register.html',**context)

@auth.route('/login',methods=['GET','POST'])
def login():
    form = RegisterForm()
    form.validate_on_submit
    context = {
        'form' : form
    }
    return render_template('auth/login.html',**context)