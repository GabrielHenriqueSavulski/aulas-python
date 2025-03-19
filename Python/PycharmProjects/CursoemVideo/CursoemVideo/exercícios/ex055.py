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

maior = 0
menor = 0

for c in range(1, 6):
    peso = float(input('Insira o peso da {}ª pessoa: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('A pessoa mais pesada têm {1}{4}Kg{0} e a mais leve tem {2}{3}Kg{0}.'
      .format(limpa, vermelho, azul, menor, maior))
