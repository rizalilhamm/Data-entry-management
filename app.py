from flask import Flask, render_template, request, url_for, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskdb'

mysql = MySQL(app)

@app.route('/')
def home():
    cur = mysql.connection.cursor()
    cur.execute('select * from computer')
    rv = cur.fetchall()
    return render_template('home.html', computer=rv)

@app.route('/tambah', methods=['POST', 'GET'])
def tambah():
    if request.method == 'POST':
        nama = request.form['nama']
        cur = mysql.connection.cursor()
        cur.execute('insert into computer(data) values (%s)', (nama,))
        mysql.connection.commit()
        return redirect(url_for('home'))
    return render_template('tambah.html')

@app.route('/update/<string:id>', methods=['POST', 'GET'])
def update(id):
    if request.method == 'POST':
        nama = request.form['nama']
        cur = mysql.connection.cursor()
        cur.execute('update computer set data=%s where id=%s', (nama, id))
        mysql.connection.commit()
        return redirect(url_for('home'))
    return render_template('update.html')
@app.route('/delete/<string:id>', methods=['GET'])
def delete(id):
    cur = mysql.connection.cursor()
    cur.execute('delete from computer where id=%s', (id,))
    mysql.connection.commit()
    return redirect(url_for('home'))