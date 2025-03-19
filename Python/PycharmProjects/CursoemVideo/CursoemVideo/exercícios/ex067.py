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
    print('=' * 40)
    n = int(input(f'De qual número você deseja ver a tabuada?'
                  f'\n{vermelho}Digite qualquer número negativo para sair{limpa}: '))
    if n < 0:
        break
    print('=' * 40)
    for c in range(1, 11):
        print(f'{n} X {c} = {n * c}')
