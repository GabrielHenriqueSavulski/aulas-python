limpa = '\033[m'
negrito = '\033[1m'
sublinhado = '\033[4m'
inversor = '\033[7m'
preto = '\033[30m' # 40 para cor do fundo
vermelho = '\033[31m'
verde = '\033[32m'
amarelo ='\033[33m'
azul = '\033[34m'
roxo = '\033[35m'
ciano = '\033[36m'
cinza = '\033[37m'

peso = float(input('Qual seu peso (KG)? '))
altura = float(input('Qual sua altura (m)? '))

imc = peso / (altura ** 2)
estado = 's'
if imc < 18.5:
    estado = 'abaixo do peso'
elif 18.5 <= imc <= 25:
    estado = 'no peso ideal'
elif 25 < imc <= 30:
    estado = 'com sobrepeso'
elif 30 < imc <= 40:
    estado = 'com obesidade'
elif 40 < imc:
    estado = 'com obesidade mórbida'

print('Segundo o seu IMC, você está {}'.format(estado))