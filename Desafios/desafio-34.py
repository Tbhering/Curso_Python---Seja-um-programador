n = int(input(' Digite o primeiro número: '))
n2 = int(input(' Digite o segundo número: '))
n3 = int(input(' Digite o terceiro número: '))

print(f' O maior número é {n}' if n > n2 and n > n3 else f' O maior número é {n2}' if n2 > n and n2 > n3 else f' O maior número é {n3}')
print(f' O menor número é {n}' if n < n2 and n < n3 else f' O menor número é {n2}' if n2 < n and n2 < n3 else f' O menor número é {n3}')