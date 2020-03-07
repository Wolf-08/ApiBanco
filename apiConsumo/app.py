from flask import Flask 
from flask import render_template, request,flash
from flask import redirect, url_for
from flask import jsonify
import json , requests


app= Flask(__name__)

#app.secret_key = 'keysecret'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cajero',methods=['POST'])
def cajero():
    if request.method == 'POST':
        id_cuenta = request.form['id_cuenta']
        ap_pat = request.form['ap_pat']
        ap_mat = request.form['ap_mat']
        ruta = 'http://127.0.0.1:8000/api/cuentas/' + id_cuenta
        try:
            datos = requests.get(ruta)
            resp = json.loads(datos.content)
            print(resp)
        except:
            return 'A ocurrido un error no se obtuvieron los datos'
    return render_template('cuentas.html',datos=resp)


@app.route('/cliente',methods=['POST'])
def usuario():
    if request.method == 'POST':
        user_id = request.form['user_id']
        nombre = request.form['nombre']
        ap_pat = request.form['ap_pat']
        ap_mat = request.form['ap_mat']
        ruta = 'http://127.0.0.1:8000/api/clientes/' + user_id
        try:
            datos = requests.get(ruta)
            resp = json.loads(datos.content)
            print(resp)
        except:
            return 'A ocurrido un error no se obtuvieron los datos'
    return render_template('clientes.html',datos=resp)
@app.route('/compartida',methods=['POST'])
def compartida():
    if request.method == 'POST':
        id_cuentaC = request.form['id_cuentaC']
        #nombre = request.form['nombre']
        ap_pat = request.form['ap_pat']
        ap_mat = request.form['ap_mat']
        ruta = 'http://127.0.0.1:8000/api/cuentaCliente/' + id_cuentaC
        try:
            datos = requests.get(ruta)
            resp = json.loads(datos.content)
            print(resp)
        except:
            return 'A ocurrido un error no se obtuvieron los datos'
    return render_template('compartida.html',datos=resp)
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status' : 404,
        'message' : 'Not Found ' + request.url,
    }
    resp = jsonify(message)
    return resp

if __name__ == '__main__':
    app.run(debug = True)

