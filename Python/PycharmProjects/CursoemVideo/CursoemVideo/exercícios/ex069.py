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

a = h = m = 0

while True:
    i = int(input('Qual a idade? '))
    s = str(input('Masculino ou Feminino? [M/F]: ')).strip()
    while s not in 'MmFf':
        s = str(input(f'{vermelho}Tente novamente{limpa}. Masculino ou Feminino? [M/F]: ')).strip()
    if i >= 18:
        a += 1
    if s in 'Mm':
        h += 1
    if s in 'Ff' and i <= 20:
        m += 1
    c = str(input('Quer continuar? [S/N]: ')).strip()
    while c not in 'SsNn':
        c = str(input(f'{vermelho}Tente novamente{limpa}. Quer continuar? [S/N]: ')).strip()
    if c in 'Nn':
        break
print('=' * 40)
print(f'No grupo cadastrado existem {verde}{a} adultos{limpa},\n'
      f'{azul}{h} homens{limpa} e {roxo}{m} meninas{limpa} com 20 anos ou menos')
