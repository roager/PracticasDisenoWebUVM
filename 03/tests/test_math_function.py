# test_math_utils.py

import unittest
from math_utils import add, multiply, divide

class TestMathUtils(unittest.TestCase):
    def test_add(self):
        """Pruebas para la función add."""
        self.assertEqual(add(2, 3), 5)  # Caso positivo
        self.assertEqual(add(-1, 1), 0)  # Suma con negativos
        self.assertEqual(add(0, 0), 0)  # Suma con ceros

    def test_multiply(self):
        """Pruebas para la función multiply."""
        self.assertEqual(multiply(2, 3), 6)  # Multiplicación simple
        self.assertEqual(multiply(-1, 3), -3)  # Multiplicación con negativos
        self.assertEqual(multiply(0, 5), 0)  # Multiplicación por cero

    def test_divide(self):
        """Pruebas para la función divide."""
        self.assertEqual(divide(6, 3), 2)  # División simple
        self.assertEqual(divide(5, 0), "No se puede dividir por cero")  # División por cero
        self.assertEqual(divide(0, 5), 0)  # División de cero entre un número

if __name__ == "__main__":
    unittest.main()
