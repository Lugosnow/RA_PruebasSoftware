from flask import Flask, request, jsonify, send_from_directory
import operaciones
import os

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/sumar', methods=['GET'])
def sumar():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    resultado = operaciones.sumar(a, b)
    return jsonify({"resultado": resultado})

@app.route('/restar', methods=['GET'])
def restar():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    resultado = operaciones.restar(a, b)
    return jsonify({"resultado": resultado})

@app.route('/multiplicar', methods=['GET'])
def multiplicar():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    resultado = operaciones.multiplicar(a, b)
    return jsonify({"resultado": resultado})

if __name__ == '__main__':
    print("API de operaciones matemáticas iniciada en http://localhost:5000")
    print("Endpoints disponibles: /sumar, /restar, /multiplicar")
    app.run(host='0.0.0.0', port=5000)
