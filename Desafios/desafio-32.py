viagem = float(input(' Qual a distância da viagem em Km? '))

print(f' Você está prestes a começar uma viagem de {viagem}Km. O preço da passagem será de R${viagem * 0.50:.2f}' if viagem <= 200
      else f' Você está prestes a começar uma viagem de {viagem}Km. O preço da passagem será de R${viagem * 0.45:.2f}')