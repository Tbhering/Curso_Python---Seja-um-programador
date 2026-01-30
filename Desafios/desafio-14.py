salario = float(input(' Digite o salário do funcionário: '))
percentualaumento = float(input(' Qual o % de aumento para o funcionário? '))

percentual = percentualaumento / 100
novopercentual = salario * percentual
novosalario = salario + novopercentual

print((' Com o aumento de {}% no salário do funcionário, agora o novo salário passa a ser {:.6}$ ').format( percentualaumento, novosalario))