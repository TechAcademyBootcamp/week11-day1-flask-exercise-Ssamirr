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
            user_id int(11) unsigned NOT NULL,
            image varchar(500),
            created_at datetime NOT NULL,
            is_published tinyint(1) default 1,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE ON UPDATE CASCADE,
            INDEX (id, user_id)
            ); 
            """
        cursor.execute(sql)
    connection.commit()

create_blog_table()

def create_blog(title, description, user_id, image, is_published=True,**kwargs):
    with connection.cursor() as cursor:
        # Create a new record
        sql = """insert into blog_project.blogs1(title, description, user_id, image, created_at, is_published)
            values(%s, %s, %s, %s, %s, %s) 
            """
        now = datetime.now()
        created_ad = now.strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute(sql, (title, description, user_id, image, created_ad, is_published))
    connection.commit()

def all_blogs(limit_f_index=None,limit_s_index=None):
    limit_query = ''
    if limit_f_index is not None and limit_s_index is not None:
        limit_query =f'LIMIT {limit_f_index}, {limit_s_index}'
    with connection.cursor() as cursor:
        # Create a new record
        sql = f"""select * from blog_project.blogs1 {limit_query};"""
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

def get_blog_user_details(blog_id):
    with connection.cursor() as cursor:
        # Create a new record
        sql = """select users.first_name,users.surname from blog_project.blogs1
        INNER JOIN blog_project.users on users.id = blogs1.user_id where blogs1.id = %s
        """
        cursor.execute(sql,blog_id)
    return cursor.fetchone()

def get_blog_count():
    with connection.cursor() as cursor:
        # Create a new record
        sql = """select count(id) from blog_project.blogs1 
        """
        cursor.execute(sql)
    return cursor.fetchone()['count(id)']

def get_user_count():
    with connection.cursor() as cursor:
        # Create a new record
        sql = """select count(id) from blog_project.users 
        """
        cursor.execute(sql)
    return cursor.fetchone()['count(id)']

def create_website_table():
    with connection.cursor() as cursor:
        # Create a new record
        sql = """insert into blog_project.about_website(social_adress, email,phone_number)
            values('Blog.com', 'Blog@gmail','+994000000') 
            """
        cursor.execute(sql)
    connection.commit()

def website_table():
    with connection.cursor() as cursor:
        # Create a new record
        sql = """SELECT * From blog_project.about_website
            """
        cursor.execute(sql)
    return cursor.fetchone()

# create_website_table()


