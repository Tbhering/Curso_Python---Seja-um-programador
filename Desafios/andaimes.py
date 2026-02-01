ModeloAndaime = str(input(""" 
Bem-vindo a calculadora de M.C de andaimes industriais modelo galvanizado \n
                              
 1 - Torre Simples \n
 2 - Torre Germinada \n 
 3 - Suporte de Carga \n
 4 - Andaime em Balanço \n

Escolha o modelo do andaime: """))

if ModeloAndaime == '1':
    AlturaAndaime = float(input(" Digite a altura do andaime em metros: "))
    LarguraAndaime = float(input(" Digite a largura do andaime em metros:  "))
    ComprimentoAndaime = float(input(" Digite o comprimento do andaime em metros: "))
    
