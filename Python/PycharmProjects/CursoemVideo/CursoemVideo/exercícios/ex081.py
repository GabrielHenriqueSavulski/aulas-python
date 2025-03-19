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
    cot = str(input('Quer continuar?[S/N] ')).strip()
    while cot not in 'SsNn':
        cot = str(input(f'{cor[1]}Valor inválido.{limpa} Quer continuar?[S/N] ')).strip()
    if cot in 'Nn':
        break

print(f'Foram digitados {len(lista)} números')
print(f'Os valores em ordem decrescente são: ', end='')
for c, n in enumerate(sorted(lista, reverse=True)):
    if c == 0:
        print(n, end='')
    elif c == len(lista) - 1:
        print(f' e {n}')
    else:
        print(f', {n}', end='')
if 5 in lista:
    print('O número 5 foi digitado')
else:
    print('O número 5 NÃO foi digitado')
