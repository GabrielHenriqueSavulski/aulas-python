print('{:=^21}'.format('DESAFIO 045'))

from random import choice

limpa = '\033[m'
vermelho = '\033[1;30;4;41m'
azul = '\033[1;4;30;44m'
roxo = '\033[1;4;30;45m'

print('{}{:=^20}{}'.format(roxo, 'JOKEMPÔ!', limpa))
print('Você é o {1}azul{0} e eu sou o {2}vermelho{0}'.format(limpa, azul, vermelho))
jogada = str(input('Digite pedra, papel ou tesoura: ')).lower().strip()
lista = ['pedra', 'papel', 'tesoura']
escolha = choice(lista)
estado = 'ERRO'
if jogada == 'pedra' and escolha == 'tesoura' or jogada == 'papel' and escolha == 'pedra' or jogada == 'tesoura' and escolha == 'papel':
    estado = '{}VITÓRIA DO AZUL!!{}'.format(azul, limpa)
elif escolha == 'pedra' and jogada == 'tesoura' or escolha == 'papel' and jogada == 'pedra' or escolha == 'tesoura' and jogada == 'papel':
    estado = '{}VITÓRIA DO VERMELHO!!{}'.format(vermelho, limpa)
elif jogada == escolha:
    estado = '{}EMPATE.{}'.format(roxo, limpa)
else:
    print('Há algo de errado.')
print('{:=^40}'.format(estado))