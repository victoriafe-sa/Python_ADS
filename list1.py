# Leitura do vetor de 8 posições
vetor = [int(input(f"Digite o valor para a posição {i+1}: ")) for i in range(8)]

# Leitura dos valores X e Y
X = int(input("Digite o valor de X (posição no vetor): "))
Y = int(input("Digite o valor de Y (posição no vetor): "))

# Soma dos valores nas posições X e Y
soma = vetor[X-1] + vetor[Y-1]  # Subtraímos 1 porque as posições em Python começam do 0

print(f"A soma dos valores nas posições {X} e {Y} é: {soma}")
