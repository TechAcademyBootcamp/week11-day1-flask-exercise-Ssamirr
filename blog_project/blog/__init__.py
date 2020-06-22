from flask import Flask


import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123',
                             db='blog_project',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

from blog.core.controllers import core
from blog.auth.controllers import auth

app = Flask(__name__)

app.register_blueprint(core)
app.register_blueprint(auth)

