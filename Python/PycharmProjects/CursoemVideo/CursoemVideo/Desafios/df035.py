print('{:=^21}'.format('DESAFIO 035'))

l1 = int(input('Digite um lado: '))
l2 = int(input('Digite um outro lado: '))
l3 = int(input('Digite um último lado: '))

if l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2:
    print('É possível formar um triângulo')
else:
    print('Não é possível formar um triângulo')
