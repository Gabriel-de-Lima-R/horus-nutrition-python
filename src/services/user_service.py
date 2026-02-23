import json
import os
from services import Autenticacao, CalculatorIMC, CalculatorTMB

class UserService:
    def __init__(self):
        self.db_path = Autenticacao.DB_PATH
    
    def _carregar_usuarios(self):
        """Lê o arquivo JSON e retorna um dicionário."""
        try:
            with open(self.db_path, 'r', encoding='utf-8') as arquivo:
                return json.load(arquivo)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}
    
    def _salvar_usuarios(self, dados):
        """Grava o dicionário de usuários no arquivo JSON."""
        with open(self.db_path, 'w', encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, indent=4)
    
    def salvar_perfil(self, email, dados_coletados):
        """Calcula IMC/TMB e atualiza o usuário no JSON"""

        #01 - Carregar o arquivo atual
        usuarios = self._carregar_usuarios()

        #02 - Realizar Calculos
        calculo_imc = CalculatorIMC(dados_coletados["peso"], dados_coletados["altura"])
        calculo_tmb = CalculatorTMB(
            dados_coletados["peso"], 
            dados_coletados["altura"], 
            dados_coletados["genero"], 
            dados_coletados["idade"]
        )

        #03 - Atualizar dicionário
        usuarios[email].update({
            "nome": dados_coletados['nome'],
            "idade": dados_coletados['idade'],
            "genero": dados_coletados['genero'],
            "altura": dados_coletados['altura'],
            "peso": dados_coletados['peso'],
            "objetivo": dados_coletados['objetivo'],
            "imc": calculo_imc.imc,
            "tmb": calculo_tmb.tmb,
            "primeiro_acesso": False
        })

        self._salvar_usuarios(usuarios)
        return True

