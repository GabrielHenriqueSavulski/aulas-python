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

s = c = 0

while True:
    n = int(input(f'Digite um número ou {vermelho}-1 para sair{limpa}: '))
    if n == -1:
        break
    s += n
    c += 1
print(f'A soma desses {azul}{c}{limpa} números resulta em: {azul}{s}{limpa}')
