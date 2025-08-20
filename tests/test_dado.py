import unittest
from src.juego.dado import Dado


class TestGenerarValor(unittest.TestCase):
    def test_generar_valor(self):
        dado = Dado()
        # generar valor del dado en rangos normales (1 a 6)
        valor = dado.generar_valor()
        self.assertGreaterEqual(valor, 1)
        self.assertLessEqual(valor, 6)

if __name__ == '__main__':
    unittest.main()
