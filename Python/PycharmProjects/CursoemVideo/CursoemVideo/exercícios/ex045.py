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
itens = ('Pedra', 'Papel', 'Tesoura')
print('{1}VAMOS JOGAR JOKEMPÔ{0}.\n'
      '{2}[1]{0} pedra\n'
      '{3}[2]{0} papel\n'
      '{4}[3]{0} tesoura'.format(limpa, azul, amarelo, vermelho, verde))

jogada = int(input('Digite {1}1{0}, {2}2{0} ou {3}3{0}: '.format(limpa, amarelo, vermelho, verde)))
escolha = randint(1, 3)

sleep(1)
print('{}{}{}JO{}'.format(sublinhado, negrito, amarelo, limpa))
sleep(1)
print('{}{}{}KEN{}'.format(sublinhado, negrito, vermelho, limpa))
sleep(1)
print('{}{}{}PÔ!!!{}'.format(sublinhado, negrito, verde, limpa))
sleep(1)

print('-=' * 14 + '-')
print('O {1}computador{2} escolheu {1}{0}{2}'.format(itens[escolha - 1], azul, limpa))
print('O {1}jogador{2} escolheu {1}{0}{2}'.format(itens[jogada - 1], roxo, limpa))
print('-=' * 14 + '-')

if escolha == 3 and jogada == 2 or escolha == 2 and jogada == 1 or escolha == 1 and jogada == 3:
    print('{}{}{}COMPUTADOR VENCE{}'.format(sublinhado, negrito, vermelho, limpa))
elif escolha == 2 and jogada == 3 or escolha == 1 and jogada == 3 or escolha == 3 and jogada == 1:
    print('{}{}{}JOGADOR VENCE{}'.format(sublinhado, negrito, verde, limpa))
elif escolha == jogada:
    print('{}{}{}EMPATE{}'.format(sublinhado, negrito, amarelo, limpa))


