from services import CalculatorIMC

def main():
    imc = CalculatorIMC(70, 180).imc
    print('Hello Horus Nutrition!')
    print(imc)

if __name__ == '__main__':
    main()