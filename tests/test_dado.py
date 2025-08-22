import unittest
from unittest import mock
from unittest.mock import patch

from src.juego.dado import Dado


class TestDado(unittest.TestCase):
    @patch('src.juego.dado.random.randint', return_value=5)
    def test_generar_valor(self, mock_valor):
        dado = Dado()
        # generar valor del dado en rangos normales (1 a 6)
        valor = dado.generar_valor()
        self.assertGreaterEqual(valor, 1)
        self.assertLessEqual(valor, 6)
        self.assertEqual(valor, 5)


        valores = [1,2,3,4,5,6]
        self.assertIn(valor, valores)

    def test_designacion(self):
        dado = Dado()
        valor = dado.generar_valor()
        nombre = dado.designacion(valor)
        self.assertIn(nombre, ["As", "Tonto", "Tren", "Cuadra", "Quina", "Sexto"])



if __name__ == '__main__':
    unittest.main()
