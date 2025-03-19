from random import choice
print('{:=^20}'.format('DESAFIO 019'))
n1 = str(input('Primeiro aluno '))
n2 = str(input('Segundo aluno '))
n3 = str(input('Terceiro aluno '))
n4 = str(input('Quarto aluno '))
lista = [n1, n2, n3, n4]
esc = choice(lista)
print('O aluno escolhido foi {}'.format(esc))
