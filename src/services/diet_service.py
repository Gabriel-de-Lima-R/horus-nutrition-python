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

