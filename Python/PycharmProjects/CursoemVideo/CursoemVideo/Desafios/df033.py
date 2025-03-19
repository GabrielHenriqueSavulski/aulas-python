print('{:=^21}'.format('DESAFIO 033'))

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite outro número: '))

if n1 > n2 and n1 > n3:
    print('{} é o maior valor'.format(n1))
if n2 > n1 and n2 > n3:
    print('{} é o maior valor'.format(n2))
if n3 > n1 and n3 > n2:
    print('{} é o maior valor'.format(n3))

if n1 < n2 and n1 < n3:
    print('{} é o menor valor'.format(n1))
if n2 < n1 and n2 < n3:
    print('{} é o menor valor'.format(n2))
if n3 < n1 and n3 < n2:
    print('{} é o menor valor'.format(n3))
