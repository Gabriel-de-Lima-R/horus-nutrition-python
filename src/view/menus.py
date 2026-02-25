import os
from view import HORUS_NUTRITION_LOGO as logo
from services import DietService

def limpa_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

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

def classifica_imc(imc: float):
    if not imc:
        return "Não calculado" 
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso ideal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"

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
    primeiro_nome = nome_completo.split()[0]

    print(f"\nObrigado, {primeiro_nome}! Estamos calculando seu IMC e TMB...")

    return {
        "nome": nome_completo,
        "idade": idade,
        "genero": genero,
        "altura": altura,
        "peso": peso,
        "objetivo": objetivo
    }

def tem_dieta(dados):
    dieta = dados.get('dieta')
    return dieta is not None and len(dieta) > 0

def menu_home(dados_usuario_atual):
    limpa_terminal()

    print("╔" + "═" * 68 + "╗")
    print("║" + "🏠 PAINEL DO USUÁRIO".center(67) + "║")
    print("╚" + "═" * 68 + "╝")

    nome = dados_usuario_atual.get('nome')
    primeiro_nome = nome.split()[0]
    print(f"\n Olá, {primeiro_nome.title()}! 👋")
    print("─" * 70)

    imc = dados_usuario_atual.get('imc', 0)
    tmb = dados_usuario_atual.get('tmb', 0)
    meta_calorica = dados_usuario_atual.get('meta_calorica', 0)
    desc_objetivo = dados_usuario_atual.get('desc_objetivo', 'Não definido')

    classificacao = classifica_imc(imc)
    print(f" 📊 IMC = {imc:.1f}  →  {classificacao}".center(70))

    print("─" * 70)
    print(f" 🎯 Seu Objetivo: {desc_objetivo}")
    print("─" * 70)
    print(f" 🔥 Gasto Basal:     {tmb:6.0f} kcal")
    print(f" ⚡ Meta Diária:     {meta_calorica:6.0f} kcal")
    print("─" * 70)

    print("╔" + "═" * 45 + "╗")
    print("║" + "OPÇÕES".center(45) + "║")
    print("╠" + "═" * 45 + "╣")
    print("║  [1] VER MINHA DIETA".ljust(46) + "║")
    print("║  [2] GERAR DIETA".ljust(46) + "║")
    print("║  [3] CONFIGURAÇÕES".ljust(46) + "║")
    print("║  [4] SAIR".ljust(46) + "║")
    print("╚" + "═" * 45 + "╝")
    
    escolha = input("\nEscolha: ").strip()
    return escolha

def menu_mostra_dieta(dados_usuario_atual):
    limpa_terminal()
    
    if not tem_dieta(dados_usuario_atual):
        print("\n" + "!"*40)
        print("🔍 Você ainda não possui uma dieta.")
        print("Volte para a Tela Home para gerar uma!")
        print("!"*40)
        input("\nPressione Enter para voltar...")
        return False

    dieta_usuario = dados_usuario_atual.get('dieta')
    
    print("╔" + "═" * 68 + "╗")
    print("║" + f"🥗 {dieta_usuario['nome']}".center(67) + "║")
    print("╚" + "═" * 68 + "╝")

def menu_gerar_dieta(dados_usuario_atual):
    limpa_terminal()

    if tem_dieta(dados_usuario_atual):
        print("⚠️ Você já possui uma dieta ativa!")
        confirmacao = input("Deseja substituí-la por uma nova? (s/n): ").lower().strip()
        
        if confirmacao not in ['s', 'sim'] :
            print("\nOperação cancelada. Mantendo dieta atual...")
            input("Pressione Enter para voltar...")
            return False
    

        
