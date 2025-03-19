print('{:=^21}'.format('DESAFIO 053'))

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

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
palindromo = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

if inverso == junto:
    palindromo = 'é um palíndromo'
else:
    palindromo = 'Não é palíndromo'

print('A frase {1}{4}{0} {2}{5}{0}, pois forma a frase {3}{6}{0}'.format(limpa, verde, azul, vermelho, junto, palindromo, inverso))
