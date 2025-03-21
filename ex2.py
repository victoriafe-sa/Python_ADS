import numpy as np

lista = np.random.randint(1,100,size=10)
print(lista)
pares = 0
for i in lista:
    if i%2 == 0:
        #pares = pares + 1
        pares +=1
print(f'Exitem {pares} numeros pares')