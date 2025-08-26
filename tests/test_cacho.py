import pytest
from unittest.mock import Mock, patch
from src.juego.cacho import Cacho

class TestCacho:

    @patch('src.juego.cacho.Dado')
    def test_almacenar_dados(self, mock_dado_class):
        # Configura el mock para la clase Dado.
        mock_dado_instance = Mock()
        mock_dado_instance.generar_valor.return_value = 3
        mock_dado_class.return_value = mock_dado_instance

        cacho = Cacho()
        cacho_con_dados = cacho.almacenar_dados()
        assert len(cacho_con_dados) == 5

        for dado_en_cacho in cacho_con_dados:
            assert isinstance(dado_en_cacho, int)
            assert dado_en_cacho == 3

    def test_agitar_dados(self):
        cacho = Cacho()

        uno = cacho.almacenar_dados().copy()
        dos = cacho.agitar_dados().copy()

        assert uno != dos

    def test_perder_dado(self):
        cacho = Cacho()
        dados_en_cacho = cacho.almacenar_dados().copy()
        eliminar_dado = cacho.perder_dado().copy()

        assert len(dados_en_cacho) > len(eliminar_dado)

    def test_ganar_dado(self):
        cacho = Cacho()
        cacho.almacenar_dados()
        cantidad_inicial = len(cacho.almacen)
        reserva_inicial = cacho.count

        cacho.ganar_dado()

        if cantidad_inicial < 5:
            assert len(cacho.almacen) == cantidad_inicial + 1
            assert cacho.count == reserva_inicial
        else:
            assert len(cacho.almacen) == cantidad_inicial
            assert cacho.count == reserva_inicial + 1

    def test_perder_dado_con_count_mayor_cero_y_almacen_menor_5(self):
        cacho = Cacho()

        cacho.almacen = [1, 2, 3]
        cacho.count = 2
        cantidad_inicial = len(cacho.almacen)
        count_inicial = cacho.count

        resultado = cacho.perder_dado()

        assert len(resultado) == cantidad_inicial + 1
        assert cacho.count == count_inicial - 1

    def test_perder_dado_con_count_mayor_cero_y_almacen_igual_5(self):
        cacho = Cacho()

        cacho.almacen = [1, 2, 3, 4, 5]
        cacho.count = 2
        cantidad_inicial = len(cacho.almacen)
        count_inicial = cacho.count

        resultado = cacho.perder_dado()

        assert len(resultado) == cantidad_inicial
        assert cacho.count == count_inicial - 1

    def test_perder_dado_con_count_cero(self):
        cacho = Cacho()

        cacho.almacen = [1, 2, 3, 4, 5]
        cacho.count = 0
        cantidad_inicial = len(cacho.almacen)

        resultado = cacho.perder_dado()

        assert len(resultado) == cantidad_inicial - 1
        assert cacho.count == 0

    def test_ganar_dado_con_almacen_lleno(self):
        cacho = Cacho()

        cacho.almacen = [1, 2, 3, 4, 5]
        cacho.count = 0
        cantidad_inicial = len(cacho.almacen)
        count_inicial = cacho.count

        resultado = cacho.ganar_dado()

        assert len(resultado) == cantidad_inicial
        assert cacho.count == count_inicial + 1

    def test_ganar_dado_con_almacen_vacio(self):
        cacho = Cacho()

        cacho.almacen = []
        cacho.count = 0
        cantidad_inicial = len(cacho.almacen)
        count_inicial = cacho.count

        resultado = cacho.ganar_dado()

        assert len(resultado) == cantidad_inicial + 1
        assert cacho.count == count_inicial

    def test_ganar_dado_con_almacen_parcialmente_lleno(self):
        cacho = Cacho()

        cacho.almacen = [1, 2, 3]
        cacho.count = 1
        cantidad_inicial = len(cacho.almacen)
        count_inicial = cacho.count

        resultado = cacho.ganar_dado()

        assert len(resultado) == cantidad_inicial + 1
        assert cacho.count == count_inicial

