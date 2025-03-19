from math import cos, sin, radians
print('{:=^20}'.format('DESAFIO 018'))
a = float(input('Digite um angulo em graus: '))
c = cos(radians(a))
s = sin(radians(a))
print('O cosseno de {}° é {:.2f} e o seno é {:.2f}'.format(a, c, s))
