from services import CalculatorIMC, Autenticacao
import os

def main_auth():
    print("=== TESTE DE PERSISTÊNCIA (JSON) ===")
    
    # Dados de teste
    email_teste = "admin@horus.com"
    senha_teste = "Admin123"

    # 1. Instanciar
    auth = Autenticacao(email_teste, senha_teste)

    # 2. Tentar criar conta
    print(f"Tentando criar conta para: {email_teste}")
    criou = auth.criar_conta()

    if criou:
        print("Sucesso: Dados gravados no arquivo JSON.")
    else:
        print("Aviso: Conta já existia ou falhou (o que é esperado se rodar 2x).")

    # 3. Tentar login (lendo do JSON recém gravado)
    print("\nTentando realizar login...")
    if auth.fazer_login():
        print("Sucesso: Login validado via leitura do JSON!")
    else:
        print("Erro: Não foi possível validar o login pelo JSON.")

    # 4. Verificar se o arquivo existe fisicamente
    if os.path.exists(Autenticacao.DB_PATH):
        print(f"\nConfirmação física: Arquivo encontrado em {Autenticacao.DB_PATH}")
    else:
        print("\nErro crítico: O arquivo JSON não foi criado!")

def main():
    print('Hello Horus Nutrition!')
    main_auth()

if __name__ == '__main__':
    main()