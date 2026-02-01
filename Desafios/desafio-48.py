soma = 0

for numero in range(1, 501):
    if numero % 2 != 0 and numero % 3 == 0:
        soma += numero
        print(numero)

print(f"A soma dos números ímpares divisíveis por 3 é: {soma}")
