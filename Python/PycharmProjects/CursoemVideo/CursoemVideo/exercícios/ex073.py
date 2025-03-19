limpa = '\033[m'
negrito = '\033[1m'
sublinhado = '\033[4m'
inversor = '\033[7m'
cor = '\033[30m', '\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m', '\033[37m'
fundo = '\033[40m', '\033[41m', '\033[42m', '\033[43m', '\033[44m', '\033[45m', '\033[46m', '\033[47m'
'''códigos das cores 0 >  preto; 1 > vermelho; 2 > verde; 3 > amarelo;
                     4 > azul; 5 > roxo; 6 > ciano; 7 > cinza'''

times = ('Flamengo', 'Bahia', 'Botafogo', 'São Paulo', 'Athletico-PR', 'Bragantino', 'Palmeiras',
         'Internacional', 'Cruzeiro', 'Atlético-MG', 'Fortaleza', 'Juventude', 'Grêmio', 'Vasco',
         'Fluminense', 'Criciúma', 'Corinthians', 'Atlético-GO', 'Cuiabá', 'Vitória')

print('-=-' * 60)
print(f'{sublinhado}Os 20 primeiros times do Brasileirão são:{limpa} ', end='')
for c, selecao in enumerate(times):
    if c == 19:
        print(f'{c + 1}º {times[c]}')
    else:
        print(f'{c + 1}º {times[c]}', end=', ')
    if c == 8:
        print('\n')
print('-=-' * 60)
print(f'{sublinhado}Os cinco primeiros colocados do Brasileirão são:{limpa} ', end='')
for c in range(0, 5):
    if c == 4:
        print(f'{c + 1}º {times[c]}')
    else:
        print(f'{c + 1}º {times[c]}', end=', ')
print('-=-' * 60)
print(f'{sublinhado}Os quatro ultimos colocados são:{limpa} ', end='')
for c in range(1, 5):
    if c == 4:
        print(f'{21 - c}º {times[- c]}')
    else:
        print(f'{21 - c}º {times[- c]}', end=', ')
print('-=-' * 60)
print(f'{sublinhado}Os vinte primeiros times são, em ordem alfabética:{limpa} ', end='')
for c, selecao in enumerate(sorted(times)):
    if c == 19:
        print(selecao)
    elif c == 18:
        print(selecao, end=' e ')
    else:
        print(selecao, end=', ')
    if c == 6:
        print('\n')
print('-=-' * 60)
n = 0
for c, selecao in enumerate(times):
    if selecao == 'Vasco':
        n = c + 1
print(f'O {cor[2]}Vasco{limpa} está em {cor[2]}{n}{limpa}')
print('-=-' * 60)