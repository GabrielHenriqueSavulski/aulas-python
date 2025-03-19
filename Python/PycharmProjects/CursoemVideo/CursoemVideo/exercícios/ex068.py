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

print('-=-' * 50)
print(f'{roxo}JOGO DE PAR OU ÍMPAR{limpa}')
print('-=-' * 50)
v = 0
status = ''

while True:
    c = randint(0, 10)
    j = int(input(f'Qual sua jogada, {azul}"número"{limpa}? '))
    poui = str(input(f'Par ou ímpar, {azul}P ou I{limpa}: ')).strip()
    while poui not in 'PpIi':
        poui = str(input(f'{vermelho}Tente novamente{limpa}. Par ou ímpar, {azul}P ou I{limpa}: ')).strip()
    s = j + c
    if poui in 'Pp':
        if s % 2 == 0:
            print('=' * 20)
            print(f'Eu joguei {c} e você {j}, a soma deu {s}, que é par,\n'
                  f'portanto você {verde}GANHOU!!!{limpa}')
            v += 1
            print('=' * 20)
        if s % 2 != 0:
            print('=' * 20)
            print(f'Eu joguei {c} e você {j}, a soma deu {s}, que é ímpar,\n'
                  f'portanto você {vermelho}PERDEU!!!{limpa}')
            print('=' * 20)
            status = 'PERDEU'
    if poui in 'Ii':
        if s % 2 != 0:
            print('=' * 20)
            print(f'Eu joguei {c} e você {j}, a soma deu {s}, que é ímpar,\n'
                  f'portanto você {verde}GANHOU!!!{limpa}')
            print('=' * 20)
        if s % 2 == 0:
            print('=' * 20)
            print(f'Eu joguei {c} e você {j}, a soma deu {s}, que é par,\n'
                  f'portanto você {vermelho}PERDEU!!!{limpa}')
            v += 1
            print('=' * 20)
            status = 'PERDEU'
    if status == 'PERDEU':
        if v == 0:
            print(f'Você {vermelho}NÃO{limpa} obteve vitórias.')
        if v == 1:
            print(f'Você obteve {azul}{v}{limpa} vitória.')
        if v > 1:
            print(f'Você obteve {azul}{v}{limpa} vitórias.')
        break