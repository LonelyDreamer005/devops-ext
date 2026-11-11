import app

def test_fr():
    assert app.add(2, 3) == 5

def test_sc():
    assert app.sub(9, 9) == 0

def test_th():
    assert app.mul(2, 10) == 20