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

print('-' * 40)
print('LOJA SUPER BARATÃO')
print('-' * 40)

soma = barato = caro = c = 0
nome = ''
while True:
    produto = str(input('Qual o nome do produto? '))
    preco = float(input('Qual o preço do produto? R$'))
    soma += preco
    if preco >= 1000:
        caro += 1
    if c == 0:
        nome = produto
        barato = preco
        c += 1
    else:
        if preco < barato:
            nome = produto
            barato = preco
    print('-' * 40)
    continua = str(input('Quer continuar? [S/N]: ')).strip()
    while continua not in 'SsNn':
        continua = str(input(f'{vermelho}Tente novamente{limpa}. Quer continuar? [S/N]: ')).strip()
    print('-' * 40)
    if continua in 'Nn':
        break
print(f'O total gasto foi {vermelho}R${soma:.2f}{limpa},\n'
      f'O produto mais barato foi {azul}{nome}{limpa} por {azul}R${barato:.2f}{limpa}\n'
      f'e {amarelo}{caro}{limpa} produtos custaram mais de R$1000,00')
