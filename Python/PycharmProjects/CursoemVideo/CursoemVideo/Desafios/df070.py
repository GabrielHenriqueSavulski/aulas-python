print('{:=^21}'.format('DESAFIO 070'))

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
c = 0
bn = ''
bv = 0
print('-' * 40)
print('LOJA SUPER BARATA')
print('-' * 40)
while True:
    nome = str(input('Qual o nome do produto? '))
    valor = int(input('Qual o valor do produto? R$'))
    s += valor
    if valor >= 1000:
        c += 1
    if bn == '':
        bn = nome
        bv = valor
    else:
        if valor < bv:
            bn = nome
            bv = valor
    cond = str(input('Quer continuar?[S/N] ')).strip()
    while cond not in 'SsNn':
        cond = str(input('Quer continuar?[S/N] ')).strip()
    if cond in 'Nn':
        break
print('=' * 40)
print('RESUMO')
print('=' * 40)
print(f'Você gastou {verde}R${s:.2f}{limpa} no total.\n'
      f'{vermelho}{c}{limpa} produtos custaram mais que R$1000,00.\n'
      f'{azul}{bn}{limpa} foi o produto mais barato, custando {azul}R${bv:.2f}{limpa}')
