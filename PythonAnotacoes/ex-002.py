nome = input('Qual seu nome? ')
idade = input('Qual sua idade? ')
cidade = input('De qual cidade você é? ')


print('Olá', nome, '! você tem', idade, 'anoes de idade e é de', cidade + '.')
print(f'Olá {nome}! Você tem {idade} anos de idade e é de {cidade}.')
print('É um prazer te conhecer, {}!'.format(nome))