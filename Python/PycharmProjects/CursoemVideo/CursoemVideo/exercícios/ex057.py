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

sexo = str(input('Qual seu sexo? M ou F ')).strip().upper()

while sexo not in 'MF':
    sexo = str(input('{}Valor errado, digite novamente. {}'.format(vermelho, limpa))).strip().upper()

escreve = ''
if sexo == 'M':
    escreve = '{}masculino{}'.format(azul, limpa)
elif sexo == 'F':
    escreve = '{}feminino{}'.format(roxo, limpa)

print('Sexo {} registrado'.format(escreve))
