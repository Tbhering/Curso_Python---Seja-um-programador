import random

x = random.randint(0, 5)
num = int(input(' Digite um número entre 0 e 5: '))

print( ' Você digitou o número {} e o número sorteado foi {}, Parabéns você acertou!.'.format(num, x) if num == x 
       else ' O número sorteado foi {}, Que pena! Você errou! Tente novamente.'.format(x)
       )