#Lista 4 - Exercício 7

n = int(input('Informe uma operação para ser feita na calculadora: \n(Digite 1 para SOMA)\n(Digite 2 para SUBTRAÇÃO)\n(Digite 3 para MULTIPLICAÇÃO)\n(Digite 4 para DIVISÃO)\n(Digite 5 para SAIR): '))
while n<1 or n>5:
    n = int(input('Informe uma operação para ser feita na calculadora: \n(Digite 1 para SOMA)\n(Digite 2 para SUBTRAÇÃO)\n(Digite 3 para MULTIPLICAÇÃO)\n(Digite 4 para DIVISÃO)\n(Digite 5 para SAIR): '))
if n<2:
    a = float(input('Informe o primeiro valor: '))
    b = float(input('Informe o segundo valor: '))
    print(f'A soma de {a, b} é {a + b}')
elif n<3:
    a = float(input('Informe o primeiro valor: '))
    b = float(input('Informe o segundo valor: '))
    print(f'A subtração de {a, b} é {a - b}')
elif n< 4:
    a = float(input('Informe o primeiro valor: '))
    b = float(input('Informe o segundo valor: '))
    print(f'A multiplicação de {a, b} é {a * b}')
elif n<5:
    a = float(input('Informe o primeiro valor: '))
    b = float(input('Informe o segundo valor: '))
    print(f'A divisão de {a, b} é {a / b}')
else:
    exit
