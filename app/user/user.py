from flask import render_template, redirect, request, url_for, flash
from flask_login import current_user

from app import app, db


@app.route('/profile/<string:name>')
def user_profile(name):
    return render_template('user_profile.html', name=name, title=name)

@app.route('/update/<string:name>', methods=('POST', 'GET'))
def update_profile(name):
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    if current_user.name != name:
        return redirect(url_for('profile/<string:name>')) 


    form = request.form
    name = form.get('name')
    email = form.get('email')
    about = form.get('about')
    if request.method == "POST":
        current_user.name = name
        current_user.about = about
        if email != current_user.email:
            flash('Email ga bisa di ubah')
            return redirect(url_for('update_profile'))
        db.session.commit()
        flash('Profile Updated successfully!')
        return redirect(url_for('profile/<string:name>'))
    
    return render_template('update_profile.html', title='Update Profile')

    