def msg():
    print('-'*20)
    print('Função em PYTHON')
    print('-'*20)

msg()

def soma(n1,n2):
    #sum = n1+n2
    #print(f"A soma dos valores é: {sum}")
    return n1+n2
#soma(1,2)
resultado = soma(5,6)
print(f"A soma dos valores é: {resultado}")

def teste(x,y):
    return x+y
resultado = teste(int(input('Digite o primeiro valor: ')),int(input('Digite o segundo valor: ')))
print(f"A soma dos valores é: {resultado}")