print('{:=^21}'.format('DESAFIO 059'))

limpa = '\033[m'
negrito = '\033[1m'
sublinhado = '\033[4m'
inversor = '\033[7m'
preto = '\033[30m' # 40 para cor do fundo
vermelho = '\033[31m'
verde = '\033[32m'
amarelo ='\033[33m'
azul = '\033[34m'
roxo = '\033[35m'
ciano = '\033[36m'
cinza = '\033[37m'

from time import sleep
continuar = 4
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
while continuar == 4:
    sleep(.5)
    print('O que deseja fazer:'.format(limpa, azul))
    sleep(.5)
    print('{1}[1]{0} Somar'.format(limpa, azul))
    sleep(.5)
    print('{1}[2]{0} Multiplicar'.format(limpa, azul))
    sleep(.5)
    print('{1}[3]{0} Maior número'.format(limpa, azul))
    sleep(.5)
    print('{1}[4]{0} Inserir novos números'.format(limpa, azul))
    sleep(.5)
    print('{1}[5]{0} Sair do programa'.format(limpa, azul))
    sleep(.5)
    menu = int(input('Qual opção? '))
    sleep(.5)
    if menu == 1:
        soma = n1 + n2
        print('A soma é {}'.format(soma))
    elif menu == 2:
        multi = n1 * n2
        print('A multiplicação é {}'.format(multi))
    elif menu == 3:
        maior = n1
        if n2 > maior:
            maior = n2
        print('O maior número é {}'.format(maior))
    elif menu == 4:
        n3 = int(input('Digite um número: '))
        n4 = int(input('Digite outro número: '))
        n1 = n3
        n2 = n4
    elif menu == 5:
        continuar = 5
