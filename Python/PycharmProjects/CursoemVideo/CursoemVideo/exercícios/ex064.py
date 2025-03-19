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

c = -1
soma = 1
n = 0
while n != -1:
    n = int(input('Digite um número inteiro, ou -1 para parar: '))
    soma += n
    c += 1
if c == 1:
    print('Você digitou {} número, ele é {}'.format(c, soma))
else:
    print('Você digitou {} números, a soma deles é {}'.format(c, soma))
