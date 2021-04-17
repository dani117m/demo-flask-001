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
    lista = ['Provincias tiene la costa', 'Esmeraldas - Capital Esmeraldas', 'Manabí - Capital Portoviejo', 'Los Ríos - Capital Babahoyo', 'Santa Elena - Capital Santa Elena', 'Guayas - Capital Guayaquil' ,'Santo Domingo de los Tsáchilas - Capital Santo Domingo','El Oro - Capital Machala']
    lista2 = ['Provincias tiene la Sierra', 'Azuay - Capital Cuenca', 'Bolívar - Capital Guaranda', 'Cañar - Capital Azogues', 'Carchi - Capital Tulcán', 'Cotopaxi - Capital Latacunga', 'Chimborazo - Capital Riobamba', 'Imbabura - Capital Ibarra', 'Loja - Capital Loja ','Pichincha - Capital Quito' , 'Tungurahua - Capital Ambato']
    lista3 = ['Provincias tiene el Oriente', 'Morona Santiago - Capital Macas',' Napo - Capital Tena', 'Orellana - Capital Orellana', 'Pastaza - Capital Puyo', 'Sucumbíos - Capital Lago Agrio', 'Zamora Chinchipe - Capital Zamora']
    tab = '<BR>'.join(lista)
    tab2 = '<BR>'.join(lista2)
    tab3 = '<BR>'.join(lista3)
    return "<h1>%s %s %s</h1>" % (tab,tab2,tab3)
 
