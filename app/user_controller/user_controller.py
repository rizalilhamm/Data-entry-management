from flask import render_template, redirect, request, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user, login_required

from app import app, db
from app.models import User

@app.route('/profile')
@login_required
def user_profile():
    """ Fungsi ini berjalan untuk menampilkan Profile User
        param:
            name(string): user name
        url:
            /profile
        return:
            user_profil(page): user profile """
    name = current_user.name
    return render_template('user_profile.html', name=name.capitalize())

@app.route('/profile/update/<string:name>', methods=('POST', 'GET'))
def update_profile(name):
    """ Digunakan untuk melakukan update user Profile or data
        param:
            semua data yang bersifat pribadi, selain email yan unchangable 
        return:
            update_profile(function): update profile template """
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    
    if current_user.name != name:
        return redirect(url_for('profile/<string:name>')) 

    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        about = request.form.get('about')
        
        current_user.name = name
        current_user.about = about
        db.session.commit()
        flash("Profile berhasil diupdate")
        return redirect(url_for('user_profile', name=current_user.name))
    
    return render_template('update_profile.html', title='Update Profile')

@app.route('/profile/change-password', methods=('POST', 'GET'))
@login_required
def change_password():
    """ Digunakan untuk melakukan update pada user password 
        params:
            password_lama(string): password lama user 
            password_baru(string): password baru user
            konfirmasi_password_baru(string): konfirmasi password baru user
        return:
            change_password(function): user change password"""
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    
    if request.method == "POST":
        password_lama = request.form.get('password_lama')
        password_baru = request.form.get('password_baru')
        konfirmasi_password_baru = request.form.get('konfirmasi_password_baru')

        # jika false maka ulangi
        if not check_password_hash(current_user.password, password_lama):
            flash("Password lama yang anda masukkan salah")
            return redirect(url_for('change_password'))
        # jika field masih ada yang kosong maka ulangi
        if not password_baru or not konfirmasi_password_baru:
            flash("Kolom password lama atau password baru harus diisi")
            return redirect(url_for('change_password'))
        # jika tidak kosong kosong maka bandingkan dan commit pada server
        if password_baru and konfirmasi_password_baru:
           
            if password_baru == konfirmasi_password_baru:
           
                if password_lama == password_baru:
                    flash("password anda tidak berubah")
                    return redirect(url_for('user_profile'))
                current_user.password = generate_password_hash(password_baru)
                db.session.commit()
           
                flash("Password sudah diperbaharui")
                return redirect(url_for('user_profile'))

    return render_template('change_password.html', title='Change Password')