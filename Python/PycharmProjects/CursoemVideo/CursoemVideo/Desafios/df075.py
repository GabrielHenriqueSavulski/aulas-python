print('{:=^21}'.format('DESAFIO 075'))

limpa = '\033[m'
negrito = '\033[1m'
sublinhado = '\033[4m'
inversor = '\033[7m'
cor = '\033[30m', '\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m', '\033[37m'
fundo = '\033[40m', '\033[41m', '\033[42m', '\033[43m', '\033[44m', '\033[45m', '\033[46m', '\033[47m'
'''códigos das cores 0 >  preto; 1 > vermelho; 2 > verde; 3 > amarelo;
                     4 > azul; 5 > roxo; 6 > ciano; 7 > cinza'''

numeros = (int(input('Digite um número: ')), int(input('Digite um número: ')),
           int(input('Digite um número: ')), int(input('Digite um número: ')))

noves = numeros.count(9)
if noves == 0:
    print('O número 9 não apareceu')
elif noves == 1:
    print('O numero 9 apareceu 1 vez')
else:
    print(f'O número 9 apareceu {noves} vezes')

tres = -1
for c, n in enumerate(numeros):
    if n == 3:
        tres = c + 1
        break
if tres == -1:
    print('O número 3 não foi escrito')
else:
    print(f'O número 3 foi o {tres}º número a ser escrito')

print('Os números pares foram: ', end='')
p = 0
for c, n in enumerate(numeros):
    if n % 2 == 0:
        print(n, end=' ')
        p += 1
if p == 0:
    print('Não houve números pares')
