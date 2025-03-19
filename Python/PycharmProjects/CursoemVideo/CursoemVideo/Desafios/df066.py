print('{:=^21}'.format('DESAFIO 066'))

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
while True:
    n = int(input(f'Digite um número, ou {azul}-1{limpa} para sair: '))
    if n == -1:
        break
    s += n
print(f'A soma desses números vale: {verde}{s}{limpa}')
