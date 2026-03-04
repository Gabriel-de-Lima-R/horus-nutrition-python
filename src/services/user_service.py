import json
import os
from .auth import Autenticacao
from .calculator import CalculatorIMC, CalculatorTMB
from .diet_service import DietService
from typing import Dict, Any, Optional


class UserService:
    def __init__(self) -> None:
        """Define o Caminho Absoluto"""
        self.db_path = Autenticacao.DB_PATH

    def _carregar_usuarios(self) -> dict[str, Any]:
        """Lê o arquivo JSON e retorna um dicionário."""
        try:
            with open(self.db_path, "r", encoding="utf-8") as arquivo:
                return json.load(arquivo)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def _salvar_usuarios(self, dados: dict[str, Any]) -> None:
        """Grava o dicionário de usuários no arquivo JSON."""
        with open(self.db_path, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, indent=4)

    def buscar_usuario(self, email: str) -> Optional[dict[str, Any]]:
        """Recupera os dados de um usuário específico pelo e-mail."""
        usuarios = self._carregar_usuarios()
        return usuarios.get(email)

    def salvar_perfil(self, email: str, dados_coletados: dict[str, Any]) -> bool:
        """Calcula IMC/TMB e atualiza o usuário no JSON"""

        # 01 - Carregar o arquivo atual
        usuarios = self._carregar_usuarios()

        # 02 - Realizar Calculos
        calculo_imc = CalculatorIMC(dados_coletados["peso"], dados_coletados["altura"])
        calculo_tmb = CalculatorTMB(
            dados_coletados["peso"],
            dados_coletados["altura"],
            dados_coletados["genero"],
            dados_coletados["idade"],
        )

        # 03 Calcula Meta e Define Objetivo
        meta_calorica, desc_objetivo = DietService().calcular_meta_calorica(
            calculo_tmb.tmb, dados_coletados["objetivo"]
        )

        # 04 - Atualizar dicionário
        usuarios[email].update(
            {
                "nome": dados_coletados["nome"],
                "idade": dados_coletados["idade"],
                "genero": dados_coletados["genero"],
                "altura": dados_coletados["altura"],
                "peso": dados_coletados["peso"],
                "objetivo": dados_coletados["objetivo"],
                "imc": calculo_imc.imc,
                "tmb": calculo_tmb.tmb,
                "primeiro_acesso": False,
                "meta_calorica": meta_calorica,
                "desc_objetivo": desc_objetivo,
            }
        )

        self._salvar_usuarios(usuarios)
        return True

    def salvar_dieta(self, email: str, dieta_escolhida: dict[str, Any]) -> bool:
        """Vincula uma dieta específica ao perfil do usuário."""
        # 01 - Carregar o arquivo atual
        usuarios = self._carregar_usuarios()

        # 02 - Verifica se o usuário existe
        if email in usuarios:

            # 03 - Atualiza o campo dieta
            usuarios[email].update({"dieta": dieta_escolhida})
            self._salvar_usuarios(usuarios)
            return True

        return False

    def atualizar_perfil(self, email: str, alteracoes: dict[str, Any]) -> bool:
        """Aplica alterações parciais no dicionário do usuário."""
        usuarios = self._carregar_usuarios()
        if email in usuarios:
            usuarios[email].update(alteracoes)
            self._salvar_usuarios(usuarios)
            return True
        return False

    def deletar_usuario(self, email: str) -> bool:
        """Remove permanentemente um usuário da base de dados."""
        usuarios = self._carregar_usuarios()

        if email in usuarios:
            del usuarios[email]
            self._salvar_usuarios(usuarios)
            return True

        return False
