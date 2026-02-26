# 🥗 Horus Nutrition - CLI

> Um assistente de dietas personalizadas diretamente no seu terminal! 🚀

## 📋 Sobre o Projeto

O **Horus Nutrition** é uma aplicação de linha de comando (CLI) desenvolvida em Python que permite aos usuários criar contas, receber dietas personalizadas baseadas em seus objetivos e acompanhar suas métricas de saúde como IMC e TMB.

O sistema foi desenvolvido seguindo boas práticas de programação, com foco em organização, testabilidade e experiência do usuário mesmo em ambiente de terminal.

É importante ressaltar que este é um projeto **amador**, criado exclusivamente para praticar meus conhecimentos em Python. Sei que existem muitas melhorias para serem feitas, e agradeço a compreensão de todos. Também aceito melhorias, então se sinta a vontade! 🤝

## 🎯 Funcionalidades

- **Gerenciamento de Contas**
  - Criação de conta com validação de e-mail e senha (mín. 8 caracteres, 1 maiúscula)
  - Persistência de dados em arquivo JSON

- **Jornada de Primeiro Acesso**
  - Coleta de dados pessoais (nome, idade, gênero, altura, peso)
  - Definição de objetivo (emagrecer, manter forma, ganhar massa)
  - Cálculo automático de IMC e TMB

- **Dashboard Personalizado**
  - Visualização do IMC atual com classificação
  - Cálculo de metas calóricas baseadas no objetivo
  - Gerenciamento de dietas

- **Sistema de Dietas**
  - Dietas pré-configuradas (1000 a 5000 kcal)
  - Dietas organizadas por objetivo
  - 4 refeições diárias com alimentos detalhados

- **Configurações**
  - Edição de dados pessoais com recálculo automático
  - Alteração de senha
  - Exclusão de conta com confirmação

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+** - Linguagem principal
- **Pytest** - Testes unitários
- **JSON** - Persistência de dados

## 📁 Estrutura do Projeto
HORUS NUTRITION
│
├── data/
│   ├── diets_db.json          # arquivo com as dietas pré-configuradas
│   └── usuarios_db.json       # arquivo com as informações de todos os usuários ativos
│
├── src/
│   ├── __init__.py
│   ├── main.py                 # ponto de entrada do sistema
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── auth.py             # autenticação (cadastro e login)
│   │   ├── calculator.py       # cálculos de IMC, TMB e metas calóricas
│   │   ├── diet_service.py     # lógica para buscar e atribuir dietas
│   │   └── user_service.py     # gerenciamento de dados do usuário
│   │
│   └── view/
│       ├── __init__.py
│       ├── artes.py            # logos e artes ASCII do sistema
│       └── menus.py            # todas as telas e menus do CLI
│
├── tests/
│   ├── __init__.py
│   ├── test_autenticacao.py    # testes de cadastro e login
│   ├── test_calculos.py        # testes de IMC e TMB
│   ├── test_servico_diet.py    # testes de busca de dietas
│   └── test_servico_usuario.py # testes de atualização e exclusão
│
├── README.md                    # documentação do projeto
├── requirements.txt             # dependências 
├── regras_de_negocio.txt        # documento com as regras de negócio do projeto (RN01 a RN12)
└── .gitignore                   # arquivos ignorados

## 🚀 Como Executar o Projeto

### Pré-requisitos

- Python 3.8 ou superior instalado
- Git (opcional, para clonar o repositório)

### Passo a Passo

1. **Clone o repositório** (ou baixe os arquivos)
```bash
git clone https://github.com/Gabriel-de-Lima-R/horus-nutrition-python.git
cd horus-nutrition-python
```

2. **Crie e ative o ambiente virtual**
```bash
# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate

# Windows
python -m venv .venv
.venv\Scripts\activate
```

3. **Instale as dependências**
```bash
pip install -r requirements.txt
```

4. **Execute o sistema**
```bash
python main.py
```

---

## Tela Inicial

Ao executar o programa, você verá o menu principal:

```
 _   _ ___________ _   _ _____   _   _ _   _ ___________ _____ _____ _____ _____ _   _ 
| | | |  _  | ___ \ | | /  ___| | \ | | | | |_   _| ___ \_   _|_   _|_   _|  _  | \ | |
| |_| | | | | |_/ / | | \ `--.  |  \| | | | | | | | |_/ / | |   | |   | | | | | |  \| |
|  _  | | | |    /| | | |`--. \ | . ` | | | | | | |    /  | |   | |   | | | | | | . ` |
| | | \ \_/ / |\ \| |_| /\__/ / | |\  | |_| | | | | |\ \ _| |_  | |  _| |_\ \_/ / |\  |
\_| |_/\___/\_| \_|\___/\____/  \_| \_/\___/  \_/ \_| \_|\___/  \_/  \___/ \___/\_| \_/
======================================================================================

1. Criar Conta
2. Fazer Login
3. Fechar App
Escolha uma opção:
```

---

## 📊 Regras de Negócio Implementadas

| RN | Descrição | Status |
|----|-----------|--------|
| RN01 | Criação de conta com validação de e-mail e senha (mín. 8 caracteres, 1 maiúscula) | ✅ |
| RN02 | Login com validação de credenciais | ✅ |
| RN03 | Jornada de primeiro acesso após cadastro | ✅ |
| RN04 | Cálculo de IMC e TMB baseado nos dados | ✅ |
| RN05 | Tela inicial com IMC e calorias diárias | ✅ |
| RN06 | Geração de dieta com confirmação | ✅ |
| RN07 | Banco com 9 dietas pré-configuradas | ✅ |
| RN08 | Dietas divididas em 4 refeições diárias | ✅ |
| RN09 | Alimentos com quantidade e calorias | ✅ |
| RN10 | Botões de sair e configurações na home | ✅ |
| RN11 | Alteração de dados com recálculo automático | ✅ |
| RN12 | Exclusão de conta com confirmação | ✅ |

---

## 🧪 Testes

Para executar os testes unitários:

```bash
# Executar todos os testes
pytest

# Executar com mais detalhes
pytest -v

# Executar testes específicos
pytest tests/test_calculos.py
```

---

## ✍️ Autor

Feito com ❤️ e muito café por **[Seu Nome]** durante meus estudos de Python.

- GitHub: [@Gabriel-de-Lima-R]([https://github.com/seu-usuario](https://github.com/Gabriel-de-Lima-R))
- LinkedIn: [Gabriel de Lima]([https://linkedin.com/in/seu-perfil](https://www.linkedin.com/in/gabriel-de-lima-rigonati-rocha/))

---

<div align="center">
  <sub>📚 Projeto amador desenvolvido para praticar Python</sub>
  <br>
  <sub>✨ "A melhor forma de aprender algo é praticando" ✨</sub>
</div>
