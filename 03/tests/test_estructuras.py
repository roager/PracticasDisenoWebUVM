
import unittest


lista1 = [1, 2, 3]
lista2 = ["a", 1]
lista3 = []
lista4 = ["a", "b"]

alumno1 = {
    "nombre": "jesus",
    "profesion": "administracion"
}

def longitud_lista(lista: list):
    """
    Funcion para regresar la longitud de una lista. 
    """
    return len(lista)


class TestEstructuras(unittest.TestCase):

    def test_longitud_lista(self):
        

        self.assertEqual(longitud_lista(lista1), 3)
        self.assertEqual(longitud_lista(lista2), 2)
        self.assertEqual(longitud_lista(lista3), 0)
    
    def test_listas(self):

        caracter1 = lista1[0]
        self.assertEqual(caracter1, 1)

        # Asegurarme que el segundo elemento de lista4 es "b"
        self.assertEqual(lista4[1], "b")

    def test_diccionario(self):
        nombre_notacion_1 = alumno1["nombre"]
        nombre_notacion_2 = alumno1.get("nombre")
        nombre_notacion_3 = alumno1.get("no_existe", 5)
        print("nombre")

    def test_calificaciones(self):

        calif_alumno_1 = 10
        calif_alumno_2 = 5

        calificaciones = []

        calificaciones.append(calif_alumno_1)
        calificaciones.append(calif_alumno_2)

        print(calificaciones)

        calificaciones[0] = 9

        print(calificaciones)



if __name__ == "__main__":
    unittest.main()
