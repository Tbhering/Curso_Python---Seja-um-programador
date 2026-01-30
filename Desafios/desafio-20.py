import random

sorteio = random.randint(0, 3)

sorteados = ('Pedro', 'João', 'Maria', 'Ana')

#n = int(input(' Digite um número entre 0 e 3: '))

print(' O número sorteado foi {} e nosso aluno sorteado neste número é {} \n Parabéns, {} !!'.format(sorteio, sorteados[sorteio], sorteados[sorteio]))
