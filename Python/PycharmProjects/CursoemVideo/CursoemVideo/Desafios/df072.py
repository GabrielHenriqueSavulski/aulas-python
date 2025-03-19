print('{:=^21}'.format('DESAFIO 072'))

limpa = '\033[m'
negrito = '\033[1m'
sublinhado = '\033[4m'
inversor = '\033[7m'
cor = '\033[30m', '\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m', '\033[37m'
fundo = '\033[40m', '\033[41m', '\033[42m', '\033[43m', '\033[44m', '\033[45m', '\033[46m', '\033[47m'
'''códigos das cores 0 >  preto; 1 > vermelho; 2 > verde; 3 > amarelo;
                     4 > azul; 5 > roxo; 6 > ciano; 7 > cinza'''

contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
            'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    n = int(input('digite um número de 0 a 20: '))
    while n < 0 or n > 20:
        n = int(input(f'{cor[1]}Inválido{limpa}, digite um número de 0 a 20: '))

    print(f'A forma extensa de {cor[2]}{n}{limpa} é {cor[2]}{contagem[n]}{limpa}')

    sai = str(input('Quer parar?[S/N]: ')).strip()
    while sai not in 'SsNn':
        sai = str(input(f'{cor[1]}Resposta inválida{limpa}. Quer parar?[S/N]: ')).strip()
    if sai in 'Ss':
        break
