a = [1, 2, 3, 4]
b = a
b[2] = 8
c = b[:]
c[2] = 9
print(f'lista A: {a}')
print(f'lista B: {b}')
print(f'lista B: {c}')