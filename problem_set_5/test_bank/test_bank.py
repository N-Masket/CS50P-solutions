from bank import value


def test_hello():
    assert value("hello")==0

def test_hi():
    assert value("Hi")==20

def test_other():
    assert value("Afternoon")==100


