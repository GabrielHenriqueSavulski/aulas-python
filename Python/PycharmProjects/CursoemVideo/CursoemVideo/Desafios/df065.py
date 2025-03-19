print('{:=^21}'.format('DESAFIO 065'))

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

c = 0
s = 0
condicao = 'S'
maior = 0
menor = 0

while condicao != 'N':
    n = int(input('\nDigite um número: '))
    c += 1
    s += n
    if c == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    condicao = str(input('Deseja escrever mais números?[S/N] ')).strip().upper()

media = s / c

print('\nA media dos {1}{2}{0} números inseridos\n'
      'é {1}{3}{0}, o maior número é {1}{4}{0}\n'
      'e o menor número é {1}{5}{0}'.format(limpa, azul, c, media, maior, menor))
