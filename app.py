from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request
import os

app = Flask(__name__)

# URL de conexión que Render te dio
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://USUARIO:PASSWORD@HOST:PORT/NOMBRE_DB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    correo = db.Column(db.String(120))
    contraseña = db.Column(db.String(120))

from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")

    nuevo_usuario = Usuario(correo=email, contraseña=password)
    db.session.add(nuevo_usuario)
    db.session.commit()

    return render_template("exito.html")  # o el archivo HTML que muestra el mensaje final

if __name__ == '__main__':
    app.run(debug=True)
if __name__ == "__main__":
    app.run()
@app.before_first_request
def crear_tabla():
    db.create_all()
