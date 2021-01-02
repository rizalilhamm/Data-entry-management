from flask import render_template, request, redirect, url_for, flash
from app import app, db
from models import Post

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
@app.route('/dashboard/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts, title='Home')

@app.route('/add/', methods=["POST", "GET"])
def add_post():
    if request.method == "POST":
        name = request.form['name']
        desc = request.form['desc']
        if name is not None:
            post = Post(name=name, desc=desc)
            db.session.add(post)
            db.session.commit()
            flash("Data Posted successfully!")
            return redirect('/dashboard')
    return render_template('add_post.html', title='Add New')

@app.route('/<int:id>/')
def detail_post(id):
    post = Post.query.filter_by(id=id).first()
    return render_template('detail_post.html', title='Detail Post', post=post)
    
@app.route('/<int:id>/edit/', methods=["POST", "GET"])
def edit_post(id):
    post = Post.query.filter_by(id=id).first()
    if request.method == "POST":
        post.name = request.form['name']
        post.desc = request.form['desc']
        db.session.commit()
        flash("Data Updated!")
        return redirect(url_for('detail_post', id=post.id))
    return render_template('edit_post.html', title='Edit Post', post=post)

@app.route('/<int:id>/delete', methods=["POST", "GET"])
def delete_post(id):
    post = Post.query.filter_by(id=id).first()
    if request.method == "POST":
        db.session.delete(post)
        db.session.commit()
        flash("Post deleted!")
        return redirect(url_for('index'))
    return render_template('confirm_delete.html', title='Delete Post', post=post)