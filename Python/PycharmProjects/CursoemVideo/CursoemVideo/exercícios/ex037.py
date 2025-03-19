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
print('Escolha um modo de conversão:\n'
      '{1}[1]{0} converte em {1}binário{0}\n'
      '{2}[2]{0} converte em {2}octal{0}\n'
      '{3}[3]{0} converte em {3}hexadecimal{0}'
      .format(limpa, verde, roxo, azul))
conversão = int(input('{1}Digite apenas o número da opção{0}: '.format(limpa, sublinhado)).strip())

if conversão == 1:
    print('{1}{3}{0} em {1}binário{0} é {1}{2}{4}{0}'.format(limpa,verde, sublinhado, num, bin(num)[2:]))
elif conversão == 2:
    print('{1}{3}{0} em {1}octal{0} é {1}{2}{4}{0}'.format(limpa, roxo, sublinhado, num, oct(num)[2:]))
elif conversão == 3:
    print('{1}{3}{0} em {1}hexadecimal{0} é {1}{2}{4}{0}'.format(limpa, azul, sublinhado, num, hex(num)[2:]))
else:
    print('{}{}{}ERRO{}'.format(vermelho, sublinhado, negrito, limpa))
