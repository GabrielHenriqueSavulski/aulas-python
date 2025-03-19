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

a1 = int(input('Qual o primeiro termo da PA? '))
razao = int(input('Qual a razão da PA? '))
n = 1
print('Por padrão são mostrados 10 termos.')
m = 0
mais = 10
while mais != 0:
    m += mais
    while n <= m:
        an = a1 + (n - 1) * razao
        if n == m:
            print(an)
        else:
            print(an, end=', ')
        n += 1
    mais = int(input('Quantos termos a mais você quer, ou 0 para sair: '))
