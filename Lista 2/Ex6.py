def somaimposto(taxaimposto,custo):
    return custo + (custo * (taxaimposto / 100))

taxa = float(input("Digite a taxa de imposto (%): "))
valor = float(input("Digite o custo do item: "))
print(f"O custo com imposto é: R${somaimposto(taxa, valor):.2f}")