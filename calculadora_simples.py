# Num1, Num2, Op, Result
num1 = int(input('Digite o primeiro número: ')) # Ler o primeiro número com float
op   = str(input('Digite a operação matemática a ser feita: '))
num2 = int(input('Digite o segundo número: '))


def calculadora():
    if op == '+':
     print(num1 + num2)
    if op == '-':
     print(num1 - num2)
    if op == '/':
     print(num1 / num2)
    if op == '*':
     print(num1 * num2)
    else: #se nenhuma das acima for verdadeira 
     print('Operação não reconhecida! ')
calculadora()