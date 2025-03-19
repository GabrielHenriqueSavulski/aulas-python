nome = str(input('Qual é seu nome? ')).strip().title()
if nome == 'Gabriel':
    print('Que nome lindo você tem!')
else:
    print('Prazer em te conhecer!')
print('Bom dia, {}!'.format(nome))
