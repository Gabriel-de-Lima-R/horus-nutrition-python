import json
import os
from services import Autenticacao


class DietService:
    def __init__(self):
        self.BASE_DIR = Autenticacao.BASE_DIR
        self.DB_DIETAS = os.path.join(self.BASE_DIR, "data", "dietas_db.json")

    def _carregar_dietas(self):
        """Lê o arquivo dietas_db.json usando o caminho absoluto corrigido."""

        try:
            with open(self.DB_DIETAS, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
                return dados.get("dietas", [])
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def calcular_meta_calorica(self, tmb, objetivo):
        """Lógica de meta baseada no objetivo."""
        meta_calorica = tmb * 1.4
        if objetivo == "1": 
            meta_calorica -= 500
            desc_objetivo = "Emagrecimento (Déficit) 🔥"
        elif objetivo == "3": 
            meta_calorica += 500
            desc_objetivo = "Ganho de Massa (Superávit) 💪"
        else:
             desc_objetivo = "Manter Peso ⚖️"

        return meta_calorica, desc_objetivo

    def buscar_dieta_ideal(self, meta_calorica, objetivo_usuario):
        dietas = self._carregar_dietas()

        if not dietas:
            return None
        
        dieta_escolhida = dietas[0]
        menor_diferenca = abs(meta_calorica - dietas[0]["calorias_totais"])

        for i in range(1, len(dietas)):
            calorias_atual = dietas[i]["calorias_totais"]
            diferenca = abs(meta_calorica - calorias_atual)

            if diferenca < menor_diferenca:
                menor_diferenca = diferenca
                dieta_escolhida = dietas[i]

            elif diferenca == menor_diferenca:
            # Desempate para Ganho de Massa (3): prefere a maior
                if objetivo_usuario == "3":
                    if calorias_atual > dieta_escolhida["calorias_totais"]:
                        dieta_escolhida = dietas[i]
                # Desempate para Emagrecer/Manter: prefere a menor
                else:
                    if calorias_atual < dieta_escolhida["calorias_totais"]:
                        dieta_escolhida = dietas[i]
            
        return dieta_escolhida
        
        