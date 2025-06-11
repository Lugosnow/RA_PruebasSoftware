import requests

def test_funcional_suma():
    respuesta = requests.get("http://localhost:5000/sumar?a=3&b=2")
    assert respuesta.json()['resultado'] == 5

def test_funcional_resta():
    respuesta = requests.get("http://localhost:5000/restar?a=5&b=2")
    assert respuesta.json()['resultado'] == 3
