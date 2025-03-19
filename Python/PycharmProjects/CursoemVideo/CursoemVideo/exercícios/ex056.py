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

homem = ''
velho = 0
menina = 0
somaIdades = 0

for c in range(1, 5):
    print('----- {}ª PESSOA -----'.format(c))
    nome = str(input('Qual o seu nome? ')).strip().title()
    idade = int(input('Qual sua idade? '))
    sexo = str(input('Qual seu sexo, responda M ou F: ')).strip().upper()
    somaIdades += idade
    if sexo == 'F' and idade <= 20:
        menina += 1
    if sexo == 'M':
        if idade > velho:
            velho = idade
            homem = nome

media = somaIdades / 4

print('A média das idades é {:.0f}'.format(media))

if velho != 0:
    print('O homem mais velho tem {1}{2}{0} anos e se chama {1}{3}{0}'.format(limpa, azul, velho, homem))
else:
    print('{}NÃO HÁ HOMENS NO GRUPO{}'.format(vermelho, limpa))

if menina == 1:
    print('Existe {1}{2}{0} menina com {1}20 anos{0} ou menos'
          .format(limpa, roxo, menina))
else:
    print('Existem {1}{2}{0} meninas com {1}20 anos{0} ou menos'
          .format(limpa, roxo, menina))
