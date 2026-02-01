n = input(' Digite algo: ')

print('O tipo primitivo desse valor é', type(n))
print('contem espaços? {}, \nÉ alphanumeric? {}, \nÉ alfabético? {}, \nÉ decimal? {}, \nÉ dígito? {}, \nEstá em minúsculas? {}, \nEstá em maiúsculas? {}, \nEstá capitalizada? {}'
        .format(n.isspace(), n.isalnum(), n.isalpha(), n.isdecimal(), n.isdigit(), n.islower(),
                n.isupper(), n.istitle()))