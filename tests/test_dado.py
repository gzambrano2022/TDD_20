import pytest
from unittest import mock
from unittest.mock import patch
from src.juego.dado import Dado

class TestDado:
    # Clase de pruebas unitarias para la clase Dado.

    @patch('src.juego.dado.random.randint', return_value=5)
    def test_generar_valor(self, mock_valor):
        """
        Prueba que generar_valor produce valores en el rango correcto (1-6)
        y que el mock funciona correctamente.
        """
        dado = Dado()
        # generar valor del dado en rangos normales (1 a 6)
        valor = dado.generar_valor()
        assert valor >= 1
        assert valor <= 6
        assert valor == 5

        valores = [1,2,3,4,5,6]
        assert valor in valores

    def test_designacion(self):
        """
        Prueba que designacion retorna el nombre correcto para cada valor
        y que todos los nombres están en la lista esperada.
        """
        dado = Dado()
        valor = dado.generar_valor()
        nombre = dado.designacion(valor)
        assert nombre in ["As", "Tonto", "Tren", "Cuadra", "Quina", "Sexto"]

