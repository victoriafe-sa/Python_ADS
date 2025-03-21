import numpy as np 

matriz = np.random.randint(10,100,size=[4,4])
print(matriz)

maior = np.max(matriz)
menor = np.min(matriz)
soma = np.sum(matriz)

print(maior)
print(menor)
print(soma)