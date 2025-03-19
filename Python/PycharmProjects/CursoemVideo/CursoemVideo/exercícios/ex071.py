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

print('=' * 30)
print('BANCO SAVULSKI')
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
ced = 50
TotCed = 0
while True:
    if total >= ced:
        total -= ced
        TotCed += 1
    else:
        if TotCed > 0:
            print(f'Total de {TotCed} cédulas de R${ced:.2f}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        TotCed = 0
        if total == 0:
            break
print('=' * 30)
print('Volte Sempre!')