n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == -1:
        break
    s += n
print('A soma vale {}'.format(s))
