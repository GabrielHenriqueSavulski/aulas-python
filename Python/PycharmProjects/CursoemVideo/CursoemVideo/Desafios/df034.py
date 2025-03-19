print('{:=^21}'.format('DESAFIO 034'))

sal = float(input('Qual o valor do seu salário? R$'))

if sal <= 1250.00:
    aum = sal * 1.15
    print('Seu salário receberá um aumento de 15% e passará a ser de R${:.2f}'.format(aum))
else:
    aum = sal * 1.1
    print('Seu salário receberá um aumento de 10% e passará a ser de R${:.2f}'.format(aum))
