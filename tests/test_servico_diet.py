import pytest
from src.services.diet_service import DietService


class TestDietService:

    def test_deve_encontrar_dieta_mais_proxima_da_meta(self):
        # GIVEN: Uma meta de 1500 kcal
        meta_calorica = 1500
        objetivo = "1"  # Emagrecer
        servico = DietService()

        # WHEN: Buscamos a dieta
        dieta_escolhida = servico.buscar_dieta_ideal(meta_calorica, objetivo)

        # THEN: Como no seu JSON a dieta é 1510, verificamos se ele trouxe a correta
        assert dieta_escolhida is not None
        assert dieta_escolhida["calorias_totais"] == 1510
        assert "Dieta Moderada" in dieta_escolhida["nome"]

    def test_deve_encontrar_dieta_mais_proxima_para_ganho_massa(self):
        # GIVEN: Uma meta de 3000 kcal
        meta_calorica = 3000
        objetivo = "3"  # Ganho de Massa
        servico = DietService()

        # WHEN: Buscamos a dieta
        resultado = servico.buscar_dieta_ideal(meta_calorica, objetivo)

        # THEN: Verificamos se trouxe a Hardcore de 3000 (ou a mais próxima do seu JSON)
        assert resultado is not None
        assert "Dieta Hardcore" in resultado["nome"]
        # Se no seu JSON for exatamente 3000:
        # assert resultado["calorias_totais"] == 3000

    def test_calculo_meta_calorica_emagrecimento(self):
        # GIVEN: Uma TMB de 2000
        tmb = 2000
        objetivo = "1"  # Emagrecer
        servico = DietService()

        # WHEN: Calculamos a meta (TMB * 1.4 - 500)
        # 2000 * 1.4 = 2800 -> 2800 - 500 = 2300
        meta, desc = servico.calcular_meta_calorica(tmb, objetivo)

        # THEN
        assert meta == 2300
        assert "Emagrecimento" in desc
