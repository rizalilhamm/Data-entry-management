import os
import jwt
import re
import smtplib, ssl
from flask import request, render_template, url_for, flash, redirect
from app import app, mail, db
from app.models import User
from flask_login import current_user
from flask_mail import Message
import datetime

# Membuat fungsi user bisa meminta untuk reset password
def send_reset_email(mail_receiver):
    token = jwt.encode({
        "email": mail_receiver,
    }, os.getenv('SECRET_KEY'), algorithm="HS256")
    smtp_server = "smtp.gmail.com"
    # mail_sender = os.getenv("MAIL_USER") or 'rzlilhm09@gmail.com'
    mail_sender = 'rzlilhm09@gmail.com'
    mail_password = os.environ.get("MAIL_PASSWORD")
    mail_port = os.environ.get('MAIL_PORT') or 465
    msg = f"""Password reset request To reset your password
          click the following link:
          {url_for('reset_password', token=token, _external=True)}
          
          if you did not make this request then simply ignore this email and no change will be made"""
    
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, mail_port, context=context) as server:
        server.login(mail_sender, mail_password)
        server.sendmail(mail_sender, mail_receiver, msg)

def validate_email(email):
    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    if not (re.search(regex, email)):
        flash("Invalid Email Format")
        return False
        
    return True

@app.route('/reset-request', methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    mail_receiver = request.form.get('email_reset_password')
    if request.method == 'POST':
        reload_url = redirect(url_for('reset_request'))
        user = User.query.filter_by(email=mail_receiver).first()
        if not mail_receiver:
            flash("Field empty")
            return reload_url
        if mail_receiver:
            if validate_email(mail_receiver) is False:
                flash("Invalid email")
                return reload_url
            if user:
                send_reset_email(mail_receiver)
        flash("Check your email to reset the password")
        return redirect(url_for('login'))

    return render_template('password_reset/reset_request.html', title="Reset Request")

@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    user = User.verify_reset_token(token)
    if user is None:
        flash("Invalid signature or expires token")
        return redirect(url_for('reset_request'))
    
    password = request.form.get('new_password')
    confirm_password = request.form.get('confirm_new_password')
    if request.method == 'POST':
        user.password = password
        user.hash_password()
        db.session.commit()
        flash("Your password has been updated! now you can login")
        return redirect(url_for('login'))
    
    return render_template('password_reset/reset_password.html', token=token, title="Reset Password")