def jornada_primeiro_acesso(email_usuario):
    print("\n" + "="*40)
    print("Seja Bem-Vindo(a) ao Horus Nutrition")
    print("Precisamos de alguns dados para calcular seu plano!")
    print("="*40 + "\n")
    nome_completo = input("Qual o seu nome completo: ").strip()
    idade = int(input("Quantos anos você tem: "))
    genero = input("Qual seu gênero (M / F): ").strip().upper()
    altura = float(input("Qual a sua altura atual em cm (ex: 175): "))
    peso = float(input("Qual o seu peso atual em kg (ex: 70.8): "))
    print("\nObjetivos: [1] Emagrecer | [2] Manter | [3] Ganhar Massa")
    objetivo = input("Escolha o número do seu objetivo: ")

    print(f"\nObrigado, {nome_completo}! Estamos calculando seu IMC e TMB...")

    return {
        "nome": nome_completo,
        "idade": idade,
        "genero": genero,
        "altura": altura,
        "peso": peso,
        "objetivo": objetivo
    }