print('{:=^21}'.format('DESAFIO 037'))

val = float(input('Qual o valor do produto?Escreva assim 3.14: '))
print('Como gostaria de pagar? Opções:'
      '\n 1 - à vista, dinheiro ou cheque.'
      '\n 2 - à vista no cartão.'
      '\n 3 - paracelado')
opcao = int(input('Digite o número da opção de pagamento: '))

if opcao == 1:
    desc = val * 0.9
    print('Nessa forma de pagamento o valor a ser pago recebe 10% de desconto,\n'
          'sendo assim, o valor a ser pago é R${:.2f}'.format(desc))
elif opcao == 2:
    desc = val * 0.95
    print('Nessa forma de pagamento o valor a ser pago recebe 5% de desconto,\n'
          'sendo assim, o valor a ser pago é R${:.2f}'.format(desc))
elif opcao == 3:
    parcelas = int(input('Em quantas vezes você quer parcelar? '))
    if parcelas == 2:
        parc = val / 2
        print('Nessa forma de pagamento o valor a ser pago é R${:.2f} por parcela, sem juros'.format(parc))
    elif parcelas >= 3:
        parc = (val * 1.2) / parcelas
        print('Nessa forma de pagamento o valor a ser pago é R${:.2f} por parcela, com juros de 20%'.format(parc))
