import pytest
import os
import json
from src.services import Autenticacao

class TestAutenticacao:
    @pytest.fixture(autouse=True)
    def setup_db(self):
        """Limpa o JSON antes de cada teste para garantir isolamento."""
        with open(Autenticacao.DB_PATH, 'w', encoding='utf-8') as f:
            json.dump({}, f)

    def test_criar_conta_valida(self):
        # Given
        email = "novo@horus.com"
        senha = "SenhaForte123"
        auth = Autenticacao(email, senha)

        # When
        resultado = auth.criar_conta()

        # Then
        assert resultado is True

    def test_erro_email_duplicado(self):
        # Given
        email = "repetido@horus.com"
        Autenticacao(email, "Senha12345").criar_conta()
        usuario_duplicado = Autenticacao(email, "OutraSenha123")

        # When
        resultado = usuario_duplicado.criar_conta()

        # Then
        assert resultado is False 

    def test_senha_fraca(self):
        # Given
        email = "senha@horus.com"
        senha_fraca = "sen123"
        usuario_fraco = Autenticacao(email, senha_fraca)

        #When
        resultado = usuario_fraco.criar_conta()

        # Then
        assert resultado is False 

    def test_fazer_login_corretamente(self):
        # Given
        email = "login@horus.com"
        senha = "SenhaValida"
        Autenticacao(email, senha).criar_conta()
        usuario_credenciado = Autenticacao(email, senha)

        # When
        resultado = usuario_credenciado.fazer_login()

        # Then
        assert resultado is True
    
    def test_login_incorreto(self):
        # Given
        email = "login@horus.com"
        senha = "SenhaValida"
        Autenticacao(email, senha).criar_conta()
        usuario_credenciado = Autenticacao(email, "SenhaIncorreta")

        # When
        resultado = usuario_credenciado.fazer_login()

        # Then
        assert resultado is False

    