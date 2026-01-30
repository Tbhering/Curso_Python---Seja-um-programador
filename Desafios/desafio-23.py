nome = str(input(' Digite seu nome completo: ')).strip()

print(nome.upper())                   # Converte todo o nome para maiúsculas
print(nome.lower())                   # Converte todo o nome para minúsculas
print(len(nome.replace(' ', '')))     # Conta o número de caracteres, removendo espaços extras nas extremidades)
print(len(nome.split()[0]))           # Conta o número de caracteres do primeiro nome
