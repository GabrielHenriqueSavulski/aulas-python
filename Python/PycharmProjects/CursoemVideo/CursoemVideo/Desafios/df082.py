print('{:=^21}'.format('DESAFIO 082'))

limpa = '\033[m'
negrito = '\033[1m'
sublinhado = '\033[4m'
inversor = '\033[7m'
cor = '\033[30m', '\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m', '\033[37m'
fundo = '\033[40m', '\033[41m', '\033[42m', '\033[43m', '\033[44m', '\033[45m', '\033[46m', '\033[47m'
'''códigos das cores 0 >  preto; 1 > vermelho; 2 > verde; 3 > amarelo;
                     4 > azul; 5 > roxo; 6 > ciano; 7 > cinza'''

num = []
while True:
    num.append(int(input('Digite um número: ')))
    continua = str(input('Quer continuar?[S/N] '))
    while continua not in 'SsNn':
        continua = str(input('Valor incorreto. Quer continuar?[S/N] '))
    if continua in 'Nn':
        break

pares = []
impares = []

for n in num:
    if n % 2 == 0:
        pares.append(n)
    elif n % 2 != 0:
        impares.append(n)

print(f'A lista completa dos números é {num}')
print(f'Os números pares são {pares}')
print(f'Os números impares são {impares}')
