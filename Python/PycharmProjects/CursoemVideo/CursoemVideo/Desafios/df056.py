print('{:=^21}'.format('DESAFIO 056'))

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

todasIdades = 0
mulheres = 0
genero = ''
nome = ''
idade = 0

for c in range(0, 4):
    sexo = str(input('Qual seu sexo, {1}M{0} ou {2}F{0}? '.format(limpa, azul, roxo))).strip().lower()
    name = str(input('Qual seu nome? ')).strip().title()
    age = int(input('Qual sua idade? '))
    todasIdades += age
    if sexo == 'm' and age > idade:
        idade = age
        nome = name
    if sexo == 'f' and age < 21:
        mulheres += 1

mediaIdades = todasIdades / 4

print('A média das idades do grupo é {}{}{} anos'.format(azul, mediaIdades, limpa))
print('O homem mais velho é {1}{2}{0}, com a idade de {1}{3}{0}'.format(limpa, verde, nome, idade))
print('Tem {}{}{} mulheres com menos de 21 anos'.format(roxo, mulheres, limpa))
