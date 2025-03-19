print('{:=^21}'.format('DESAFIO 073'))

limpa = '\033[m'
negrito = '\033[1m'
sublinhado = '\033[4m'
inversor = '\033[7m'
cor = '\033[30m', '\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m', '\033[37m'
fundo = '\033[40m', '\033[41m', '\033[42m', '\033[43m', '\033[44m', '\033[45m', '\033[46m', '\033[47m'
'''códigos das cores 0 >  preto; 1 > vermelho; 2 > verde; 3 > amarelo;
                     4 > azul; 5 > roxo; 6 > ciano; 7 > cinza'''

times = ('Flamengo', 'Bahia', 'Botafogo', 'São Paulo', 'Athlatico-PR', 'Bragantino', 'Palmeiras',
         'Internacional', 'Cruzeiro', 'Atlético-MG', 'Fortaleza', 'Juventude', 'Grêmio', 'Vasco',
         'Fluminense', 'Criciúma', 'Corinthians', 'Atlético-GO', 'Cuiabá', 'Vitória')

print('-=-' * 120)
print('Os vinte primeiros times são: ', end='')
for c, time in enumerate(times):
    if c == 19:
        print(f'{c + 1}º {time}')
    else:
        print(f'{c + 1}º {time}', end=', ')
print('-=-' * 120)
print('Os cinco primeiros colocados são: ', end='')
for c in range(0, 5):
    if c == 4:
        print(f'{c + 1}º {times[c]}')
    else:
        print(f'{c + 1}º {times[c]}', end=', ')
print('-=-' * 120)
print('Os quatro últimos são: ', end='')
p = 17
for c in range(4, 0, -1):
    if c == 1:
        print(f'{p}º {times[-c]}')
    else:
        print(f'{p}º {times[-c]}', end=', ')
    p += 1
print('-=-' * 120)
print('Os times em ordem alfabética são: ', end='')
for c, time in enumerate(sorted(times)):
    if c == 19:
        print(f'{time}')
    else:
        print(f'{time}', end=', ')
print('-=-' * 120)
print('O Vasco está em: ', end='')
for c, time in enumerate(times):
    if time == 'Vasco':
        print(f'{c + 1}º')