n1 = int(input('Digite um número: '))
print('-'*16)
print(f'Tabuada do {n1}')
print('-'*16)
for i in range(0,11):
    print(f'{n1} x {i} = {n1 * i}')
print('-'*16)