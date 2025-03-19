print('{:=^21}'.format('DESAFIO 058'))

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
r = 'S'
while r == 'S':
    c = 1
    num = randint(0, 10)
    print('-=-' * 20)
    print('Vou pensar em um número entre 0 e 10. Tente adivinhar ......')
    print('-=-' * 20)
    resp = int(input('Em que número pensei? '))
    print('PROCESSANDO....')
    sleep(2)
    if num == resp:
        print('Ahhh... Você ganhou! O número era {}.'.format(num))
    else:
        while resp != num:
            print('Errado, chuta outro.')
            resp = int(input('Qual número? '))
            c += 1
            sleep(1)
    print('Você precisou de {} tentativas.'.format(c))
    r = str(input('Quer continuar, [S/N] ')).upper()
