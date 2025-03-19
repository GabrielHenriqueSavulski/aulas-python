galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 4):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 18:
        print(f'\n {p[0]} é maior de idade.')
        totmai += 1

    else:
        print(f'\n {p[0]} é menor de idade.')
        totmen += 1

print(f"\n Nessa família há {totmai} maiores de idade "
      f"\n {totmen} menor de idade")
