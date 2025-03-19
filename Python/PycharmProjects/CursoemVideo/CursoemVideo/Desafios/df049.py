print('{:=^21}'.format('DESAFIO 049'))

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

n = int(input('Digite um número para saber a tabuada dele: '))
t = int(input('Digite um valor para saber qual o alcance da tabuada: '))
for c in range(0, t + 1):
    m = n * c
    print('{1}{4}{0} X {2}{5}{0} = {3}{6}{0}'.format(limpa, verde, azul, vermelho, n, c, m))
