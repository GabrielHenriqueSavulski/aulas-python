from math import trunc
print('{:=^20}'.format('DESAFIO 016'))
n = float(input('Digite qualquer número quebrado: '))
i = trunc(n)
print('A parte inteira de {} é {}'.format(n, i))
