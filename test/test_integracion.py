from main import app

def test_sumar_integracion():
    cliente = app.test_client()
    respuesta = cliente.get('/sumar?a=2&b=3')
    assert respuesta.json['resultado'] == 5

def test_restar_integracion():
    cliente = app.test_client()
    respuesta = cliente.get('/restar?a=5&b=2')
    assert respuesta.json['resultado'] == 3
