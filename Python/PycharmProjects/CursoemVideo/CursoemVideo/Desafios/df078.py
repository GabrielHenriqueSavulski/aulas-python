print('{:=^21}'.format('DESAFIO 078'))

limpa = '\033[m'
negrito = '\033[1m'
sublinhado = '\033[4m'
inversor = '\033[7m'
cor = '\033[30m', '\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m', '\033[37m'
fundo = '\033[40m', '\033[41m', '\033[42m', '\033[43m', '\033[44m', '\033[45m', '\033[46m', '\033[47m'
'''códigos das cores 0 >  preto; 1 > vermelho; 2 > verde; 3 > amarelo;
                     4 > azul; 5 > roxo; 6 > ciano; 7 > cinza'''

n = []

for c in range(0, 5):
    n.append(int(input(f'Digite um número, para a posição {c + 1}: ')))

print(f'O maior valor escrito foi {max(n)}, ele está nas posições {n.index(max(n)) + 1}...', end='')
if n.count(max(n)) >= 2:
    c = 1
    posicao = n.index(max(n)) + 1
    while c != n.count(max(n)):

        maximo = n.index(max(n), posicao) + 1
        print(f'{maximo}...', end='')
        posicao = maximo
        c += 1
    print('')
else:
    print('')
print(f'O menor valor escrito foi {min(n)}, ele está nas posições {n.index(min(n)) + 1}...', end='')
if n.count(min(n)) >= 2:
    c = 1
    posicao = n.index(min(n)) + 1
    while c != n.count(min(n)):

        minimo = n.index(min(n), posicao) + 1
        print(f'{minimo}...', end='')
        posicao = minimo
        c += 1
    print('')
else:
    print('')