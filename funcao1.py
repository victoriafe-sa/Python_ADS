def msg():
    print('-'*20)
    print('Função em PYTHON')
    print('-'*20)

msg()

def s(n1,n2):
    #sum = n1+n2
    #print(f"A soma dos valores é: {sum}")
   return n1+n2
#s(1,2)
resultado = s(5,6)
print(f"A soma dos valores é: {resultado}")
print('-'*30)

def operacoes(x,y):
    soma = x+y
    sub = x-y
    mult = x*y
    div = x/y
    #return soma, sub, mult, div
    print(f"A soma dos valores é: {soma}")
    print(f"A soma dos valores é: {sub}")
    print(f"A soma dos valores é: {mult}")
    print(f"A soma dos valores é: {div}")
#soma, sub, mult, div = operacoes(int(input('Digite o primeiro valor: ')),int(input('Digite o segundo valor: ')))
operacoes(int(input('Digite o primeiro valor: ')),int(input('Digite o segundo valor: ')))

print('-'*30)

