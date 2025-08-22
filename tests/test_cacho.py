import unittest
from unittest.mock import Mock, patch
from src.juego.cacho import Cacho

class TestCacho(unittest.TestCase):
    @patch('src.juego.cacho.Dado')
    def test_almacenar_dados(self, mock_dado_class):
        # Configura el mock para la clase Dado.
        mock_dado = Mock()
        mock_dado_class.return_value = mock_dado

        cacho = Cacho()
        cacho_con_dados = cacho.almacenar_dados()
        self.assertEqual(len(cacho_con_dados), 5)

        for dado_en_cacho in cacho_con_dados:
            self.assertIsInstance(dado_en_cacho,Mock)

        self.assertEqual(mock_dado_class.call_count, 5)
