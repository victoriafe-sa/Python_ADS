print('VENDA E DESCONTO')
print('-'*30)

valor = float(input('Digite o valor de venda de um produto: '))

desc = valor - (valor*0.15)

print(f'O valor do produto com 15% de desconto é R${desc:.2f}')