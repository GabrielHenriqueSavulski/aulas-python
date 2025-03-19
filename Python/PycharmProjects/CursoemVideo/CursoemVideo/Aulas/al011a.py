print('\033[4;37;43mOlá mundo!\033[m')
print('\033[7mOlá mundo!\033[m')
nome = 'Gabriel'
print('Olá, meu nome é {}{}{}'.format('\033[1;31m', nome, '\033[m'))
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7m'}
print('{0}Olá, Mundo!{1}{2}Meu nome é {1}{3}{4}{1}!!!'
      .format(cores['azul'],
              cores['limpa'],
              cores['amarelo'],
              cores['pretoebranco'],
              nome))
