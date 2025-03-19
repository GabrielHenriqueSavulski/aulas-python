from math import sin, cos, tan, radians
an = float(input('Insira um ângulo qualquer: '))
seno = sin(radians(an))
cosseno = cos(radians(an))
tangente = tan(radians(an))
print('O ângulo {0} tem o valor do seno sendo: {1:.2f}\n'
      'O ângulo {0} tem o valor do cosseno sendo: {2:.2f}\n'
      'O ângulo {0} tem o valor da tangente sendo: {3:.2f}'
      .format(an, seno, cosseno, tangente))
