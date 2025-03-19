print('-=-' * 40)
print('É possível formar um triângulo?')
print('-=-' * 40)

l1 = float(input('Escreva o primeiro lado: '))
l2 = float(input('Escreva o segundo lado: '))
l3 = float(input('Escreva o terceiro lado: '))

if l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2:
    print('Forma um triângulo')
else:
    print('Não forma um triângulo')
