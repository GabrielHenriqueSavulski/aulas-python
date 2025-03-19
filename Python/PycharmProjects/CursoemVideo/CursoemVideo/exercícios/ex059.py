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

from time import  sleep

n1 = int(input('Insira um número: '))
sleep(.5)
n2 = int(input('Isira mais um número: '))
sleep(.5)
continua = 0
while continua != 5:
    print('\n' + azul + '='*20 + limpa)
    sleep(.5)
    print('O que deseja fazer?')
    sleep(.5)
    print('{}[1]{} somar'.format(amarelo, limpa))
    sleep(.5)
    print('{}[2]{} multiplicar'.format(amarelo, limpa))
    sleep(.5)
    print('{}[3]{} maior número'.format(amarelo, limpa))
    sleep(.5)
    print('{}[4]{} novos números'.format(amarelo, limpa))
    sleep(.5)
    print('{}[5]{} sair do programa'.format(amarelo, limpa))
    sleep(.5)
    opcao = str(input('Digite a opção desejada, apenas número: ')).strip()
    sleep(.5)
    while opcao not in '12345':
        opcao = str(input('Opção inválida, tente novamente: '))
        sleep(.5)
    print(azul + '=' * 20 + limpa + '\n')
    sleep(.5)
    if opcao == '1':
        soma = n1 + n2
        print('A soma desses números é {}{}{}'.format(verde, soma, limpa))
        sleep(2)
    elif opcao == '2':
        multi = n1 * n2
        print('O valor da multiplicação é {}{}{}'.format(vermelho, multi, limpa))
        sleep(2)
    elif opcao == '3':
        maior = n1
        if n2 > maior:
            maior = n2
        print('O maior número é {}{}{}'.format(azul, maior, limpa))
        sleep(2)
    elif opcao == '4':
        n3 = int(input('Insira um número: '))
        sleep(.5)
        n4 = int(input('Isira mais um número: '))
        sleep(.5)
        n1 = n3
        n2 = n4
    elif opcao == '5':
        print('{}{}FINALIZANDO>>>{}'.format(sublinhado, vermelho, limpa))
        c = 5
        while c != 0:
            print(c)
            sleep(1)
            c -= 1

        continua = 5
