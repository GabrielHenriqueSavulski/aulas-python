l = float(input('Largura da parede: '))
h = float(input('Altura da parede: '))
a = h * l
c = a / 2
print('Sua parede de dimensção {}m X {}m, tem uma área de {}m².'.format(l, h, a))
print('Para pintar essa parede, considerando que 1L de tinta cobre 2m² de parede,'
      '\nserá necessário {}L de tinta.'.format(c))
