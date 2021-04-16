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
    return "<h1>Provincias costa</h1>"
    return "<h2> Esmeraldas - Capital Esmeraldas <br> Manabí - Capital Portoviejo <br> Los Ríos - Capital Babahoyo <br> Santa Elena - Capital Santa Elena <br> Guayas - Capital Guayaquil <br> Santo Domingo de los Tsáchilas - Capital Santo Domingo <br> El Oro - Capital Machala </h2>"
 
