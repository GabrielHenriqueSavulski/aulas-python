lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim'
print('CARDÁPIO')

for c in range(0, len(lanche)):
    print(f'{c + 1} - {lanche[c]}')
print('\n')
for pos, comida in enumerate(lanche):
    print(f'{pos + 1} - {comida}')
print('\n')
for comida in lanche:
    print(f'Eu vou comer {comida}')
