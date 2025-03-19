d = int(input('Por quantos dia o carro foi alugado? '))
km = int(input('Quantos quilometros o carro andou? '))
c = d * 60 + km * 0.15
print('Sabendo que a diária do carro é de R$60,00 e o custo do km rodado é R$0.15'
      '\ne que andou por {} dia(s) e rodou {}km, o valor total foi de R${:.2f}'.format(d, km, c))
