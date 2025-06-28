# Prueba Rogelio Guzman - para dar PUSH al Repositorio SIN modificar el codigo original...


import unittest


def recuperar_todas_las_calificaciones_de_alumno(calificaciones: dict, alumno: str):
    return calificaciones.get(alumno)


def recuperar_una_calificacion(
    calificaciones: dict, alumno: str, indice_calificacion: int
):
    # esto es una lista
    todas_las_calificaciones_del_alumno = calificaciones.get(alumno)
    return todas_las_calificaciones_del_alumno[indice_calificacion]


def calcular_promedio(calificaciones: dict, alumno: str):
    if len(calificaciones[alumno]) == 0:
        return False
    todas_las_calificaciones_del_alumno = calificaciones.get(alumno)
    return sum(todas_las_calificaciones_del_alumno) / len(
        todas_las_calificaciones_del_alumno
    )


def modificar_calificacion(
    calificaciones: dict,
    alumno: str,
    indice_de_calificacion_a_modificar: int,
    nueva_calificacion: int,
):
    calificaciones.get(alumno)[indice_de_calificacion_a_modificar] = nueva_calificacion
    return False


calificaciones = {
    "jorge": [10, 5, 10, 8],
    "luis": [9, 9, 9, 8],
    "berenice": [10, 10, 10, 10],
}


class TestCalificaciones(unittest.TestCase):

    def test_recuperar_todas_las_calificaciones_de_alumno(self):
        resultado = recuperar_todas_las_calificaciones_de_alumno(
            calificaciones, "jorge"
        )
        self.assertEqual(
            resultado,
            [10, 5, 10, 8],
            "Error al recuperar todas las calificaciones de Jorge",
        )

    def test_recuperar_una_calificacion(self):
        resultado = recuperar_una_calificacion(
            calificaciones=calificaciones, alumno="jorge", indice_calificacion=1
        )
        self.assertEqual(
            resultado, 5, "Error al recuperar la calificación específica de Jorge"
        )

    def test_calcular_promedio(self):
        promedio = calcular_promedio(calificaciones, "luis")
        self.assertEqual(promedio, 8.75, "Error al calcular el promedio de Luis")

    def test_calcular_promedio_de_calificaciones_vacias(self):
        promedio = calcular_promedio({"luis": []}, "luis")
        self.assertFalse(promedio)

    def test_modificar_calificacion(self):
        nuevo_valor = 7
        modificar_calificacion(
            calificaciones, "berenice", 2, nuevo_valor
        )  # Cambiar la tercera calificación
        resultado = recuperar_todas_las_calificaciones_de_alumno(
            calificaciones, "berenice"
        )
        self.assertEqual(
            resultado, [10, 10, 7, 10], "Error al modificar la calificación de Berenice"
        )


if __name__ == "__main__":
    unittest.main()
