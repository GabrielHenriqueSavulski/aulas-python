print('{:=^21}'.format('DESAFIO 067'))

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

while True:
    n = int(input(f'Quer ver a tabuada de qual número?{vermelho}(digite número negativo para sair){limpa} '))
    if n < 0:
        break
    c = 1
    print('-=-' * 40)
    while c <= 10:
        m = c * n
        print(f'{azul}{n}{limpa} X {amarelo}{c}{limpa} = {verde}{m}{limpa}')
        c += 1
    print('-=-' * 40)
