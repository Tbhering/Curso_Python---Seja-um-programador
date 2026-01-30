l = float(input('Insira a largura da parede: '))
h = float(input('Insira a altura da parede: '))

a = l * h
t = a / 2

print(('A área total da parede é igual a {:.3} m² e são necessários {:.3}l  de tinta').format(a, t))