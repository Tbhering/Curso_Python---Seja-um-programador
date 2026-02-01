salario = float(input( ' Digite o salário do funcionário: '))

if salario <= 1250:
    novosalario = salario + (salario * 15 / 100)
else:
    novosalario = salario + (salario * 10 / 100)

print(f' Para o salário de R${salario:.2f}, com o aumento aplicado, o novo salário passa a ser R${novosalario:.2f}')