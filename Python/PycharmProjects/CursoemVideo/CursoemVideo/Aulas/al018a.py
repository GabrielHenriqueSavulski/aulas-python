teste = list()
teste.append("Gabriel")
teste.append(20)
galera = list()
galera.append(teste[:])
teste[0] = 'Miguel'
teste[1] = 10
galera.append(teste[:])
print(galera)
