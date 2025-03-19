print('{:=^21}'.format('DESAFIO 031'))

dist = float(input('Quantos quilometros terão sua viagem?(Pode usar números como 3.5Km) '))
if dist <= 200:
    val = dist * 0.5
    print('O valor da passagem de uma viagem de {}Km, será R${:.2f}'.format(dist, val))
else:
    val = dist * 0.45
    print('O valor da passagem de uma viagem de {}Km, será R${:.2f}'.format(dist, val))
