sal = float(input('Qual o salário do funcionário? '))

if sal <= 1250:
    aumento = sal * 1.15
else:
    aumento = sal * 1.1
print('O salário desse funcionário passará a ser de R${:.2f}'.format(aumento))
