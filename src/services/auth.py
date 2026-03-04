import json
import os
from typing import Dict, Any


class Autenticacao:

    # Caminho absoluto para evitar erros de diretório
    BASE_DIR = os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    )
    # Caminho para chegar no arquivo usuarios_db.json
    DB_PATH = os.path.join(BASE_DIR, "data", "usuarios_db.json")

    def _carregar_usuarios(self) -> Dict[str, Any]:
        """Lê o arquivo JSON e retorna um dicionário."""
        try:
            with open(self.DB_PATH, "r", encoding="utf-8") as arquivo:
                return json.load(arquivo)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def _salvar_usuarios(self, usuarios: Dict[str, Any]) -> None:
        """Grava o dicionário de usuários no arquivo JSON."""
        with open(self.DB_PATH, "w", encoding="utf-8") as arquivo:
            json.dump(usuarios, arquivo, indent=4)

    def __init__(self, email: str, senha: str) -> None:
        """
        Inicializa uma instância de Autenticação.

        Args:
            email (str): E-mail fornecido pelo usuário.
            senha (str): Senha (deve seguir os critérios de validação do sistema).
        """
        self._email = email
        self._senha = senha

    def valida_email(self, usuarios: Dict[str, Any]) -> bool:
        """Verifica se o email já está cadastrado no banco de dados."""
        return self._email not in usuarios

    def valida_senha(self) -> bool:
        """
        Verifica se a senha atende aos requisitos mínimos de segurança.

        Requisitos:
            - Mínimo de 8 caracteres.
            - Ao menos uma letra maiúscula.
        """
        tem_oito_caracteres = len(self._senha) >= 8
        tem_letra_maiuscula = any(caracter.isupper() for caracter in self._senha)
        return tem_oito_caracteres and tem_letra_maiuscula

    def valida_arroba_email(self) -> bool:
        """Verifica a ausência do caractere '@' no e-mail."""
        return "@" not in self._email

    def criar_conta(self) -> bool:
        """
        Orquestra o processo de criação de uma nova conta de usuário.

        O processo consiste em:
        1. Carregar a base de dados atual.
        2. Validar se o e-mail já existe.
        3. Validar o formato básico do e-mail.
        4. Validar a força da senha.
        5. Persistir os novos dados se todas as etapas passarem.
        """
        usuarios_db = self._carregar_usuarios()

        if not self.valida_email(usuarios_db):
            print("Já existe uma conta com esse e-mail.")
            return False

        if self.valida_arroba_email():
            print("O e-mail precisa ser válido")
            return False

        if not self.valida_senha():
            print(
                "A senha deve conter no mínimo 8 caracteres e pelo menos uma letra maiúscula."
            )
            return False

        print("Conta criada com sucesso!")
        usuarios_db[self._email] = {"senha": self._senha, "primeiro_acesso": True}
        self._salvar_usuarios(usuarios_db)
        return True

    def fazer_login(self) -> bool:
        """Permite o login bem sucedido caso o e-mail e a senha estejam corretos"""
        usuarios_db = self._carregar_usuarios()

        if (
            self._email in usuarios_db
            and usuarios_db[self._email]["senha"] == self._senha
        ):
            print("Login realizado com sucesso!")
            return True
        else:
            print("E-mail ou senha inválidos. Tente novamente.")
            return False

    @property
    def primeiro_acesso(self) -> bool:
        """Lê o estado atual da flag 'primeiro_acesso' diretamente do banco de dados."""
        usuarios_db = self._carregar_usuarios()

        return usuarios_db[self._email]["primeiro_acesso"]

    def __str__(self) -> str:
        """Retorna uma representação amigável das credenciais (para fins de debug)."""
        return (
            f'Credenciais do usuário: e-mail "{self._email}" | senha "{self._senha}" '
        )
