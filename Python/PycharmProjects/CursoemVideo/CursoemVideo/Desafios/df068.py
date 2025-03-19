print('{:=^21}'.format('DESAFIO 068'))

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

from random import randint
print('-' * 30)
print(f'{sublinhado}{roxo}VAMOS JOGAR PAR OU ÍMPAR{limpa}')
print('-' * 30)
while True:
    computador = randint(1, 10)
    jogada = int(input('Escolha um número: '))
    poui = str(input('Par ou ímpar?[P/I] ')).strip().upper()
    while poui not in 'PpIi':
        poui = str(input(f'{vermelho}Opção inválida{limpa}, tente novamente,\n'
                         f'digite P ou I: '))
    c = 0
    s = jogada + computador
    r = s % 2
    status = ''
    if poui in 'Pp':
        if r == 0:
            print('=' * 10)
            print(f'Você {azul}ganhou!{limpa}')
            print(f'O computador escolheu {amarelo}{computador}{limpa} e você {verde}{jogada}{limpa},'
                  f' totalizando {azul}{s}{limpa} que é par')
            print('=' * 10)
            c += 1
        elif r != 0:
            print('=' * 10)
            print(f'Você {vermelho}perdeu!{limpa}')
            print(f'O computador escolheu {amarelo}{computador}{limpa} e você {verde}{jogada}{limpa},'
                  f' totalizando {azul}{s}{limpa} que é ímpar')
            print('=' * 10)
            status = 'Perdeu'
    if poui in 'Ii':
        if r != 0:
            print('=' * 10)
            print(f'Você {azul}ganhou!{limpa}')
            print(f'O computador escolheu {amarelo}{computador}{limpa} e você {verde}{jogada}{limpa},'
                  f' totalizando {azul}{s}{limpa} que é ímpar')
            print('=' * 10)
            c += 1
        elif r == 0:
            print('=' * 10)
            print(f'Você {vermelho}perdeu!{limpa}')
            print(f'O computador escolheu {amarelo}{computador}{limpa} e você {verde}{jogada}{limpa},'
                  f' totalizando {azul}{s}{limpa} que é par')
            print('=' * 10)
            status = 'Perdeu'
    if status == 'Perdeu':
        print(f'{negrito}{azul}Você obteve {c} vítorias.')
        break
