print('{:=^21}'.format('DESAFIO 036'))

vaca = float(input('\033[31mQual o valor da casa?\033[m '))
sal = float(input('\033[32mQuanto você recebe?\033[m '))
anos = int(input('\033[33mEm quantos anos você quer parcelar?\033[m '))

par = vaca / (anos * 12)

if par <= (sal * 0.3):
    print('\033[1mOK\033[m, \033[1;4mempréstimo concedido!\033[m')
else:
    print('\033[1;4;31mNEGADO!\033[m O seu salário não dá conta.')
