print("hola")

# Las constantes se escriben con mayusculas
CONSTANTE = 5

# Los nombres de clase se UpperCamelCase
class ConvertidorDivisas:

    def __init__(self):
        pass


# En general nombres de variables y funciones en snake_case
def convertir_celsius_fahrenheit(x: float):
    """
    Función para convertir grados celsius a fahrenheit de acuerdo a la formula
    9/5x + 32. 
    """
    pass 
    grados_fahrenheit = 9/5 * x + 32
    return grados_fahrenheit


grados_celsius = 25

grados_fahrenheit = convertir_celsius_fahrenheit(x=grados_celsius)

# Yo espero que 25 grados C sean 77 grados F
print(f"{grados_celsius} grados C son {grados_fahrenheit} grados F")
