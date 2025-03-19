palavra = str(input('Digite algo: ')).strip().upper()
print('Existem {} letras "A" nessa frase'.format(palavra.count('A')))
print('A primerira letra "a" aparece na {}° posição'.format(palavra.find('A') + 1))
print('A última letra "A" aparece na {}° posição'.format(palavra.rfind('A') + 1))
