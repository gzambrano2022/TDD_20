import unittest
from unittest.mock import Mock, patch
from src.juego.cacho import Cacho
from src.juego.dado import Dado

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
            self.assertIsInstance(dado_en_cacho,int)
            self.assertEqual(dado_en_cacho, 3)

    def test_agitar_dados(self):
       cacho = Cacho()

       uno=cacho.almacenar_dados().copy()
       dos=cacho.agitar_dados().copy()

       self.assertNotEqual(uno, dos)

    def test_perder_dado(self):
        cacho = Cacho()
        dados_en_cacho = cacho.almacenar_dados().copy()
        eliminar_dado = cacho.perder_dado().copy()

        assert len(dados_en_cacho) > len(eliminar_dado)

    def test_ganar_dado(self):
        cacho = Cacho()
        dados_en_cacho = cacho.almacenar_dados().copy()
        cacho_con_dados_ganados = cacho.ganar_dado.copy()

        assert len(dados_en_cacho) < len(cacho_con_dados_ganados)