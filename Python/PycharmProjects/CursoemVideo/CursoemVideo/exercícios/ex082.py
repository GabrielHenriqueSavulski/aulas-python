limpa = '\033[m'
negrito = '\033[1m'
sublinhado = '\033[4m'
inversor = '\033[7m'
cor = '\033[30m', '\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m', '\033[37m'
fundo = '\033[40m', '\033[41m', '\033[42m', '\033[43m', '\033[44m', '\033[45m', '\033[46m', '\033[47m'
'''códigos das cores 0 >  preto; 1 > vermelho; 2 > verde; 3 > amarelo;
                     4 > azul; 5 > roxo; 6 > ciano; 7 > cinza'''

lista = []

while True:
    lista.append(int(input('Digite um número: ')))
    continua = str(input('Quer continuar?[S/N] '))
    while continua not in 'SsNn':
        continua = str(input(f'{cor[1]}Valor negado!{limpa} Quer continuar?[S/N] '))
    if continua in 'Nn':
        break

lista.sort()
print('_' * 30)
print('A lista completa foi: ', end='')
for c, n in enumerate(lista):
    if c == 0:
        print(n, end='')
    elif c == len(lista) - 1:
        print(f' e {n}.')
    else:
        print(f', {n}', end='')

pares = []
impares = []

for num in lista:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print('Os números pares foram: ', end='')
for c, n in enumerate(pares):
    if c == 0:
        print(n, end='')
    elif c == len(pares) - 1:
        print(f' e {n}.')
    else:
        print(f', {n}', end='')

print('E os números pares foram: ', end='')
for c, n in enumerate(impares):
    if c == 0:
        print(n, end='')
    elif c == len(impares) - 1:
        print(f' e {n}.')
    else:
        print(f', {n}', end='')
