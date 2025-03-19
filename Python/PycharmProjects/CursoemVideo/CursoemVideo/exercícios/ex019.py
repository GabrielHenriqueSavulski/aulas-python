from random import choice
a1 = input('1º aluno ')
a2 = input('2º aluno ')
a3 = input('3º aluno ')
a4 = input('4º aluno ')
l = [a1, a2, a3, a4]
e = choice(l)
print('O aluno escolhido foi {}'.format(e))
