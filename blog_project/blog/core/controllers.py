from flask import Blueprint, jsonify, render_template,request,redirect,flash,session
from blog.core.models import create_blog , all_blogs , blog_detail , blog_delete, blog_update , blog_search,get_blog_count
from blog.core.forms import BlogForm,ContactForm
from blog.core.utils import login_required
from blog import Contact ,db
import math

core = Blueprint(__name__,'core')
import json

@core.route('/')
def home():
    page = int(request.args.get('page', 1))
    blogs = all_blogs((page-1)*2,2)
    page_count = math.ceil(get_blog_count()/2)
    page_range = range(1,page_count+1)
    print(request.args)
    word = request.args.get('word')
    if word:
        blogs = blog_search(word)
        print(blogs)
    next_page = None
    previous_page = None
    if page+1 <= page_count:
        next_page = page + 1
    if page-1 >= 0:
        previous_page = page - 1
    context = {
        'blogs':blogs,
        'page_range' : page_range,
        'next_page' : next_page,
        'previous_page' : previous_page,
        'current_page' : page
    }
    return render_template('core/index.html',**context)

@core.route('/create',methods=['GET','POST'])
@login_required
def create():
    form = BlogForm()
    if form.validate_on_submit():
        create_blog(**form.data,user_id = session.get('user_id'),image='')
        flash('Melumat elave edildi')
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
@login_required
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
@login_required
def delete_blog(id):
    blog = blog_delete(id)
    flash('Blog deleted')
    return redirect('/')

@core.route('/contact',methods=['GET','POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        contact_info =Contact(username=form.username.data, email=form.email.data, subject=form.subject.data, message=form.message.data)
        db.session.add(contact_info)
        db.session.commit()
        flash('Mesajiniz gonderildi')
        return redirect('/')
    context = {
        'form' : form
    }
    return render_template('core/contact.html',**context)

@core.route('/faqs')
def faqs():
    questions =Contact.query.all()
    context ={
        'questions':questions
    }
    return render_template('core/faqs.html', **context)











    # return jsonify(blogs)