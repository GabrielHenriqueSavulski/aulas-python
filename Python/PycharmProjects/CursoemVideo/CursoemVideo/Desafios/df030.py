print('{:=^21}'.format('DESAFIO 030'))

n = int(input('Digite um número inteiro: '))
d = n % 2
if d == 0:
    print('O número {} é par'.format(n))
else:
    print('O número {} é ímpar'.format(n))
