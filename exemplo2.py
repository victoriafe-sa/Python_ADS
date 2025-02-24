print('Programa para calcular media')
print('-'*40)

nome=input('Digite o nome do aluno: ')
n1= float(input('Digite a primeira nota: '))
n2= float(input('Digite a segundaa nota: '))
n3= float(input('Digite a terceira nota: '))

m = (n1+n2+n3)/3

if m>=6:
    print(f'O aluno {nome} está aprovado com média {m}')
elif 2 <= m < 6:
    print(f'O aluno {nome} está de recuperação com média {m}')
else:
    print(f'O aluno {nome} está reprovado com média {m}')

'''print(f'A media do aluno {nome} é {m:.2f}')'''