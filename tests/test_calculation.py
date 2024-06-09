'''My Calculator Test'''
from calculator.operations import add, subtract, multiply, divide

def test_addition():
    '''Test that addition function works '''
    assert add(8,2) == 10

def test_subtraction():
    '''Test that subtraction function works '''
    assert subtract(8,2) == 6

def test_multiplication():
    '''Test that multiplication function works '''
    assert multiply(8,2) == 16

def test_division():
    '''Test that division function works '''
    assert divide(8,2) == 4
    