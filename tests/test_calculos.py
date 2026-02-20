import pytest
from src.services import CalculatorIMC, CalculatorTMB

class TestCalculo:
    def test_calculo_imc(self):
        # Given
        entrada_peso = 45
        entrada_altura = 150
        imc_esperado = 20
        calculator_test = CalculatorIMC(entrada_peso, entrada_altura)

        resultado = calculator_test.imc # When

        assert resultado == imc_esperado # Then

    def test_tmb_calculo_masculino(self):
        # Given
        entrada_peso = 80
        entrada_altura = 180
        entrada_genero = 'M'
        entrada_idade = 30
        esperado_tmb = 1864.54
        calculator_test = CalculatorTMB(entrada_peso, entrada_altura, entrada_genero, entrada_idade)
        
        resultado = calculator_test.tmb # When

        assert resultado == esperado_tmb # Then

    def test_tmb_calculo_feminino(self):
        # Given
        entrada_peso = 60
        entrada_altura = 165
        entrada_genero = 'F'
        entrada_idade = 25
        esperado_tmb = 1417.23
        calculator_test = CalculatorTMB(entrada_peso, entrada_altura, entrada_genero, entrada_idade)
        
        resultado = calculator_test.tmb # When

        assert resultado == esperado_tmb # Then
    
    def test_tmb_genero_invalido(self):
        calculator_test = CalculatorTMB(peso=80, altura=180, genero='invalido', idade=20)
        with pytest.raises(ValueError):

            resultado = calculator_test.tmb
            # Se houver uma falha ao criar a váriavel resultado, logo, o teste passa