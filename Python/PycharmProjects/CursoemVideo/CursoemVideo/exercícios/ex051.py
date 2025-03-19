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

razão = int(input('Digite a razão da progressão aritimética: '))
a1 = int(input('Digite o primeiro termo da progressão: '))

for c in range(1, 11):
    an = a1 + (c - 1) * razão
    print('{}{}{} ---->'.format(vermelho, an, limpa), end=' ')
print('n')
