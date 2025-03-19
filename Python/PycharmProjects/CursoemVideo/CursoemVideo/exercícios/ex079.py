limpa = '\033[m'
negrito = '\033[1m'
sublinhado = '\033[4m'
inversor = '\033[7m'
cor = '\033[30m', '\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m', '\033[37m'
fundo = '\033[40m', '\033[41m', '\033[42m', '\033[43m', '\033[44m', '\033[45m', '\033[46m', '\033[47m'
'''códigos das cores 0 >  preto; 1 > vermelho; 2 > verde; 3 > amarelo;
                     4 > azul; 5 > roxo; 6 > ciano; 7 > cinza'''

from time import sleep

lista = []

while True:
    n = int(input('Digite um número: '))
    if n in lista:
        print(f'{cor[1]}Negado!{limpa} O número {n} já foi salvo na lista anteriormente')
    else:
        lista.append(n)
        print('Número salvo com sucesso.')
    continua = str(input('Quer continuar?[S/N] ')).strip()
    while continua not in 'SsNn':
        continua = str(input(f'{cor[1]}Tente novamente.{limpa} Quer continuar?[S/N] ')).strip()
    if continua in 'Nn':
        print('Encerrando...')
        sleep(1)
        break

print(f'Os números digitados em ordem crescente foram ', end='')
for i, c in enumerate(sorted(lista)):
    if i + 1 == len(lista):
        print(f' e {c}')
    elif i + 1 == 1:
        print(f'{c}', end='')
    else:
        print(f', {c}', end='')

print('Fim')
