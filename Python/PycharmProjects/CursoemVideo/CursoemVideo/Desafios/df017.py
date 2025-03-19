from math import sqrt,pow
print('{:=^20}'.format('DESAFIO 015'))
ca = float(input('Escreva o valor do cateto adjacente: '))
co = float(input('Escreva o valor do cateto oposto: '))
h = sqrt(pow(ca, 2) + pow(co, 2))
print('A hipotenusa é {:.2f}'.format(h))
