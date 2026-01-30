val = float(input(' O preço deste produto é: R$'))
des = float(input(' O valor do desconto é: %'))

tdes = des / 100

vdes = val  * tdes
vfin = val - vdes

print(('O valor do produto com {}% de desconto é igual a {:.4}').format(des, vfin))