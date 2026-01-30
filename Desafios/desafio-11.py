real = float(input('Qual o valor que você possui na carteira? R$'))
dollar = real / 3.27

print(('Você pode comprar US${:.4}').format(dollar))