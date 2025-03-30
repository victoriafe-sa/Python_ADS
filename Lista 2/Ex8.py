import random

a_numeros = [random.randint(1, 100) for _ in range(10)]

def sorteia(lista):
    return random.sample(lista, 5)

def soma_par(lista):
    return sum(num for num in lista if num % 2 == 0)

print(f"Lista gerada: {a_numeros}")

sorteados = sorteia(a_numeros)
print(f"Números sorteados: {sorteados}")

print(f"Soma dos pares sorteados: {soma_par(sorteados)}")