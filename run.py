"""
Introducción a Flask
https://parzibyte.me/blog
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def inicio():
    return "<h1>Hola mundo con Flask levantado desde heroku</h1>"
    return "<h1>dani117m</h1>"

@app.route('/suma')
def suma():
    resultado = 10 + 10
    return "<h3>10 + 10 = %d</h3>" % (resultado)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)
    
@app.route('/lista')
def lista():
    return "<h2>Provincias costa</h2>"
    return "<p> Esmeraldas - Capital Esmeraldas </p>"
    return "<p> Manabí - Capital Portoviejo </p>"
    return "<p> Los Ríos - Capital Babahoyo </p>"
    return "<p> Santa Elena - Capital Santa Elena </p>"
    return "<p> Guayas - Capital Guayaquil </p>"
    return "<p> Santo Domingo de los Tsáchilas - Capital Santo Domingo </p>"
    return "<p> El Oro - Capital Machala </p>"
