print('{:=^21}'.format('DESAFIO 076'))

limpa = '\033[m'
negrito = '\033[1m'
sublinhado = '\033[4m'
inversor = '\033[7m'
cor = '\033[30m', '\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m', '\033[37m'
fundo = '\033[40m', '\033[41m', '\033[42m', '\033[43m', '\033[44m', '\033[45m', '\033[46m', '\033[47m'
'''códigos das cores 0 >  preto; 1 > vermelho; 2 > verde; 3 > amarelo;
                     4 > azul; 5 > roxo; 6 > ciano; 7 > cinza'''

prodpre = 'Caneta', 1.50, 'Estojo', 12.90, 'Caderno', 23.00

print('_' * 42)
print(f'{'LISTAGEM DE PREÇOS':^42}')
print('_' * 42)
for c in range(0, len(prodpre)):
    if c % 2 == 0:
        print(f'{prodpre[c]:.<30}', end='')
    else:
        print(f'R${prodpre[c]:>10.2f}')
print('_' * 42)