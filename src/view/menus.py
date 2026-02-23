def coleta_nome():
     while True:
        nome_completo = input("Qual o seu nome completo: ").strip()
        if len(nome_completo) >= 2:
            return nome_completo
        print("Tente Novamente. Precisa ser o nome completo!\n")

def coleta_idade():
    while True:
        try:
            idade = int(input("Quantos anos você tem: "))
            if 0 < idade < 120:
                return idade
            print("Tente Novamente. Você precisa ter entre 1 a 119 anos!\n")
        except:
            print("Precisa ser um número válido!\n")

def coleta_genero():
    while True:
        genero = input("Qual seu gênero (M / F): ").strip().upper()
        if genero in ["M", "F", "MASCULINO", "FEMININO"]:
            return genero
        print("Tente Novamente. Você precisa digitar M ou F!\n")

def coleta_altura():
    while True:
        try:
            altura = float(input("Qual a sua altura atual em cm (ex: 175): ").replace(".", ""))
            if 50 < altura < 300:
                return altura
            print("Tente Novamente. Você precisa ter entre 50 a 300 cm de altura!\n")
        except:
            print("Precisa ser um número válido (ex: 175)!\n")

def coleta_peso():
    while True:
        try:
            peso = float(input("Qual o seu peso atual em kg (ex: 70.8): ").replace(",", "."))
            if 0 < peso < 300:
                return peso
            print("Tente Novamente. Você precisa ter entre 0 a 300 kg de peso!\n")
        except:
            print("Precisa ser um número válido (ex: 70.5)!\n")

def coleta_objetivo():
    while True:
        print("\nObjetivos: [1] Emagrecer | [2] Manter | [3] Ganhar Massa")
        objetivo = input("Escolha o número do seu objetivo: ").strip()
        if objetivo in ["1", "2", "3"]:
            return objetivo
        print("Escolha uma opção válida!\n")

def jornada_primeiro_acesso(email_usuario):
    print("\n" + "="*40)
    print("Seja Bem-Vindo(a) ao Horus Nutrition")
    print("Precisamos de alguns dados para calcular seu plano!")
    print("="*40 + "\n")

    nome_completo = coleta_nome()
    idade = coleta_idade()
    genero = coleta_genero()
    altura = coleta_altura()
    peso = coleta_peso()
    objetivo = coleta_objetivo()

    print(f"\nObrigado, {nome_completo}! Estamos calculando seu IMC e TMB...")

    return {
        "nome": nome_completo,
        "idade": idade,
        "genero": genero,
        "altura": altura,
        "peso": peso,
        "objetivo": objetivo
    }