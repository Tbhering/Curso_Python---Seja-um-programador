kmpercorridos = float(input(' Qual a distância em km percorrida pelo carro? '))
diasalugados = int(input(' Por quantos dias o carro foi alugado? '))

custodia = 60.00
custokm = 0.15

print((' O custo total do aluguel do carro considerando {} dias alugados e {:.2f} km percorridos é de R${:.2f}').format(diasalugados, kmpercorridos, (custodia * diasalugados) + (custokm * kmpercorridos)))
