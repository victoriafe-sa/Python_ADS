def operacoes(x,y):
    soma = x+y
    sub = x-y
    mult = x*y
    div = x/y

    print(f"A soma dos valores é: {soma}")
    print(f"A subtração dos valores é: {sub}")
    print(f"A multiplicação dos valores é: {mult}")
    print(f"A divisão dos valores é: {div}")

operacoes(int(input('Digite o primeiro valor: ')),int(input('Digite o segundo valor: ')))