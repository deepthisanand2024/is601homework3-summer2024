'''My Calculator Test'''
from calculator import Calculator

def test_addition():
    '''Test that addition function works '''
    assert Calculator.add(8,2) == 10

def test_subtraction():
    '''Test that subtraction function works '''
    assert Calculator.subtract(8,2) == 6

def test_multiplication():
    '''Test that multiplication function works '''
    assert Calculator.multiply(8,2) == 16

def test_division():
    '''Test that division function works '''
    assert Calculator.divide(8,2) == 4
