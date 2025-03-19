r = float(input('Quanto dinheiro você quer converter: R$'))
d = r / 5.05
e = r / 5.42
f = r / 5.58
g = r / 0.00068
y = r / 0.033
k = r / 16.40
print('Com R${:.2f} você pode comprar:\nUS${:.2f}'.format(r, d))
print('{:.2f} Euros'.format(e))
print('{:.2f} Francos Suíços'.format(f))
print('{:.2f} Guaranis Paraguaios'.format(g))
print('{:.2f} Yene Japonês'.format(y))
print('{:.2f} Dinar Kuaitiano'.format(k))
