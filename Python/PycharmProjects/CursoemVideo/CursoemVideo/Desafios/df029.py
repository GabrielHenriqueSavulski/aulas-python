print('{:=^21}'.format('DESAFIO 029'))

vel = int(input('A qual velocidade você passou no radar?Apenas números '))
vmax = int(80)
if vel > vmax:
    print('Você foi multado, a velocidade máxima era 80Km/h')
    vex = int(vel - vmax)
    val = float(vex * 7)
    print('Por passar {}Km/h acima da velocidade máxima, o valor da multa é: R${:.2f}'.format(vex, val))
elif vel < (vmax/2):
    print('Você foi multado por baixa velocidade em uma via de 80Km/h')
    abv = int(vmax - vel)
    val = float(abv * 7)
    print('Por trafegar {}Km/h abaixo do permitido, o valor da sua multa é de R${:.2f}'.format(abv, val))
else:
    print('Tudo ok.')
