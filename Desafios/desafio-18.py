import math

catetooposto = float(input(' Digite o comprimento do cateto oposto: '))
catetoadjacente = float(input(' Digite o comprimento do cateto adjacente: '))

print(' A hipotenusa vai medir {:.2f} '.format(math.hypot(catetooposto, catetoadjacente)))