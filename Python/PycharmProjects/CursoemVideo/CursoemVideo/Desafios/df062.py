print('{:=^21}'.format('DESAFIO 062'))

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
print('{}CALCULADORA DE P.A.{}'.format(verde, limpa))
sleep(.5)
continuar = 1
while continuar != 7:

    print('\nO que deseja fazer?\n'
          '{1}[1]{0} Mostrar uma quantidade de termos\n'
          '{1}[2]{0} Somar uma quantidade de termos\n'
          '{1}[3]{0} Achar um termo An\n'
          '{1}[4]{0} Achar o primeiro termo\n'
          '{1}[5]{0} Achar a razão\n'
          '{1}[6]{0} Achar a posição de um termo, "N"\n'
          '{1}[7]{0} Sair'
          .format(limpa, azul))
    sleep(.5)
    opção = int(input('Digite o número da opção desejada: '))
    sleep(.5)
    if opção == 1:
        print('\nPara ver uma quantidade de termos {}você precisa ter conhecimento{} dos seguintes dados:'
              '\nA1 e razão.'
              .format(vermelho, limpa))
        sleep(.5)
        print('{}Por padrão aparecem os dez primeiros termos:{}'.format(verde, limpa))
        sleep(.5)
        n = 1
        a1 = int(input('Qual o primeiro termo da P.A.? '))
        sleep(.5)
        razao = int(input('Qual a razão da P.A.? '))
        sleep(.5)
        print('Os termos da P.A. do a1 até o a10 são:')
        sleep(.5)

        while n <= 10:
            an = a1 + (n - 1) * razao
            print(an, end=' ')
            n += 1
        sleep(.5)
        print('\n{1}{2}Deseja ver mais termos?{0}'.format(limpa, sublinhado, vermelho))
        resp1 = str(input('Responda [S/N]: ')).strip().upper()
        sleep(.5)

        if resp1 == 'S':
            m = int(input('Quantos termos deseja ver no total? '))
            n =1

            while n <= m:
                an = a1 + (n - 1) * razao
                print(an, end=' ')
                n += 1
        sleep(.5)
    elif opção == 2:
        print('\nPara somar {}você precisa ter conhecimento{} dos seguintes dados:'
              '\nA1, An e n.'
              .format(vermelho, limpa))
        sleep(.5)
        a1 = int(input('Qual o primeiro termo da P.A.? '))
        sleep(.5)
        an = int(input('Qual o ultimo termo desejado? '))
        sleep(.5)
        n = int(input('Qual a posição do último número? '))
        sleep(.5)
        Sn = ((a1 + an) * n) / 2
        print('A soma dos {1}{2}{0} primeiros termos da P.A. é {1}{3}{0}'.format(limpa, azul, n, Sn))
        sleep(.5)
    elif opção == 3:
        print('\nPara achar An {}você precisa ter conhecimento{} dos seguintes dados:'
              '\nA1, razão e n.'
              .format(vermelho, limpa))
        sleep(.5)
        a1 = int(input('Qual o primeiro termo da P.A.? '))
        sleep(.5)
        razao = int(input('Qual a razão da P.A.? '))
        sleep(.5)
        n = int(input('Qual a posição do último número? '))
        sleep(.5)
        an = a1 + (n - 1) * razao
        print('O termo A{2} dessa P.A. é {1}{3}{0}'.format(limpa, azul, n, an))
        sleep(.5)
    elif opção == 4:
        print('\nPara achar A1 {}você precisa ter conhecimento{} dos seguintes dados:'
              '\nAn (qualquer), razão e n (do An).'
              .format(vermelho, limpa))
        sleep(.5)
        an = int(input('Qual o termo conhecido? '))
        sleep(.5)
        razao = int(input('Qual a razão da P.A.? '))
        sleep(.5)
        n = int(input('Qual a posição do termo conhecido? '))
        sleep(.5)
        x = (n - 1) * razao
        a1 = an - x
        print('O valor do primeiro termo da P.A. é {}{}{}'.format(azul, a1, limpa))
        sleep(.5)
    elif opção == 5:
        print('\nPara achar a razão {}você precisa ter conhecimento{} dos seguintes dados:'
              '\nAn (qualquer), A1 e n (do An).'
              .format(vermelho, limpa))
        sleep(.5)
        a1 = int(input('Qual o primeiro termo da P.A.? '))
        sleep(.5)
        an = int(input('Qual o termo conhecido? '))
        sleep(.5)
        n = int(input('Qual a posição do termo conhecido? '))
        sleep(.5)
        razao = (an - a1) / (n - 1)
        print('A razão dessa P.A. é {}{}{}'.format(azul, razao, limpa))
        sleep(.5)
    elif opção == 6:
        print('\nPara achar a posição de um termo {}você precisa ter conhecimento{} dos seguintes dados:'
              '\nAn (qualquer), A1 e razão.'
              .format(vermelho, limpa))
        sleep(.5)
        a1 = int(input('Qual o primeiro termo da P.A.? '))
        sleep(.5)
        an = int(input('Qual o termo conhecido? '))
        sleep(.5)
        razao = int(input('Qual a razão da P.A.? '))
        sleep(.5)
        n = ((an - a1) / razao) + 1
        print('A posição do termo conhecido nessa P.A. é {}{}{}'.format(azul, n, limpa))
        sleep(.5)
    elif opção == 7:
        continuar = 7
