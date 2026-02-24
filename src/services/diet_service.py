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
        manutencao = tmb * 1.4
        if objetivo == "1": return manutencao - 500
        if objetivo == "3": return manutencao + 500
        return manutencao
    
    