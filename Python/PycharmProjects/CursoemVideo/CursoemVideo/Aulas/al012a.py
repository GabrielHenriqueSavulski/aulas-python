nome = str(input('\033[4;1mQual o seu nome?\033[m ')).title()

if nome == 'Gabriel':
    print('\033[1;4;36mQue nome bonito!!!\033[m')
elif nome == 'Ana' or nome == 'Henrique' or nome == 'Miguel':
    print('Tenho um \033[4mparente com um nome igual ao \033[1mSEU!!\033[m')
else:
    print('\033[1;4mOK\033[m.')
print('Tenha um bom dia, \033[1;4m{}\033[m!'.format(nome))
