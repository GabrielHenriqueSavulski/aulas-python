from random import randint
from time import sleep
num = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar ......')
print('-=-' * 20)
resp = int(input('Em que número pensei? '))
print('PROCESSANDO....')
sleep(2)
if num == resp:
    print('Ahhh... Você ganhou! O número era {}.'.format(num))
else:
    print('Ha! Eu ganhei! O número era {}.'.format(num))
