print('{:=^21}'.format('DESAFIO 057'))

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

sexo = str(input('Qual seu sexo, [M/F]? ')).strip().upper()

while sexo not in 'M''F':
    sexo = str(input('{}Errado, tente novamente, M ou F?{} '.format(vermelho, limpa))).strip().upper()
genero = ''
if sexo == 'M':
    genero = 'Homem'
if sexo == 'F':
    genero = 'Mulher'

print('Você é {}'.format(genero))
