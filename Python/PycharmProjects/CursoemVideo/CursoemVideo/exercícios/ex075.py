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

nove = numeros.count(9)
if nove == 0:
    print(f'{cor[1]}Não{limpa} foi digitado nenhum nove.')
elif nove == 1:
    print(f'Foi digitado {cor[5]}{nove}{limpa} número nove.')
else:
    print(f'Foram digitados {cor[5]}{nove}{limpa} números nove.')

existe = numeros.count(3)
if existe == 0:
    print(f'{cor[1]}Nenhum{limpa} números três foi digitado')
else:
    print(f'O {cor[4]}Primeiro{limpa} número três foi digitado na {numeros.index(3) + 1}º posição')

print(f'Os números {cor[2]}pares{limpa} digitados foram: ', end='')
for c, n in enumerate(numeros):
    if n % 2 == 0:
        print(n, end=' ')
