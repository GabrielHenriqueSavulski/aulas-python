print('{:=^21}'.format('DESAFIO 071'))

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
print('BANCO SAVINT')
print('-' * 40)
n = int(input('Quanto você quer sacar? '))
c50 = n // 50
r1 = n % 50
c20 = r1 // 20
r2 = r1 % 20
c10 = r2 // 10
r3 = r2 % 10
c1 = r3
print(f'Você receberá {azul}{c50}{limpa} cédulas de R$50,00,'
      f' {azul}{c20}{limpa} cédulas de R$20,00, {azul}{c10}{limpa} cédulas de R$10,00 e '
      f'{azul}{c1}{limpa} cédulas de R$1,00,')
