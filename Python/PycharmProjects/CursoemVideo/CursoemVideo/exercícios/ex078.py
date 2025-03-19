limpa = '\033[m'
negrito = '\033[1m'
sublinhado = '\033[4m'
inversor = '\033[7m'
cor = '\033[30m', '\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m', '\033[37m'
fundo = '\033[40m', '\033[41m', '\033[42m', '\033[43m', '\033[44m', '\033[45m', '\033[46m', '\033[47m'
'''códigos das cores 0 >  preto; 1 > vermelho; 2 > verde; 3 > amarelo;
                     4 > azul; 5 > roxo; 6 > ciano; 7 > cinza'''

lista = []

for c in range(0, 5):
    lista.append(int(input(f'{c + 1}º Digite um número: ')))

print(f'O maior valor da lista foi {max(lista)}, e suas posições foram ', end='')
for i, v in enumerate(lista):
    if v == max(lista):
        print(f'{i + 1}º...', end='')
print('e só')
print(f'O menor valor da lista foi {min(lista)}, e suas posições foram ', end='')
for i, v in enumerate(lista):
    if v == min(lista):
        print(f'{i + 1}º...', end='')
print('e só')
