class Calculator:
    def __init__(self, peso, altura):
        self._peso = peso
        self._altura = altura
        

class CalculatorIMC(Calculator):
    def __init__(self, peso, altura):
        super().__init__(peso, altura)
    
    @property
    def imc(self):
        indice_massa_corporal = round(self._peso / (self._altura / 100) ** 2, 2)
        return indice_massa_corporal
    
class CalculatorTMB(Calculator):
    def __init__(self, peso, altura, genero, idade):
        super().__init__(peso, altura)
        self._genero = genero
        self._idade = idade
    
    @property
    def tmb(self):
        genero_limpo = self._genero.lower().strip()
        if genero_limpo in ['m', 'masculino']:
            taxa_metabolica_basal = round(66.5 + (13.75 * self._peso) + (5.003 * self._altura) - (6.75 * self._idade), 2)
            return taxa_metabolica_basal
        elif genero_limpo in ['f', 'feminino']:
            taxa_metabolica_basal = round(655.1 + (9.563 * self._peso) + (1.850 * self._altura) - (4.676 * self._idade), 2)
            return taxa_metabolica_basal
        else:
            raise ValueError(f"Gênero '{self._genero}' inválido. Use 'Masculino' ou 'Feminino'.")