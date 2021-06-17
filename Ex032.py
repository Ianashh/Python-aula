ano = int(input('Qual ano deseja testar: '))
bissexto = ano%4 #and % 100 != 0 or ano % 400 == 0

if bissexto == 0:
    print('\nO ano de {} é bissexto!!\n'.format(ano))
else:
    print('\nO ano de {} não é bissexto!!\n'.format(ano))

print('\nObrigado por utilizar a TestAno.com !!!')