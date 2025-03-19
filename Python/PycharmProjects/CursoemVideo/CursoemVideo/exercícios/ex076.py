limpa = '\033[m'
negrito = '\033[1m'
sublinhado = '\033[4m'
inversor = '\033[7m'
cor = '\033[30m', '\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m', '\033[37m'
fundo = '\033[40m', '\033[41m', '\033[42m', '\033[43m', '\033[44m', '\033[45m', '\033[46m', '\033[47m'
'''códigos das cores 0 >  preto; 1 > vermelho; 2 > verde; 3 > amarelo;
                     4 > azul; 5 > roxo; 6 > ciano; 7 > cinza'''

listagem = ('Pote de Sorvete', 15.90, 'Arroz', 12.45, '1Kg de Maçã', 3.40,
            'Doritos', 19.90, 'Alface', 2.99, 'Itubaína', 4.50)

print('_' * 40)
print(f'{"SUPERMERCADO DO ZÉ":^40}')
print('_' * 40)
for con in range(0, len(listagem)):
    if con % 2 == 0:
        print(f'{listagem[con]:.<30}', end='')
    else:
        print(f'R${listagem[con]:>8.2f}')
print('_' * 40)