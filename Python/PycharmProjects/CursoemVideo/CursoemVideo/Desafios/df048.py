print('{:=^21}'.format('DESAFIO 048'))

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

s = 0
for c in range(1, 500):
    if c % 2 == 1 and c % 3 == 0:
        s += c
print('A somatória de todos os números ímpares\n'
      'múltiplos de 3, no intervalo de 1 a 500,\n'
      'resulta em {}{}{}'.format(vermelho, s, limpa))
