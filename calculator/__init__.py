from calculator.operations import add, subtract, multiply, divide
from calculator.calculation import calculation

class Calculator:
    @staticmethod
    def add(a,b):
        cal = calculation(a, b, add)  # Pass the add function from calculator.operations
        return cal.getOutput()
    
    @staticmethod
    def subtract(a,b):
        cal = calculation(a, b, subtract)  # Pass the add function from calculator.operations
        return cal.getOutput()
    
    @staticmethod
    def multiply (a,b):
        cal = calculation(a, b, multiply)  # Pass the add function from calculator.operations
        return cal.getOutput()
    
    @staticmethod
    def divide(a,b):
        cal = calculation(a, b, divide)  # Pass the add function from calculator.operations
        return cal.getOutput()