frase = 'Curso em Video Python'

print(frase.replace('Python', 'Android')) # Substitui 'Python' por 'Android' na string frase
print(frase.upper().replace('VIDEO', 'ANDROID')) # Converte a string para maiúsculas e substitui 'VIDEO' por 'ANDROID'
print('Curso' in frase) # Verifica se a substring 'Curso' está presente na string frase
print('curso' in frase) # Verifica se a substring 'curso' (minúscula) está presente na string frase
print(frase.find('Video')) # Retorna o índice da primeira ocorrência da substring 'Video' na string frase
print(frase.find('video')) # Retorna -1, pois 'video' (minúscula) não está presente na string frase
print(frase.split()) # Divide a string frase em uma lista de palavras
print(frase.split()[0]) # Divide a string frase em uma lista de palavras e retorna a primeira palavra
print('-'.join(frase.split())) # Divide a string frase em uma lista de palavras e junta-as com '-' entre elas
print(frase.capitalize()) # Converte a primeira letra da string frase para maiúscula e o restante para minúscula
print(frase.title()) # Converte a primeira letra de cada palavra na string frase para maiúscula
print(frase.strip()) # Remove espaços em branco no início e no final da string frase
print(frase.rstrip()) # Remove espaços em branco no final da string frase
print(frase.lstrip()) # Remove espaços em branco no início da string frase
print(frase.center(50)) # Centraliza a string frase em um campo de largura 50
print(frase.count('o')) # Conta quantas vezes a letra 'o' aparece na string frase
print(frase.count('o', 0, 13)) # Conta quantas vezes a letra 'o' aparece na string frase entre os índices 0 e 13
print(frase.startswith('Curso')) # Verifica se a string frase começa com 'Curso'
print(frase.endswith('Python')) # Verifica se a string frase termina com 'Python'
print(frase.replace('Python', 'Java').upper().count('A')) # Substitui 'Python' por 'Java', converte para maiúsculas e conta quantas vezes 'A' aparece na string resultante
print(frase[::-1]) # Inverte a string frase
print(frase[::2]) # Imprime os caracteres da string frase com passo 2 (ou seja, pula um caractere)
print(frase[9:14]) # Imprime os caracteres da string frase do índice 9 ao 13
print(frase[9:21:3]) # Imprime os caracteres da string frase do índice 9 ao 20 com passo 3
print(len(frase)) # Imprime o comprimento da string frase
print(len(frase.strip())) # Imprime o comprimento da string frase sem espaços em branco no início e no final
print(frase.replace(' ', '').upper()) # Remove todos os espaços da string frase e converte para maiúsculas
print(frase.split()[2][3:6]) # Divide a string frase em uma lista de palavras, pega a terceira palavra e imprime os caracteres do índice 3 ao 5
print(frase.encode('utf-8')) # Codifica a string frase em bytes usando UTF-8
print(frase.encode('utf-8').decode('utf-8')) # Codifica a string frase em bytes usando UTF-8 e depois decodifica de volta para string
print(frase.replace('em', 'no')) # Substitui 'em' por 'no' na string frase
