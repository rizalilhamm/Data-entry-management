from flask import render_template, request, redirect, flash, url_for
from app import app, db
from app.models import Entry

@app.route('/')
@app.route('/index')
def index():
    entries = Entry.query.all()
    return render_template('index.html', entries=entries)

@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        form = request.form
        title = form.get('title')
        description = form.get('description')
        if title != '' or description != '':
            entry = Entry(title=title, description=description)
            db.session.add(entry)
            db.session.commit()
            return redirect('/')
        else:
            flash("Form wajib isi")
            return redirect('/')
    return render_template('add.html', title='Add Item')

@app.route('/update/<int:id>', methods=['POST', 'GET'])
def update(id):
    entry = Entry.query.get(id)
    if entry:
        if request.method == 'POST':
            entry.title = request.form['title']
            entry.description = request.form['description']
            db.session.commit()
            return redirect('/')
        return render_template('update.html', entry=entry, title='Update')
    
    return "of the jedi"

def confirm_delete(entry):
    if request.method == 'POST':
        db.session.delete(entry)
        db.session.commit()
        flash("Data Deleted!")
        return redirect('/')
    return render_template('confirm_delete.html', entry=entry, title='Delete')

@app.route('/delete/<int:id>', methods=['POST', 'GET'])
def delete(id):
    if not id or id != 0:
        entry = Entry.query.get(id)
        if entry:
            return confirm_delete(entry)
                
    return "Delete"

@app.route('/turn/<int:id>')
def turn(id):
    if not id or id != 0:
        entry = Entry.query.get(id)
        if entry:
            entry.status = not entry.status
            db.session.commit()
        return redirect('/')
    
    return "of the jedi"