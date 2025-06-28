import unittest

def recuperar_todas_las_calificaciones_de_alumno(calificaciones: dict, alumno: str):
    # TODO: leer las calificaciones de un alumno y regresarlas
    return calificaciones.get(alumno, []) 

def recuperar_una_calificacion(calificaciones: dict, alumno: str, indice_calificacion: int):
    # TODO: leer una calificacion especifica de un alumno
    if alumno in calificaciones and 0 <= indice_calificacion < len(calificaciones[alumno]):
        return calificaciones[alumno][indice_calificacion]
    return None
def calcular_promedio(calificaciones: dict, alumno: str):
    # TODO: recuperar todas las calificaciones de un alumno y calcular su promedio
    todas_las_calificaciones = recuperar_todas_las_calificaciones_de_alumno(calificaciones, alumno)
    if todas_las_calificaciones:
        return sum(todas_las_calificaciones) / len(todas_las_calificaciones)
    return 0

def modificar_calificacion(calificaciones: dict, alumno: str, indice_de_calificacion_a_modificar: int, nueva_calificacion: int):
    # TODO: actualizar una calificacion en el diccionario de calificaciones. 
    #   Pista: calificaciones[alumno][indice]
    if alumno in calificaciones and 0 <= indice_de_calificacion_a_modificar < len(calificaciones[alumno]):
        calificaciones[alumno][indice_de_calificacion_a_modificar] = nueva_calificacion


calificaciones = {
    "jorge": [10, 5, 10, 8],
    "luis": [9, 9, 9, 8],
    "berenice": [10, 10, 10, 10]
}

class TestCalificaciones(unittest.TestCase):

    def test_recuperar_todas_las_calificaciones_de_alumno(self):
        resultado = recuperar_todas_las_calificaciones_de_alumno(calificaciones, "jorge")
        self.assertEqual(resultado, [10, 5, 10, 8], "Error al recuperar todas las calificaciones de Jorge")

    def test_recuperar_una_calificacion(self):
        resultado = recuperar_una_calificacion(calificaciones, "jorge", 1)
        self.assertEqual(resultado, 5, "Error al recuperar la calificación específica de Jorge")

    def test_calcular_promedio(self):
        promedio = calcular_promedio(calificaciones, "luis")
        self.assertEqual(promedio, 8.75, "Error al calcular el promedio de Luis")

    def test_modificar_calificacion(self):
        nuevo_valor = 7
        modificar_calificacion(calificaciones, "berenice", 2, nuevo_valor)  # Cambiar la tercera calificación
        resultado = recuperar_todas_las_calificaciones_de_alumno(calificaciones, "berenice")
        self.assertEqual(resultado, [10, 10, 7, 10], "Error al modificar la calificación de Berenice")

if __name__ == "__main__":
    unittest.main()