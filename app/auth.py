from flask import Flask, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.urls import url_parse
from flask_login import current_user, login_user, login_required, logout_user

from app import app, db
from app import views
from app.models import User

@app.route('/<string:name>')
def user_profile(name):
    return render_template('user_profile.html', name=name, title=name)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash('Currently you are logging in')
        return redirect(url_for('index'))
    
    form = request.form
    email = form.get('email')
    password = form.get('password')
    remember = form.get('remember')

    if request.method == "POST":

        user = User.query.filter_by(email=email).first()

        if not user or not check_password_hash(user.password, password):
            flash("Invalid Email or Password")
            return redirect(url_for('login'))
        login_user(user, remember=remember)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)

    return render_template('login.html', title='Login')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = request.form
    name = form.get('name')
    email = form.get('email')
    password = form.get('password')
    confirm_password = form.get('confirm_password')

    if request.method == "POST":
        user = User.query.filter_by(email=email).first()
        if user is not None:
            flash("Email Sudah terdaftar silahkan coba login")
            return redirect(url_for('register'))
        elif password != confirm_password:
            flash("Password harus sama")
            return redirect(url_for('register'))

        new_user = User(name=name, email=email, password=generate_password_hash(password, method='sha256'))
        db.session.add(new_user)
        db.session.commit()
        flash("Selamat!, User sudah terdaftar.")
        return redirect(url_for('login'))

    return render_template('register.html', title='Register')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Anda sudah Keluar!')
    return redirect(url_for('login'))
