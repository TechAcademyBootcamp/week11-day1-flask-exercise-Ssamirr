from flask import Blueprint, jsonify, render_template,request,redirect,flash
from blog.core.models import create_blog , all_blogs , blog_detail , blog_delete, blog_update , blog_search
core = Blueprint(__name__,'core')
import json

@core.route('/')
def home():
    blogs = all_blogs()
    word = request.args.get('x')
    if word:
        blogs = blog_search(word)
        print(blogs)
    context = {
        'blogs':blogs
    }
    return render_template('core/index.html',**context)

@core.route('/create',methods=['GET','POST'])
def create():
    print(request.form)
    if request.method == 'POST':
        # create_blog(title=request.form['title'], description=request.form['description'], owner_name=request.form['owner_name'], image='')
        create_blog(**request.form,image='')
        flash('Blog created')
        return redirect('/')
    return render_template('core/create.html')

@core.route('/update-blog/<int:id>',methods=['GET','POST'])
def update(id):
    blog = blog_detail(id)
    context = {
        'blog':blog
    }
    if request.method == 'POST':
        # create_blog(title=request.form['title'], description=request.form['description'], owner_name=request.form['owner_name'], image='')
        blog_update(**request.form,id=id)
        flash('Blog updated')
        return redirect('/')
    return render_template('core/blog-update.html',**context)

@core.route('/blog/<int:id>')
def information(id):
    blog = blog_detail(id)
    context = {
        'blog':blog
    }
    return render_template('core/blog-detail.html',**context)

@core.route('/delete-blog/<int:id>')
def delete_blog(id):
    blog = blog_delete(id)
    return redirect('/')






    # return jsonify(blogs)