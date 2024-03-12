# Faça uma função calculadora de dois números com três parâmetros:
# os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a operação a ser executada.
# Considera a seguinte definição:
# 1. Soma
# 2. Subtração
# 3. Multiplicação
# 4. Divisão
# Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.

v1 = float(input("Insita um valor para o cálculo: "))
v2 = float(input("Insira outro valor para o cálculo: "))
print("Operações disponiveis:\n1-Soma\t2-Subtração\n3-Multiplicação\t4-Divisão")
op = int(input("insira a operação desejada: "))

def Calculadora(valor1, valor2, operacao):
    if(operacao == 1):
        resultado = valor1 + valor2
        return resultado
    elif(operacao == 2):
        resultado = valor1 - valor2
        return resultado
    elif(operacao == 3):
        resultado = valor1 * valor2
        return resultado
    elif(operacao == 4):
        resultado = valor1 / valor2
        return resultado
    else:
        return 0

res = Calculadora(v1,v2,op)
if(res != 0):
    print("O resultado do cálculo entre", v1, " e ", v2, " é igual a ", res)
else:
    print("A operação informada não pode ser realizada")