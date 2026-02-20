import json
from services import CalculatorIMC, Autenticacao

def limpar_banco_de_usuarios():
    """Reseta o banco usuarios_db"""
    try:
        with open(Autenticacao.DB_PATH, 'w', encoding='utf-8') as arquivo:
            banco_vazio = {}
            json.dump(banco_vazio, arquivo)
        print("Bando de dados (JSON) limpo com sucesso!")
    except Exception as erro:
        print(f'Erro ao limpar o arquivo JSON: {erro}')

def main():
    limpar_banco_de_usuarios()
    print('Hello Horus Nutrition!')

if __name__ == '__main__':
    main()