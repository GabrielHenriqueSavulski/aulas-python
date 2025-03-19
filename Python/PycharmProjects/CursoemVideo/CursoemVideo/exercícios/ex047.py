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

from time import sleep
from random import choice
lista = [verde, vermelho, azul, amarelo, roxo, ciano]

print('{}Números pares de 1 a 50:{}'.format(sublinhado, limpa))

for c in range(2, 51, 2):
    escolha = choice(lista)
    print('{}{}{}'.format(escolha, c, limpa), end=' ')
    sleep(0.5)

print('Acabou!')