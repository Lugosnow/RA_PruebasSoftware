import operaciones

def test_sumar():
    assert operaciones.sumar(2, 3) == 5

def test_restar():
    assert operaciones.restar(5, 3) == 2

def test_multiplicar():
    assert operaciones.multiplicar(2, 4) == 8
