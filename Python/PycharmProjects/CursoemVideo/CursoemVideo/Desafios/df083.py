print('{:=^21}'.format('DESAFIO 083'))

limpa = '\033[m'
negrito = '\033[1m'
sublinhado = '\033[4m'
inversor = '\033[7m'
cor = '\033[30m', '\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m', '\033[37m'
fundo = '\033[40m', '\033[41m', '\033[42m', '\033[43m', '\033[44m', '\033[45m', '\033[46m', '\033[47m'
'''códigos das cores 0 >  preto; 1 > vermelho; 2 > verde; 3 > amarelo;
                     4 > azul; 5 > roxo; 6 > ciano; 7 > cinza'''

conta = str(input('Digite sua expressão: '))
lista = []
for n in conta:
    lista.append(n)

abre = lista.count('(')
fecha = lista.count(')')

if abre == fecha:
    print('Sua expressão é válida')
else:
    print('Sua expressão é inválida')
