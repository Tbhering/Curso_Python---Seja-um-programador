#Aula 3 - Operadores Básicos
#concatenação de strings
n1 = input(' Digite um número: ')
n2 = input(' Digite outro número: ')
s  = n1 + n2
print(' A soma entre os valores é', s)

#-------------------------------------------------------------
#Aula 4 - Conversão de Tipos primitivos exemplo 01
#int() float() str() bool()

n3 = int(input(' Digite um número: '))
n4 = int(input(' Digite outro número: '))
s1 = n3 + n4
print(' A soma entre os valores é', s1)

#-------------------------------------------------------------
#Aula 4 - Conversão de Tipos primitivos exemplo 02
#int() float() str() bool()

n5 = int(input(' Digite um número: '))
n6 = int(input(' Digite outro número: '))
s2 = n5 + n6
print(' A soma entre os valores é {}'.format(s2))

#-------------------------------------------------------------
#Aula 4 - Conversão de Tipos primitivos exemplo 03
#int() float() str() bool()

n7 = int(input(' Digite um número: '))
n8 = int(input(' Digite outro número: '))
s3 = n7 + n8
print(' A soma entre', n7, 'e', n8, 'vale', s3) #uso de vírgulas
print(' A soma entre {} e {} vale {}'.format(n7, n8, s3)) #uso do método format