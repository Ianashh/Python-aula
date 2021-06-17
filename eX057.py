# Passo 1: Criar variável que contera a str já formatada

n = input('Selecione [M ou F]: ').strip().title()

# Passo 2: Cria o loop com 2 condições e formata a str recebida para
# "strip" e "title" tirando espaços e deixando a primeira letra de cada palavra maiúscula.

while n != 'M' and n != 'F':
        n = input(f'\nVocê digitou {n}.\nO valor {n} não corresponde a um valor válido.\nPor favor, digite novamente, [M/F]: ').strip().title()

# Passo 3: Print fim

print('\nFIM')

