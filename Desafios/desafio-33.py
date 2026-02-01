ano = int(input(' Digite um ano qualquer: '))

print(f' O ano {ano} é BISSEXTO!' if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0) else f' O ano {ano} NÃO É BISSEXTO!')