def quantidade_digitos(numero):
    x = len(str(abs(numero)))
    print(f"O número {numero} tem {x} dígitos.")

quantidade_digitos(int(input("Digite um número inteiro: ")))