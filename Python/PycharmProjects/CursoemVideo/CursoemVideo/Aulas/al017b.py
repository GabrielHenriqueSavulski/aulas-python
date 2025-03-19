val = []
val.append(5)
val.append(7)
val.append(6)
val.append(58)
val.append(56)

for v in val:
    print(f'{v}...', end='')
print('')

for c, v in enumerate(val):
    print(f'Na posição {c} eu achei o valor {v}')

print('Nova Lista')

num = []
for cont in range(0, 10):
    num.append(int(input('Digite um valor: ')))

for c, v in enumerate(num):
    print(f'Na posição {c} eu achei o valor {v}')
