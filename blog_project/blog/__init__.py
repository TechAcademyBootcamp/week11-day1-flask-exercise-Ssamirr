from flask import Flask,session
from flask_sqlalchemy import SQLAlchemy


import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123',
                             db='blog_project',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


from blog.auth.models import get_user
from blog.core.models import get_blog_user_details,get_blog_count,get_user_count,website_table



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123@127.0.0.1:3306/blog_project'
db = SQLAlchemy(app)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40),nullable=False)
    email = db.Column(db.String(40), nullable=False)
    subject = db.Column(db.String(255), nullable=False)
    message = db.Column(db.Text(), nullable=False)

    def __repr__(self):
        return self.username


class AboutWebsite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    social_adress = db.Column(db.String(40),nullable=False)
    email = db.Column(db.String(40), nullable=False)
    phone_number = db.Column(db.String(40), nullable=False)

    def __repr__(self):
        return self.social_adress

db.create_all()

from blog.auth.controllers import auth
from blog.core.controllers import core

app.register_blueprint(auth)
app.register_blueprint(core)

@app.context_processor
def utility_processor():
    def current_user():
        user_id = session.get('user_id')
        if user_id:
            return get_user(user_id)
        else:
            return 'Anonymous'
    return dict(current_user=current_user())

@app.context_processor
def utility_processor():
    def get_blog_user(blog_id):
        user_detail = get_blog_user_details(blog_id)
        return f"{user_detail['first_name']} {user_detail['surname']}"

    return dict(get_blog_user=get_blog_user)

@app.context_processor
def utility_processor():
    def count_blog():
        blog_count = get_blog_count()
        return blog_count
    return dict(count_blog=count_blog)

@app.context_processor
def utility_processor():
    def count_user():
        user_count = get_user_count()
        print(user_count)
        return user_count
    return dict(count_user=count_user)

@app.context_processor
def utility_processor():
    def info_website():
        website_info = website_table()
        return website_info
    return dict(info_website=info_website)



