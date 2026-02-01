velocidade = float(input( ' Qual a velocidade atual do carro em Km/h?'))

print( f' Sua velocidade é {velocidade:.2f}, você está dentro do limite permitido, tenha uma boa viagem!' if velocidade <= 80 
      else f' Sua velocidade é {velocidade:.2f}, MULTADO! Você excedeu o limite permitido que é de 80km/h. Você deve pagar uma multa de R${(velocidade - 80)*7} reais.')
