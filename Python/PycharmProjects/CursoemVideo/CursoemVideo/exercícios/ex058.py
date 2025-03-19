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

from random import randint
from time import sleep

c = 0
print('{}{}JOGO DE ADIVINHA!!!{}'.format(sublinhado, azul, limpa))
sleep(1)
print('Olá sou o computador, serei seu oponente,\n'
      'pensei em um número de {}0 a 10{}, tente adivinha-lo.'.format(amarelo, limpa))
escolha = randint(0, 10)
sleep(1)
print('-=-' * 20)
resposta = int(input('Qual seu palpite? '))
print('-=-' * 20)
sleep(1)
print('PROCESSANDO....')
sleep(2)

if resposta == escolha:
    print('UAU!!! Você acertou!')
else:
    while resposta != escolha:
        moum = ''
        if resposta > escolha:
            moum = '{}menor{}'.format(vermelho, limpa)
        if resposta < escolha:
            moum = '{}maior{}'.format(vermelho, limpa)
        resposta = int(input('ERROU!!! Tente novamente, o número é {}... '.format(moum)))
        c += 1
    if c == 1:
        print('ACERTOU! Você levou {}{}{} tentativa extras para acertar.'.format(vermelho, c, limpa))
    else:
        print('ACERTOU! Você levou {}{}{} tentativas extras para acertar.'.format(vermelho, c, limpa))
