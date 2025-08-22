import unittest
from unittest.mock import Mock, patch
from src.juego.cacho import Cacho

class TestCacho(unittest.TestCase):
    @patch('src.juego.cacho.Dado')
    def test_almacenar_dados(self, mock_dado_class):
        # Configura el mock para la clase Dado.
        mock_dado_instance = Mock()
        mock_dado_instance.generar_valor.return_value = 3
        mock_dado_class.return_value = mock_dado_instance

        cacho = Cacho()
        cacho_con_dados = cacho.almacenar_dados()
        self.assertEqual(len(cacho_con_dados), 5)

        for dado_en_cacho in cacho_con_dados:
            print(dado_en_cacho)
            self.assertIsInstance(dado_en_cacho,int)
            self.assertEqual(dado_en_cacho, 3)

    @patch('src.juego.cacho.Dado')
    def test_agitar_dados(self, mock_dado_class):
        mock_dado_instance = Mock()
        mock_dado_class.return_value = mock_dado_instance

        mock_dado_instance.generar_valor.side_effect = [1,2,3,4,5]
        cacho = Cacho()
        primera_tirada = cacho.almacenar_dados()

        mock_dado_instance.generar_valor.side_effect = [5,4,2,5,1]
        segunda_tirada = cacho.agitar_dados()

        self.assertNotEqual(primera_tirada, segunda_tirada)
        self.assertEqual(primera_tirada, [1,2,3,4,5])
        self.assertEqual(segunda_tirada, [5,4,2,5,1])