print('{:=^21}'.format('DESAFIO 081'))

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
    continua = str(input('Quer continuar?[S/N] ')).strip()
    while continua not in 'NnSs':
        continua = str(input('Valor incorreto. Quer continuar?[S/N] ')).strip()
    if continua in 'Nn':
        break

print(f'Foram digitados {len(lista)} números')
lista.sort(reverse=True)
print(f'Em ordem decrescente os números são {lista}')
if 5 in lista:
    print('O número cinco está na lista')
else:
    print('O número cinco não está na lista')

