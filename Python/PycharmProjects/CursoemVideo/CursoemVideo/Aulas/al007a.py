n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
sub = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
rd = n1 % n2
e = n1 ** n2
r = n1 ** (1/n2)
print('A soma é {} e a subtração é {}'.format(s, sub))
print('O produto é {}, a divisão é {:.4f}, a divisão inteira é {} e o resto da divisão inteira é {}'.format(m, d, di, rd))
print('A potencia do primeiro pelo segundo é {} e a rais na mesma ordem é {:.4f}'.format(e, r))
