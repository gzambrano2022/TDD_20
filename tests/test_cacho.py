import pytest
from unittest.mock import Mock, patch
from src.juego.cacho import Cacho

class TestCacho:
    # Clase de pruebas unitarias para la clase Cacho
    @patch('src.juego.cacho.Dado')
    def test_almacenar_dados(self, mock_dado_class):
        """
        Prueba que almacenar_dados genera la cantidad correcta de dados
        y que todos tienen valores válidos.
        """
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
        """
        Prueba que agitar_dados genera nuevos valores diferentes
        a los anteriores.
        """
        cacho = Cacho()

        uno = cacho.almacenar_dados().copy()
        dos = cacho.agitar_dados().copy()

        assert uno != dos

    def test_perder_dado(self):
        """
        Prueba básica que perder_dado reduce la cantidad de dados.
        """
        cacho = Cacho()
        dados_en_cacho = cacho.almacenar_dados().copy()
        eliminar_dado = cacho.perder_dado().copy()

        assert len(dados_en_cacho) > len(eliminar_dado)

    def test_ganar_dado(self):
        """
        Prueba que ganar_dados incrementa la cantidad de dados o el contador
        dependiendo del estado actual.
        """
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
        """
        Prueba perder_dado cuando count>0 y almacén tiene menos de 5 dados.
        """
        cacho = Cacho()

        cacho.almacen = [1, 2, 3]
        cacho.count = 2
        cantidad_inicial = len(cacho.almacen)
        count_inicial = cacho.count

        resultado = cacho.perder_dado()

        assert len(resultado) == cantidad_inicial + 1
        assert cacho.count == count_inicial - 1

    def test_perder_dado_con_count_mayor_cero_y_almacen_igual_5(self):
        """
        Prueba perder_dado cuando count>0 y almacén tiene exactamente 5 dados.
        """
        cacho = Cacho()

        cacho.almacen = [1, 2, 3, 4, 5]
        cacho.count = 2
        cantidad_inicial = len(cacho.almacen)
        count_inicial = cacho.count

        resultado = cacho.perder_dado()

        assert len(resultado) == cantidad_inicial
        assert cacho.count == count_inicial - 1

    def test_perder_dado_con_count_cero(self):
        """
        Prueba perder_dado cuando count==0 (debe eliminar un dado del cacho)
        """
        cacho = Cacho()

        cacho.almacen = [1, 2, 3, 4, 5]
        cacho.count = 0
        cantidad_inicial = len(cacho.almacen)

        resultado = cacho.perder_dado()

        assert len(resultado) == cantidad_inicial - 1
        assert cacho.count == 0

    def test_ganar_dado_con_almacen_lleno(self):
        """
        Prueba ganar_dado cuando el almacén está lleno
        (debe incrementar count)
        """
        cacho = Cacho()

        cacho.almacen = [1, 2, 3, 4, 5]
        cacho.count = 0
        cantidad_inicial = len(cacho.almacen)
        count_inicial = cacho.count

        resultado = cacho.ganar_dado()

        assert len(resultado) == cantidad_inicial
        assert cacho.count == count_inicial + 1

    def test_ganar_dado_con_almacen_vacio(self):
        """
        Prueba ganar_dado cuando el almacén está vacío
        (debe añadir un dado)
        """
        cacho = Cacho()

        cacho.almacen = []
        cacho.count = 0
        cantidad_inicial = len(cacho.almacen)
        count_inicial = cacho.count

        resultado = cacho.ganar_dado()

        assert len(resultado) == cantidad_inicial + 1
        assert cacho.count == count_inicial

    def test_ganar_dado_con_almacen_parcialmente_lleno(self):
        """
        Prueba ganar_dado cuando el almacén tiene dados pero no está lleno
        """
        cacho = Cacho()

        cacho.almacen = [1, 2, 3]
        cacho.count = 1
        cantidad_inicial = len(cacho.almacen)
        count_inicial = cacho.count

        resultado = cacho.ganar_dado()

        assert len(resultado) == cantidad_inicial + 1
        assert cacho.count == count_inicial

    def test_visibilidad_dados(self):
        """
        Prueba la funcionalidad de cambiar visibilidad_dados.
        """
        cacho = Cacho()
        cacho.almacen = [5]

        # Primera activación debería funcionar
        exito, mensaje = cacho.visibilidad_dados()
        assert exito == True
        assert cacho.dados_visibles == True
        assert cacho.mostrar_dados_activado == True

        # Segunda activación debería fallar
        exito2, mensaje2 = cacho.visibilidad_dados()
        assert exito2 == False
        assert "Ya usaste esta función anteriormente" in mensaje2


