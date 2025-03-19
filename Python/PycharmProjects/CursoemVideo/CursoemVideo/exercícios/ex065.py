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

maior = 0
menor = 0
s = 0
c = 0
cond = 'S'
while cond not in 'Nn':
    n = int(input('Digite um número: '))
    cond = str(input('Quer continuar? [S/N] ')).strip().upper()
    s += n
    c += 1
    if c == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    while cond not in 'SsNn':
        cond = str(input('Quer continuar? [S/N] ')).strip().upper()
media = s / c
print('Foi digitado {1}{2}{0} números, a média deles é {1}{3}{0}\n'
      'o maior é {1}{4}{0} e o menor é {1}{5}{0}'.format(limpa, azul, c, media,maior, menor))
