import unittest
from src.juego.dado import Dado


class TestDado(unittest.TestCase):
    def test_generar_valor(self):
        dado = Dado()
        # generar valor del dado en rangos normales (1 a 6)
        valor = dado.generar_valor()
        self.assertGreaterEqual(valor, 1)
        self.assertLessEqual(valor, 6)

    def test_designacion(self):
        dado = Dado()
        valor = dado.generar_valor()
        nombre = dado.designacion(valor)
        self.assertIn(nombre, ["As", "Tonto", "Tren", "Cuadra", "Quina", "Sexto"])


if __name__ == '__main__':
    unittest.main()
