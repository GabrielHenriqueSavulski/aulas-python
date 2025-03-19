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

n1 = int(input('{}Digite um número: {}'.format(ciano, limpa)))
n2 = int(input('{}Digite outro valor: {}'.format(amarelo, limpa)))

if n1 > n2:
    print('{}O primeiro número é maior.{}'.format(verde, limpa))
elif n2 > n1:
    print('{}O segundo número é maior.{}'.format(azul, limpa))
else:
    print('{}Os dois números são iguais.{}'.format(vermelho, limpa))
