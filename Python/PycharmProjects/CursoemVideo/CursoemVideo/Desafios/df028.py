from random import choice

print('{:=^21}'.format('DESAFIO 028'))
números = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
np = int(choice(números))
r = int(input('Escolha um número de 0 a 10: '))
if np == r:
    print('Acertou!')
else:
    print('Errou!, o número era {}'.format(np))
