from random import shuffle
print('{:=^20}'.format('DESAFIO 020'))
a1 = input('1º aluno ')
a2 = input('2º aluno ')
a3 = input('3º aluno ')
a4 = input('4º aluno ')
lista = [a1, a2, a3, a4]
shuffle(lista)
print('Os a orde dos alunos escolhidos foi:')
print(lista)