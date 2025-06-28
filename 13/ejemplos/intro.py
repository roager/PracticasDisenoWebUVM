# Clase 16: Introducción a Python
# ===================================
# Este archivo contiene ejemplos didácticos para explicar los temas fundamentales de la clase 16.

# -------------------------------
# 1. Primer programa en Python
# -------------------------------
print("Hola, mundo")  # Imprime un mensaje en pantalla

# -------------------------------
# 2. Operadores, expresiones y sentencias
# -------------------------------
resultado = 10 + 5  # Operador aritmético +
print("Resultado de 10 + 5:", resultado)

# Expresión: devuelve un valor
area = (3 * 4) + 2  # Multiplicación y suma
print("Área:", area)

# Sentencia: acción completa (asignación, condicional, etc.)
if area > 10:
    print("El área es mayor que 10")

# -------------------------------
# 3. Sentencias de más de una línea
# -------------------------------
suma_larga = 1 + 2 + 3 + 4 + 5 + 6
print("Suma larga:", suma_larga)

# Otra forma con listas (continuación implícita)
numeros = [1, 2, 3, 4, 5, 6]
print("Números:", numeros)


# -------------------------------
# 4. Indentación
# -------------------------------
def saludar(nombre):
    print("Hola,", nombre)


saludar("Python")

# -------------------------------
# 5. Comentarios
# -------------------------------
# Esto es un comentario de una sola línea
"""Esto es un comentario
que ocupa varias líneas"""


# -------------------------------
# 6. Docstrings
# -------------------------------
def sumar(a, b):
    """
    Suma dos números y devuelve el resultado.
    Esta función es un ejemplo de uso de docstrings.
    """
    return a + b


print("5 + 3 =", sumar(5, 3))

# -------------------------------
# 7. Convenciones de nombres
# -------------------------------
# Variables
contador = 0
suma_total = 100


# Clases
class Vehiculo:
    pass


# Python distingue mayúsculas de minúsculas
Variable_1 = 10
variable_1 = 5
print("Distintas variables:", Variable_1, variable_1)

# -------------------------------
# 8. Palabras reservadas
# -------------------------------
# Algunas palabras reservadas: if, else, for, while, def, class, return, True, False, None

# -------------------------------
# 9. Constantes
# -------------------------------
# Aunque Python no tiene constantes reales, se puede usar convenciones
PI = 3.14159  # Se escribe en mayúsculas para indicar que es constante

# -------------------------------
# 10. Tipado dinámico y fuerte
# -------------------------------
x = 10  # tipo entero
x = "ahora soy string"  # cambia a string
print(x)

# Python no permite esto: print("5" + 5) # Error: tipos incompatibles
# Hay que convertirlos explícitamente:
print("5" + str(5))  # Correcto
