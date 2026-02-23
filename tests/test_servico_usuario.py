import pytest
import json
import os
from src.services import UserService, Autenticacao


class TestUserService:

    @pytest.fixture(autouse=True)
    def setup_db(self):
        """Prepara um banco com um usuário pré-existente para testar a atualização."""
        dados_iniciais = {
            "teste@horus.com": {"senha": "SenhaForte123", "primeiro_acesso": True}
        }
        with open(Autenticacao.DB_PATH, "w", encoding="utf-8") as arquivo:
            json.dump(dados_iniciais, arquivo)
        yield

    def test_salvar_perfil_com_sucesso(self):
        # GIVEN
        email = "teste@horus.com"
        dados_jornada = {
            "nome": "Fernando Tester",
            "idade": 30,
            "genero": "M",
            "altura": 180,
            "peso": 80,
            "objetivo": "1",  # => Emagrecer
        }
        servico = UserService()

        # WHEN
        resultado = servico.salvar_perfil(email, dados_jornada)

        # THEN
        with open(Autenticacao.DB_PATH, "r") as arquivo:
            db = json.load(arquivo)

        usuario_atualizado = db[email]

        assert resultado is True
        assert usuario_atualizado["primeiro_acesso"] is False
        assert usuario_atualizado["nome"] == "Fernando Tester"
        assert "imc" in usuario_atualizado
        assert "tmb" in usuario_atualizado
        assert usuario_atualizado["imc"] > 0

    def test_erro_usuario_inexistente(self):
        # GIVEN
        email_nao_cadastrado = "erro@horus.com"
        dados = {
            "nome": "Ninguém",
            "idade": 20,
            "genero": "F",
            "altura": 160,
            "peso": 50,
            "objetivo": "2",
        }
        service = UserService()

        # WHEN / THEN
        # Deverá dar KeyError
        with pytest.raises(KeyError):
            service.salvar_perfil(email_nao_cadastrado, dados)
