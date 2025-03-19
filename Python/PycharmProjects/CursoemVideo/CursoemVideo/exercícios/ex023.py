n = int(input('Digite um número: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('Analisando o número {} temos que:\n'
      'Unidade = {}\n'
      'Dezena = {}\n'
      'Centena = {}\n'
      'Milhar = {}'
      .format(n, u, d, c, m))
