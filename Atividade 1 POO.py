def questao1():
    def somar_tres_valores(val1, val2, val3):
        return val1 + val2 + val3

    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    num3 = int(input("Digite o terceiro número: "))
    resultado = somar_tres_valores(num1, num2, num3)
    print(f"A soma é: {resultado}")

def questao2():
    def calcular_area_retangulo(comprimento, largura):
        return comprimento * largura

    comp = float(input("Digite o comprimento do retângulo: "))
    larg = float(input("Digite a largura do retângulo: "))
    area = calcular_area_retangulo(comp, larg)
    print(f"A área do retângulo é: {area}")

def questao3():
    def valor_absoluto(numero):
        if numero < 0:
            return numero * -1
        else:
            return numero

    num = float(input("Digite um número para encontrar seu valor absoluto: "))
    resultado = valor_absoluto(num)
    print(f"O valor absoluto é: {resultado}")

def questao4():
    def somar(val1, val2):
        print(f"Resultado da soma: {val1 + val2}")

    def subtrair(val1, val2):
        print(f"Resultado da subtração: {val1 - val2}")

    def multiplicar(val1, val2):
        print(f"Resultado da multiplicação: {val1 * val2}")

    def dividir(val1, val2):
        if val2 != 0:
            print(f"Resultado da divisão: {val1 / val2}")
        else:
            print("Erro: Divisão por zero!")

    operador = input("Digite a operação (+, -, x, /): ")
    num1 = float(input("Digite o primeiro valor: "))
    num2 = float(input("Digite o segundo valor: "))

    if operador == '+':
        somar(num1, num2)
    elif operador == '-':
        subtrair(num1, num2)
    elif operador == 'x' or operador == '*':
        multiplicar(num1, num2)
    elif operador == '/':
        dividir(num1, num2)
    else:
        print("Operador inválido!")

def questao5():
    def calcular_media_turma():
        notas = []
        print("Digite as notas dos alunos (digite -1 para terminar):")
        while True:
            try:
                nota = float(input())
                if nota == -1:
                    break
                notas.append(nota)
            except ValueError:
                print("Entrada inválida. Por favor, digite um número ou -1 para sair.")

        if notas:
            media = sum(notas) / len(notas)
            print(f"Média aritmética da turma: {media:.2f}")
            print(f"Quantidade de alunos na turma: {len(notas)}")
        else:
            print("Nenhum aluno foi inserido.")

    calcular_media_turma()

def main_menu():
    while True:
        print("\nEscolha a questão para executar:")
        print("1 - Somar três valores")
        print("2 - Calcular área de retângulo")
        print("3 - Valor absoluto")
        print("4 - Calculadora de quatro operações")
        print("5 - Calcular média da turma")
        print("0 - Sair")

        escolha = input("Digite o número da questão: ")

        if escolha == '1':
            questao1()
        elif escolha == '2':
            questao2()
        elif escolha == '3':
            questao3()
        elif escolha == '4':
            questao4()
        elif escolha == '5':
            questao5()
        elif escolha == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main_menu()