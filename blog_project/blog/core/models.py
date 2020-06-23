from blog import connection
import pymysql.cursors
from datetime import datetime

def create_blog_table():
    with connection.cursor() as cursor:
        # Create a new record
        sql = """create table if not exists blogs1(
            id int(11) unsigned AUTO_INCREMENT PRIMARY KEY,
            title varchar(255) NOT NULL,
            description text NOT NULL,
            owner_name varchar(50) NOT NULL,
            image varchar(500),
            created_at datetime NOT NULL,
            is_published tinyint(1) default 1
            ); 
            """
        cursor.execute(sql)
    connection.commit()

create_blog_table()

def create_blog(title, description, owner_name, image, is_published=True,**kwargs):
    with connection.cursor() as cursor:
        # Create a new record
        sql = """insert into blog_project.blogs1(title, description, owner_name, image, created_at, is_published)
            values(%s, %s, %s, %s, %s, %s) 
            """
        now = datetime.now()
        created_ad = now.strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute(sql, (title, description, owner_name, image, created_ad, is_published))
    connection.commit()

def all_blogs():
    with connection.cursor() as cursor:
        # Create a new record
        sql = """select * from blog_project.blogs1;"""
        cursor.execute(sql)
    return cursor.fetchall()

def blog_detail(id):
    with connection.cursor() as cursor:
        # Create a new record
        sql = """select * from blog_project.blogs1 where id=%s"""
        cursor.execute(sql,id)
    return cursor.fetchone()

def blog_delete(id):
    with connection.cursor() as cursor:
        # Create a new record
        sql = """delete from blog_project.blogs1 where id=%s"""
        cursor.execute(sql,id)
    connection.commit()
    return cursor.fetchone()
    

def blog_update(title, description, owner_name,id,**kwargs):
    with connection.cursor() as cursor:
    # Create a new record
        sql = "Update blog_project.blogs1 Set title=%s, description=%s, owner_name=%s where id =%s"
        now = datetime.now()
        created_ad = now.strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute(sql,(title, description, owner_name,id))
    connection.commit()

def blog_search(x):
    with connection.cursor() as cursor:
        # Create a new record
        sql = """SELECT * from blog_project.blogs1 WHERE title LIKE %s"""
        cursor.execute(sql, ("%" + x + "%"))
    connection.commit()
    return cursor.fetchall()

