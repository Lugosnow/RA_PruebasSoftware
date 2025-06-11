from flask import Flask, request, jsonify
import operaciones

app = Flask(__name__)

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
    app.run(host='0.0.0.0', port=5000)
