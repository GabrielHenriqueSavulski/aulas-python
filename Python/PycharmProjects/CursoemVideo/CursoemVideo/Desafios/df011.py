print('{:=^20}'.format('DESAFIO 11'))

print('Vamos calcular quanta tinta será necessária para pintar uma parede')
h = float(input('Qual a altura da parede? '))
l = float(input('Qual a largura da parede? '))
a = h * l
c = a / 2
print('O consumo de tinta em litros de uma parede com {:.2f}m²,\nconsiderando que cada litro cobre 2.00m², será de {:.2f}L'.format(a, c))
