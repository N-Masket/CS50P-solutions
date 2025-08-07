from twttr import shorten
import pytest



#test
def test_lowercase_vowel():
    assert shorten("name")=="nm"

def test_uppercase_vowel():
    assert shorten("nAmE")=="nm"

def test_num():
    assert shorten("1234")=="1234"

def test_punctuation():
    assert shorten(",,ESfg")==",,Sfg"
