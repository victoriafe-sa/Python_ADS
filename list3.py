# Leitura de 5 valores
valores = [int(input(f"Digite o valor {i+1}: ")) for i in range(5)]

# Encontrar o maior e o menor valor e suas posições
maior_valor = max(valores)
menor_valor = min(valores)
pos_maior = valores.index(maior_valor) + 1  # Adicionamos 1 para tornar a posição 1-based
pos_menor = valores.index(menor_valor) + 1

print(f"O maior valor é {maior_valor} na posição {pos_maior}.")
print(f"O menor valor é {menor_valor} na posição {pos_menor}.")
