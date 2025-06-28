# math_utils.py

def add(a, b):
    """Devuelve la suma de dos números."""
    return a + b

def multiply(a, b):
    """Devuelve la multiplicación de dos números."""
    return a * b

def divide(a, b):
    """Devuelve la división de dos números, o un mensaje si el divisor es 0."""
    if b == 0:
        return "No se puede dividir por cero"
    return a / b 
