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

vaca = float(input('{}Qual o valor da casa? R${}'.format(azul, limpa)))
sal = float(input('{}Qual o seu salário? R${}'.format(roxo, limpa)))
temp = int(input('{}Em quantos anos você quer pagar? {}'.format(amarelo, limpa)))

parc = vaca / (temp * 12)

if parc <= sal * 0.3:
    print('O empréstimo foi {1}{2}APROVADO!{0} O valor da parcela será {3}R${4:.2f}{0}.'
          .format(limpa, sublinhado, verde, amarelo, parc))
else:
    print('O empréstimo foi {1}{2}NEGADO!{0} O valor da parcela {2}EXCEDE 30%{0} do seu salário,'
          ' sendo o valor da parcela {3}R${4:.2f}{0}'
          .format(limpa, sublinhado, vermelho, amarelo, parc))
