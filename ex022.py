nome = str(input('Qual seu nome? ').strip())
print(nome.upper())
print(nome.lower())
print('Esse nome possui {} letras.'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome possui {} letras'.format(nome.find(' ')))
print(nome)