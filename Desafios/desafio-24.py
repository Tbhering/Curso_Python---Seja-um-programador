valor = int(input('Digite um numero entre 0 a 9999: '))

print(' Analisando o numero {}, concluimos que ele possui {} unidades, {} dezenas, {} centenas e {} milhar.'.format(valor, (valor // 1) % 10, (valor // 10) % 10, (valor // 100) % 10, (valor // 1000) % 10))