limpa = '\033[m'
negrito = '\033[1m'
sublinhado = '\033[4m'
vermelho = '\033[31m'

print('Olá, bem vindo!')
val = float(input('Digite o valor do produto: R$'))
print('Qual meio de pagamento você deseja?\n'
      '[1] À vista, {1}dinheiro ou cheque{0}\n'
      '[2] À vista no {1}cartão{0}\n'
      '[3] parcelado no {1}cartão{0}'
      .format(limpa, vermelho))
modo = int(input('Digite apenas o número da opção desejada: '))

if modo == 1:
    desc = val * 0.9
    print('Pagando {1}à vista{0} no dinheiro ou cheque, o produto sai por {2}R${3:.2f}{0}'
          .format(limpa, sublinhado, vermelho, desc))
elif modo == 2:
    desc = val * 0.95
    print('Pagando {1}à vista{0} no cartão, o produto sai por {2}R${3:.2f}{0}'
          .format(limpa, sublinhado, vermelho, desc))
elif modo == 3:
    vezes = int(input('Em quantas vezes quer parcelar? '))
    if vezes == 2:
        parc = val / vezes
        print('Pagando parcelado em 2 vezes, {1}não há juros{0}, portanto custa {2}R${3:.2f}{0} por parcela.'
              .format(limpa, sublinhado, vermelho, parc))
    elif vezes > 2:
        juros = val * 1.2
        parc = juros / vezes
        print('Pagando parcelado em {1}{4}{0} vezes, {1}há juros de 20%{0},\n'
              'portanto custa {2}R${5:.2f}{0} por parcela, totalizando {2}R${3:.2f}{0}'
              .format(limpa, sublinhado, vermelho, juros, vezes, parc))
