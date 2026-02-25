import json
import os
from services import CalculatorIMC, Autenticacao, UserService
from view import HORUS_NUTRITION_LOGO as logo
from view import jornada_primeiro_acesso, menu_home, menu_mostra_dieta, menu_gerar_dieta

def limpar_banco_de_usuarios():
    """Reseta o banco usuarios_db"""
    try:
        with open(Autenticacao.DB_PATH, 'w', encoding='utf-8') as arquivo:
            banco_vazio = {}
            json.dump(banco_vazio, arquivo)
        print("Bando de dados (JSON) limpo com sucesso!")
    except Exception as erro:
        print(f'Erro ao limpar o arquivo JSON: {erro}')

def menu_login():
    while True:
        print(logo)
        print("=" * 86, '\n')
        print("1. Criar Conta")
        print("2. Fazer Login")
        print("3. Fechar App")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            email = input("Digite seu e-mail: ").strip()
            senha = input("Digite sua senha (mín. 8 caracteres e 1 maiúscula): ").strip()
            usuario = Autenticacao(email, senha)
            usuario.criar_conta()
            input()

        elif opcao == "2":
            email = input("E-mail: ").strip()
            senha = input("Senha: ").strip()
            usuario = Autenticacao(email, senha)
            if usuario.fazer_login():
                servico = UserService()

                if usuario.primeiro_acesso:
                    dados = jornada_primeiro_acesso(usuario._email)
                    if servico.salvar_perfil(email, dados):
                        print("Perfil Configurado com Sucesso".upper())
                        input()
                while True:
                    dados_atuais = servico.buscar_usuario(email)
                    opcao_escolhida_da_home = menu_home(dados_atuais) # mostra as informações da home e retorna a opção escolhida da home
                    if opcao_escolhida_da_home == "1":
                        menu_mostra_dieta(dados_atuais)
                    elif opcao_escolhida_da_home == "2":
                        menu_gerar_dieta(dados_atuais)
                    elif opcao_escolhida_da_home == "4":
                        print("Encerrando sessão...")
                        break
            input()

        elif opcao == "3":
            print("Encerrando...")
            break

        else:
            print("Opção inválida.")
            input()



def main():
    # limpar_banco_de_usuarios()
    menu_login()

if __name__ == '__main__':
    main()