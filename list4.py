import random

# Gerar a matriz 4x4 com números aleatórios entre 10 e 100
matriz = [[random.randint(10, 100) for _ in range(4)] for _ in range(4)]

# Exibir a matriz gerada
print("Matriz 4x4 gerada:")
for linha in matriz:
    print(linha)

# Encontrar o maior e o menor valor na matriz
maior_valor = max(max(linha) for linha in matriz)
menor_valor = min(min(linha) for linha in matriz)

# Calcular a soma de todos os elementos da matriz
soma_matriz = sum(sum(linha) for linha in matriz)

print(f"\nMaior valor da matriz: {maior_valor}")
print(f"Menor valor da matriz: {menor_valor}")
print(f"Soma de todos os valores da matriz: {soma_matriz}")


import numpy as np 

# Gerar a matriz 4x4 com números aleatórios entre 10 e 100
matriz = np.random.randint(10, 100, size=[4, 4])

# Imprimir a matriz
for linha in matriz:
    print(linha)

# Inicializar as variáveis para o maior e menor valor
maior = matriz[0][0]
menor = matriz[0][0]

# Inicializar a soma
soma = 0

# Percorrer a matriz para calcular maior, menor e soma
for linha in matriz:
    for valor in linha:
        # Verificar o maior valor
        if valor > maior:
            maior = valor
        # Verificar o menor valor
        if valor < menor:
            menor = valor
        # Adicionar o valor à soma
        soma += valor

# Imprimir os resultados
print("Maior valor:", maior)
print("Menor valor:", menor)
print("Soma de todos os valores:", soma)
