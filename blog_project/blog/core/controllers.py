from flask import Blueprint, jsonify, render_template,request,redirect,flash
from blog.core.models import create_blog , all_blogs , blog_detail , blog_delete, blog_update , blog_search
from blog.core.forms import BlogForm

core = Blueprint(__name__,'core')
import json

@core.route('/')
def home():
    blogs = all_blogs()
    print(request.args)
    word = request.args.get('word')
    if word:
        blogs = blog_search(word)
        print(blogs)
    context = {
        'blogs':blogs
    }
    return render_template('core/index.html',**context)

@core.route('/create',methods=['GET','POST'])
def create():
    form = BlogForm()
    if form.validate_on_submit():
        create_blog(**form.data, image='')
        return redirect('/')
    context = {
        'form' : form
    }
    return render_template('core/create.html',**context)
    # if request.method == 'POST':
    #     # create_blog(title=request.form['title'], description=request.form['description'], owner_name=request.form['owner_name'], image='')
    #     create_blog(**request.form,image='')
    #     flash('Blog created')
    #     return redirect('/')
    

@core.route('/update-blog/<int:id>',methods=['GET','POST'])
def update(id):
    if request.method == 'POST':
        form = BlogForm()
        if form.validate_on_submit():
        # create_blog(title=request.form['title'], description=request.form['description'], owner_name=request.form['owner_name'], image='')
            blog_update(**form.data,id=id)
            flash('Blog updated')
            return redirect('/')
    else :
        blog = blog_detail(id)
        print(blog)
        form = BlogForm(data = blog)
    context = {
        'form':form
    }
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
    flash('Blog deleted')
    return redirect('/')






    # return jsonify(blogs)