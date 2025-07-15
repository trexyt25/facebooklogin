
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    conn = sqlite3.connect('usuarios.db')
    conn.execute('INSERT INTO usuarios (email, password) VALUES (?, ?)', (email, password))
    conn.commit()
    conn.close()

    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
