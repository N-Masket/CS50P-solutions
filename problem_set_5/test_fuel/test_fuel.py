from fuel import convert
from fuel import gauge
import pytest

def test_fraction():
    assert convert("3/4")==75

def test_raise_error():
    with pytest.raises((ZeroDivisionError)):
        convert("4/0")
    with pytest.raises((ValueError)):
        convert("10/3")
    with pytest.raises((ValueError)):
        convert("-1/4")

#gauge tests

def test_empty():
    assert gauge(1)=='E'

def test_full():
    assert gauge(99)=='F'

def test_other():
    assert gauge(40)=="40%"
