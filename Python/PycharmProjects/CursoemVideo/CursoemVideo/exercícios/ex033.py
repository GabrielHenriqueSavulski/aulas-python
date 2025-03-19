n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
n3 = float(input('Terceiro valor: '))

if n2 < n1 > n3:
    print('O maior valor é {}'.format(n1))
if n1 < n2 > n3:
    print('O maior valor é {}'.format(n2))
if n2 < n3 > n1:
    print('O maior valor é {}'.format(n3))

if n2 > n1 < n3:
    print('O menor valor é {}'.format(n1))
if n1 > n2 < n3:
    print('O menor valor é {}'.format(n2))
if n2 > n3 < n1:
    print('O menor valor é {}'.format(n3))
