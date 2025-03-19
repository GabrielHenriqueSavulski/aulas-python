Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print("Estou aprendo Python!")
Estou aprendo Python!
print('olá, mundo!')
olá, mundo!
print(olá, mundo!)
SyntaxError: invalid syntax
print(7+4)
11
print('7'+'4')
74
7+4
11
'7'+'4'
'74'
print('Olá' + 5)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print('Olá' + 5)
TypeError: can only concatenate str (not "int") to str
print('Olá', 5)
Olá 5
nome='Gabriel'
idade=20
peso=95
print(nome, idade, peso)
Gabriel 20 95
print(nome + idade + peso)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print(nome + idade + peso)
TypeError: can only concatenate str (not "int") to str
>>> nome = input('Qual seu nome?')
Qual seu nome? Gabriel
>>> idade = input('Qual sua idade?')
Qual sua idade?20
>>> peso = input('Qual seu peso?')
Qual seu peso?94
>>> print('Seu nome é', nome,', sua idade é', idade, 'e seu peso é', peso)
Seu nome é  Gabriel , sua idade é 20 e seu peso é 94
>>> nome = input('Qual seu nome?')
Qual seu nome? Setsuna
>>> idade = input('Qual sua idade?')
Qual sua idade? 23
>>> peso = input('Qual seu peso?')
Qual seu peso? 57
>>> print(nome, idade, peso)
 Setsuna  23  57
