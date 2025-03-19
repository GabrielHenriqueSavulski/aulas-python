print('{:=^20}'.format('DESAFIO 023'))
número = int(input('Digite um número de 0 a 9999: '))
u = número // 1 % 10
d = número // 10 % 10
c = número // 100 % 10
m = número // 1000 % 10
print('Unidade: {}\n'
      'Dezena: {}\n'
      'Centena: {}\n'
      'Milhar: {}'
      .format(u, d, c, m))

