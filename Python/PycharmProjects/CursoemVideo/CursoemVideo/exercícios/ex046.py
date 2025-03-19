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

import emoji
from time import sleep

for c in range(10, -1, -1):
    print(c)
    sleep(1)
print(emoji.emojize('!FOGOS!\n'
      '🎆🎇🎆🎇🎆🎇🎆🎇🎆🎇🎆'))
