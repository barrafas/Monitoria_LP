"""Documentação de linha única do módulo"""

import sys
 
sys.path.insert(0, "../src")

import modulo_qualidade as mq
import unittest
from unittest.mock import Mock
from datetime import date

def setUpModule():
    print("Running setUpModule")


def tearDownModule():
    print("Running tearDownModule")

class TestModuloQualidade(unittest.TestCase):

    #Fixtures
    @classmethod
    def setUpClass(cls):
        print("Executando setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("Executando tearDownClass")
  
    def setUp(self):
        print("Executando setUp method")

    def tearDown(self):
        print("Executando tearDown method")

    def test_skip_exemplo(self):
        self.skipTest("Teste em Desenvolvimento")

    @unittest.skip("Este teste ainda não foi finalizado.")
    def test_case_decimais_grandes_negativo_negativo(self):
        pass

    def test_case_inteiros_positivo_positivo(self):
        print("Executando Caso de Teste: Inteiros - Positivo - Positivo")
        self.assertEqual(mq.funcao_mais_simples_do_mundo(1, 1), 2)

    def test_case_inteiros_negativo_negativo(self):
        print("Executando Caso de Teste: Inteiros - Negativo - Negativo")
        self.assertEqual(mq.funcao_mais_simples_do_mundo(-1, -1), -2)

    def test_case_decimais_positivo_positivo(self):
        print("Executando Caso de Teste: Decimais - Positivo - Positivo")
        self.assertAlmostEqual(mq.funcao_mais_simples_do_mundo(1.0, 1.0), 2.0, 10)

    def test_case_decimais_negativo_negativo(self):
        print("Executando Caso de Teste: Decimais - Negativo - Negativo")
        self.assertAlmostEqual(mq.funcao_mais_simples_do_mundo(-1.0, -1.0), -2.0, 10)

    @unittest.skipIf(date.today().day % 2 != 0, "Executar apenas em dias pares!")
    def test_case_dias_pares(self):
        print("Executando Caso de Teste: Dias Pares")
        self.assertEqual(mq.funcao_mais_simples_do_mundo(1, 1), 2)

    @unittest.skipIf(date.today().day % 2 == 0, "Executar apenas em dias ímpares!")
    def test_case_dias_impares(self):
        print("Executando Caso de Teste: Dias Ímpares")
        self.assertEqual(mq.funcao_mais_simples_do_mundo(1, 1), 2)

    #Entendendo o uso de Mocks
    def test_case_alarme_fulgor_verdadeiro(self):
        print("Executando Caso de Teste: Alarme - Fulgor - Verdadeiro")
        mq.ler_temperatura = Mock()
        mq.ler_temperatura.return_value = 50
        print(mq.ler_temperatura())
        self.assertTrue(mq.alerta_ponto_fulgor())

    #Entendendo o uso de Mocks
    def test_case_alarme_fulgor_falso(self):
        print("Executando Caso de Teste: Alarme - Fulgor - Falso")
        mq.ler_temperatura = Mock()
        mq.ler_temperatura.return_value = 8
        print(mq.ler_temperatura())
        self.assertFalse(mq.alerta_ponto_fulgor())

if __name__ == "__main__":
    unittest.main(verbosity=2)