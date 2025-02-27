from operacoes import soma, subtracao, multiplicacao, divisao
from utils import exibir_resultado

def main():
    operacoes = {
        '+': soma,
        '-': subtracao,
        '*': multiplicacao,
        '/': divisao
    }

    operacao = input("Escolha uma operação (+, -, *, /): ")
    if operacao not in operacoes:
        print("Operação inválida")
        return

    try:
        a = float(input("Insira o primeiro número: "))
        b = float(input("Insira o segundo número: "))
    except ValueError:
        print("Entrada inválida. Por favor, insira números válidos.")
        return

    resultado = operacoes[operacao](a, b)
    exibir_resultado(operacao, resultado)

if __name__ == "__main__":
    main()
