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
fpreto = '\033[40m' # 40 para cor do fundo
fvermelho = '\033[41:30m'
fverde = '\033[42:30m'
famarelo ='\033[43:30m'

print('Escolha  o modelo de notas:\n'
      '{1}[1]{0} 4 bimestres;\n'
      '{2}[2]{0} 2 bimestres;\n'
      '{3}[3]{0} 3 trimestres;\n'
      '{4}[4]{0} 2 semestres;\n'
      '{5}[5]{0} 10 notas.'
      .format(limpa, vermelho, verde, amarelo, azul, roxo))
modelo = int(input('{}Digite apenas o número da opção desejada{}: '.format(sublinhado, limpa)))

if modelo == 1:
    n1 = float(input('{}1ºNota: {}'.format(vermelho, limpa)))
    n2 = float(input('{}2ºNota: {}'.format(verde, limpa)))
    n3 = float(input('{}3ºNota: {}'.format(amarelo, limpa)))
    n4 = float(input('{}4ºNota: {}'.format(azul, limpa)))
    media = (n1 + n2 + n3 + n4) / 4
    if media >= 7:
        print('{1}APROVADO!{0} Sua média foi {1}{2:.1f}{0}'.format(limpa, azul, media))
    elif 5 < media <= 6.9:
        print('{1}RECUPERAÇÃO!{0} Estude mais sua média foi {1}{2:.1f}{0}'.format(limpa, amarelo, media))
    else:
        print('{1}{2}{3}REPROVADO{0} A sua média foi {1}{2}{3}{4:.1f}{0},\n'
              'você precisa {1}ESTUDAR MUITO{0}.'.format(limpa, sublinhado, negrito, vermelho, media))
elif modelo == 2 or modelo == 4:
    n1 = float(input('{}1ºNota: {}'.format(vermelho, limpa)))
    n2 = float(input('{}2ºNota: {}'.format(verde, limpa)))
    media = (n1 + n2) / 2
    if media >= 7:
        print('{1}APROVADO!{0} Sua média foi {1}{2:.1f}{0}'.format(limpa, azul, media))
    elif 5 < media <= 6.9:
        print('{1}RECUPERAÇÃO!{0} Estude mais sua média foi {1}{2:.1f}{0}'.format(limpa, amarelo, media))
    else:
        print('{1}{2}{3}REPROVADO{0} A sua média foi {1}{2}{3}{4:.1f}{0},\n'
              'você precisa {1}ESTUDAR MUITO{0}.'.format(limpa, sublinhado, negrito, vermelho, media))
elif modelo == 3:
    n1 = float(input('{}1ºNota: {}'.format(vermelho, limpa)))
    n2 = float(input('{}2ºNota: {}'.format(verde, limpa)))
    n3 = float(input('{}3ºNota: {}'.format(amarelo, limpa)))
    media = (n1 + n2 + n3) / 3
    if media >= 7:
        print('{1}APROVADO!{0} Sua média foi {1}{2:.1f}{0}'.format(limpa, azul, media))
    elif 5 < media <= 6.9:
        print('{1}RECUPERAÇÃO!{0} Estude mais sua média foi {1}{2:.1f}{0}'.format(limpa, amarelo, media))
    else:
        print('{1}{2}{3}REPROVADO{0} A sua média foi {1}{2}{3}{4:.1f}{0},\n'
              'você precisa {1}ESTUDAR MUITO{0}.'.format(limpa, sublinhado, negrito, vermelho, media))
elif modelo == 5:
    n1 = float(input('{}1ºNota: {}'.format(vermelho, limpa)))
    n2 = float(input('{}2ºNota: {}'.format(verde, limpa)))
    n3 = float(input('{}3ºNota: {}'.format(amarelo, limpa)))
    n4 = float(input('{}4ºNota: {}'.format(azul, limpa)))
    n5 = float(input('{}5ºNota: {}'.format(roxo, limpa)))
    n6 = float(input('{}6ºNota: {}'.format(ciano, limpa)))
    n7 = float(input('{}7ºNota: {}'.format(fpreto, limpa)))
    n8 = float(input('{}8ºNota: {}'.format(fvermelho, limpa)))
    n9 = float(input('{}9ºNota: {}'.format(fverde, limpa)))
    n10 = float(input('{}10ºNota: {}'.format(famarelo, limpa)))
    media = (n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10) / 10
    if media >= 7:
        print('{1}APROVADO!{0} Sua média foi {1}{2:.1f}{0}'.format(limpa, azul, media))
    elif 5 < media <= 6.9:
        print('{1}RECUPERAÇÃO!{0} Estude mais sua média foi {1}{2:.1f}{0}'.format(limpa, amarelo, media))
    else:
        print('{1}{2}{3}REPROVADO{0} A sua média foi {1}{2}{3}{4:.1f}{0},\n'
              'você precisa {1}ESTUDAR MUITO{0}.'.format(limpa, sublinhado, negrito, vermelho, media))
else:
    print('{}INVÁLIDO{}'.format(vermelho, limpa))
