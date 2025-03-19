print('{:=^21}'.format('DESAFIO 040'))

sublinhado = '\033[4m'
azul = '\033[34m'
amarelo = '\033[33m'
vermelho = '\033[31m'
limpa = '\033[m'

print('{}ESTE PROGRAMA CÁLCULA A MÉDIA BASEADO EM 4 BIMESTRES{}'.format(vermelho, limpa))

nota1 = float(input('Digite uma nota: '))
nota2 = float(input('Digite uma nota: '))
nota3 = float(input('Digite uma nota: '))
nota4 = float(input('Digite uma nota: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media > 7.0:
    print('{3}{0}APROVADO!{1}{0} Sua nota foi {2:.1f}{1}'
          .format(azul, limpa, media, sublinhado))
elif 5.0 < media <= 6.9:
    print('{0}{2}RECUPERAÇÃO!{1}{2} Preste mais atenção! Sua nota foi {3:.1f}{1}'
          .format(sublinhado, limpa, amarelo, media))
else:
    print('{1}{2}REPROVADO!{0}{2} Seu desempenho foi insuficiente, sua nota foi {3:.1f}{0}'
          .format(limpa, sublinhado, vermelho, media))
