import unittest
from src.juego.dado import dado


class TestGenerarValor(unittest.TestCase):
    def test_generar_valor(self):
        # generar valor del dado en rangos normales (1 a 6)
        valor = dado()
        self.assertGreaterEqual(valor, 1)
        self.assertLessEqual(valor, 6)

if __name__ == '__main__':
    unittest.main()
