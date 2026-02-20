class CalculatorIMC:
    def __init__(self, peso, altura):
        self._peso = peso
        self._altura = altura
    
    @property
    def imc(self):
        indice_massa_corporal = round(self._peso / (self._altura / 100) ** 2, 2)
        return indice_massa_corporal