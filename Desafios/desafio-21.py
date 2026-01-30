import random

ordem = ['Pedro', 'João', 'Maria', 'Ana']
random.shuffle(ordem)
print(' A ordem de apresentação será: ')
for i in ordem:
    print(' {}'.format(i))