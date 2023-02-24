from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")

def hola_mundo():
    return "<p>Hola mundooo</p>"

@app.route('/usuario/<usernamee>')
def mostrar_usuario(usernamee):
    return f"<p>Usuario: {escape(usernamee)}!</p>"

@app.route('/post/<int:post_id>')

def mostrar_post(post_id):
    return f"<p>Post id: {escape(post_id)}</p>"

@app.route('/github')

def saludogithub():
    return "<p>Esto fue commiteado desde la web de github. Editado</p>"
