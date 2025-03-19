vel = float(input('Qual a velocidade atual do carro? '))
vmax = 80
if vel > vmax:
    exc = vel - vmax
    multa = exc * 7
    print('Multado! Você ultrapassou a velocidade em {}Km/h,\n'
          'portantando deverá pagar uma multa de R${:.2f}'.format(exc, multa))
elif vel < (vmax / 2):
    falta = vmax - vel - 40
    multa = falta * 7
    print('Multado! Você está muito lento em uma via de 80Km/h,\n'
          'portanto será multado em R${:.2f}'.format(multa))
else:
    print('Tudo certo! tenha uma boa viagem!')
print('Diraja com segurança!')
