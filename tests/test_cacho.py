import unittest
from unittest.mock import Mock, patch
from src.juego.cacho import Cacho

class TestCacho(unittest.TestCase):
    @patch('src.juego.cacho.Dado')
    def test_almacenar_dados(self, mock_dado_class):
        # Configura el mock para la clase Dado.
        mock_instancia = Mock()
        mock_instancia.generar_valor.return_value = 3
        mock_dado_class.return_value = mock_instancia

        cacho = Cacho()
        cacho_con_dados = cacho.almacenar_dados()
        self.assertEqual(len(cacho_con_dados), 5)

        for dado_en_cacho in cacho_con_dados:
            print(dado_en_cacho)
            self.assertIsInstance(dado_en_cacho,int)
            self.assertEqual(dado_en_cacho, 3)


    #def test_agitar_dados(self):
     #   cacho = Cacho()
      #  cacho_con_dados = cacho.almacenar_dados()
