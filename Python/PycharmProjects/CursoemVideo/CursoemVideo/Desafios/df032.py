print('{:=^21}'.format('DESAFIO 032'))

ano = int(input('Qual ano você deseja saber se é bissexto? '))
if ano % 4 == 0:
    print('O ano {} é bissexto.'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))
