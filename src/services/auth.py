import json
import os

class Autenticacao:
    # Caminho absoluto para evitar erros de diretório
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    DB_PATH = os.path.join(BASE_DIR, 'data', 'usuarios_db.json')

    def _carregar_usuarios(self):
        """Lê o arquivo JSON e retorna um dicionário."""
        try:
            with open(self.DB_PATH, 'r', encoding='utf-8') as arquivo:
                return json.load(arquivo)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def _salvar_usuarios(self, usuarios):
        """Grava o dicionário de usuários no arquivo JSON."""
        with open(self.DB_PATH, 'w', encoding='utf-8') as arquivo:
            json.dump(usuarios, arquivo, indent=4)

    def __init__(self, email, senha):
        self._email = email
        self._senha = senha

    def valida_email(self, usuarios):
        return self._email not in usuarios
    
    def valida_senha(self):
        tem_oito_caracteres = len(self._senha) >= 8
        tem_letra_maiuscula = any(caracter.isupper() for caracter in self._senha)
        return tem_oito_caracteres and tem_letra_maiuscula

    def criar_conta(self):
        usuarios_db = self._carregar_usuarios()

        if not self.valida_email(usuarios_db):
            print("Já existe uma conta com esse e-mail.")
            return False
        
        if not self.valida_senha():
            print("A senha deve conter no mínimo 8 caracteres e pelo menos uma letra maiúscula.")
            return False

        print("Conta criada com sucesso!")
        usuarios_db[self._email] = {
            "senha": self._senha,
            "primeiro_acesso": True
        }
        self._salvar_usuarios(usuarios_db)
        return True
    
    def fazer_login(self):
        usuarios_db = self._carregar_usuarios()

        if self._email in usuarios_db and usuarios_db[self._email]["senha"] == self._senha:
            print("Login realizado com sucesso!")
            return True
        else:
            print("E-mail ou senha inválidos. Tente novamente.")
            return False

    def __str__(self):
        return f'Credenciais do usuário: e-mail "{self._email}" | senha "{self._senha}" '

    