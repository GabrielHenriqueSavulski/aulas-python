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

a1 = int(input('Qual o primeiro termo da PA? '))
razao = int(input('Qual a razão da PA? '))
n = 1
print('Os 10 primeiros termos da PA são:')
while n != 11:
    an = a1 + (n - 1) * razao
    if n == 10:
        print(an)
    else:
        print(an, end=', ')
    n += 1
