dist = float(input('Qual a distância em Km da sua viajem? (Ex: 300.5) '))

if dist <= 200:
    val = dist * 0.5
else:
    val = dist * 0.45
print('Para {}km de viagem a passagem do ônibus será de R${:.2f}'.format(dist, val))
