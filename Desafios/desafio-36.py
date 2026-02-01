print( " Digite três valores quaisquer:")

valor = float(input( " 1 - valor: "))
valor2 = float(input(" 2 - valor: "))
valor3 = float(input(" 3 - valor: "))

a = valor
b = valor2
c = valor3

if a + b > c and a + c > b and b + c > a:
    print(" Os valores acima PODEM FORMAR um triângulo")
else:
    print(" Os valores acima NÃO PODEM FORMAR um triângulo")