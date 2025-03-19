print('{:=^21}'.format('DESAFIO 069'))

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

p = 0
h = 0
m = 0
while True:
    print('-' * 30)
    idade = int(input(f'{amarelo}Digite a idade:{limpa} '))
    sexo = str(input(f'{azul}Sexo? [M/F]{limpa} ')).strip()
    while sexo not in 'MmFf':
        sexo = str(input(f'{azul}Sexo? [M/F]{limpa}')).strip()
    if idade >= 18:
        p += 1
    if sexo in 'Mm':
        h += 1
    if sexo in 'Ff' and idade <= 20:
        m += 1
    cont = str(input(f'{roxo}Quer continuar? [S/N]{limpa} ')).strip()
    while cont not in 'SsNn':
        cont = str(input(f'{roxo}Quer continuar? [S/N]{limpa} ')).strip()
    if cont in 'Nn':
        break
print('=' * 30)
print(f'Nesse grupo tem {verde}{p}{limpa} com pessoas mais de 18 anos,\n'
      f'{azul}{h}{limpa} homens e {roxo}{m}{limpa} mulheres com menos de 20 anos')
