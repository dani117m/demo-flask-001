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
    lista = ['Pronvincias del Ecuador','Azuay','Bolívar','Cañar','Carchi','Chimborazo','Cotopaxi','El Oro','Esmeraldas','Galápagos','Guayas','Imbabura','Loja','Los Ríos','Manabí','Morona Santiago','Napo','Orellana','Pastaza','Pichincha','Santa Elena','Santo Domingo de los Tsáchilas','Sucumbíos','Tungurahua','Zamora Chinchipe']
    listado = ' <BR>'.join(lista)
    return "<h1>%s</h1>" % (listado)
 
