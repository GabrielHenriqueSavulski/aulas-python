print('{:=^21}'.format('DESAFIO 037'))

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

num = int(input('Digite um número inteiro: ').strip())

modo = int(input('{4}Escolha uma das bases para conversão:\n{0}'
                 '{1}[1]{0} para transformar em {1}binário;\n{0}'
                 '{2}[2]{0} para tansformar em {2}octal;\n{0}'
                 '{3}[3]{0} para transformar em {3}hexadecimal.{0}\n'
                 '{5}Digite aqui apenas o número{0}: '
                 .format(limpa, verde, vermelho, azul, negrito, sublinhado)).strip())

if modo == 1:
    print('{1}{3}{0} em {1}binário{0} é {1}{2}{4}{0}'.format(limpa, verde, sublinhado, num, bin(num)[2:]))
elif modo == 2:
    print('{1}{3}{0} em {1}octal{0} é {1}{2}{4}{0}'.format(limpa, vermelho, sublinhado, num, oct(num)[2:]))
elif modo == 3:
    print('{1}{3}{0} em {1}hexadecimal{0} é {1}{2}{4}{0}'.format(limpa, azul, sublinhado,num, hex(num)[2:]))
else:
    print('{}{}{}ERRO{}'.format(vermelho, sublinhado, negrito, limpa))
