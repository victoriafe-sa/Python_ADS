# Leitura do vetor de 10 posições
vetor = [int(input(f"Digite o valor para a posição {i+1}: ")) for i in range(10)]

# Contagem de números pares
pares = sum(1 for num in vetor if num % 2 == 0)

print(f"O vetor possui {pares} valores pares.")
