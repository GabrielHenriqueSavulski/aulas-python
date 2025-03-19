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

print('VAMOS FAZER UM TRIÂNGULO')

l1 = float(input('Digite um lado: '))
l2 = float(input('Digite um lado: '))
l3 = float(input('Digite um lado: '))

forma = 's'

if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    forma = '{}podem formar um triângulo{}'.format(sublinhado, limpa)
    tipo = 's'
    if l1 == l2 != l3 or l1 == l3 != l2 or l2 == l3 != l1:
        tipo = '{}ISÓCELES{}'.format(vermelho, limpa)
    elif l1 == l2 == l3:
        tipo = '{}EQUILÁTERO{}'.format(verde, limpa)
    elif l1 != l2 != l3 != l1:
        tipo = '{}ESCALENO{}'.format(roxo, limpa)
    print('O lados {} do tipo {}'.format(forma, tipo))
else:
    forma = '{}NÃO podem formar um triângulo{}'.format(sublinhado, limpa)
    print('Os lados {}'.format(forma))