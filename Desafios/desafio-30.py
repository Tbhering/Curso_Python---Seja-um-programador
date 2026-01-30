velocidade = float(input( ' Qual a velocidade atual do carro? Km/h'))

print( ' Sua velocidade é {velocidade}, você está dentro do limite permitido, tenha uma boa viagem!' if velocidade <= 80 
      else ' Sua velocidade é {}, MULTADO! Você excedeu o limite permitido que é de 80km/h.'.format(velocidade) )
