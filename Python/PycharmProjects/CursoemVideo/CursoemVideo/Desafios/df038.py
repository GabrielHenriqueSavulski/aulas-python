print('{:=^21}'.format('DESAFIO 038'))

vermelho = '\033[31m'
amarelo = '\033[33m'
limpa = '\033[m'
n1 = int(input('{}Digite um número:{} '.format(vermelho, limpa)))
n2 = int(input('{}Digite outro número:{} '.format(amarelo, limpa)))

if n1 > n2:
    print('{2}{3}{1} é maior que {0}{4}{1}'.format(amarelo, limpa, vermelho, n1, n2))
elif n2 > n1:
    print('{0}{4}{1} é maior que {2}{3}{1}'.format(amarelo, limpa, vermelho, n1, n2))
else:
    print('{2}{3}{1} é igual a {0}{4}{1}'.format(amarelo, limpa, vermelho, n1, n2))
