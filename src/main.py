import json
import os
from services import CalculatorIMC, Autenticacao
from view import HORUS_NUTRITION_LOGO as logo

def limpar_banco_de_usuarios():
    """Reseta o banco usuarios_db"""
    try:
        with open(Autenticacao.DB_PATH, 'w', encoding='utf-8') as arquivo:
            banco_vazio = {}
            json.dump(banco_vazio, arquivo)
        print("Bando de dados (JSON) limpo com sucesso!")
    except Exception as erro:
        print(f'Erro ao limpar o arquivo JSON: {erro}')

def menu_principal():
    while True:
        print(logo)
        print("=" * 28, '\n')
        print("1. Criar Conta")
        print("2. Fazer Login")
        print("3. Sair")

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
                print("Encaminhando para o sistema...")
                break
                # Entra a jornada primeiro acesso ou jornada menu principal
            input()

        elif opcao == "3":
            print("Encerrando...")
            break

        else:
            print("Opção inválida.")
            input()



def main():
    limpar_banco_de_usuarios()
    menu_principal()

if __name__ == '__main__':
    main()