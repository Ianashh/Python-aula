# Passo 1: importar libs e criar variáveis
import datetime # Necessário para puxar o ano atual
hoje = datetime.datetime.now().year # Puxa o ano atual
ma = 0 # Variável criada para soma de maiores
me = 0 # Variável criada para soma de menores

# Passo 2: coletar ano de nascimento e transformar em idade atual.
for c in range(0,2):
        idade = int(input('Qual seu ano de nascimento: ')) # Necessário 4 digitos
        idade = hoje-idade # Faz o calculo da idade atual
        print( f'{idade} anos.')

# Passo 3: Checar se a idade é maior ou igual que 21 anos
        if idade >= 21:

# Passo 4: Se for maior, armazena uma contagem em "ma".
            ma = ma + 1
            if ma == 1 :
                print(f'\n{ma} pessoa maior de idade.')
            else:
                print(f'\n{ma} pessoas maiores de idade.')

# Passo 5: Se for menor, armazena uma contagem em "me".
        else:
            me = me + 1
            if me == 1:
                print(f'\n{me} pessoa menor de idade.')
            else:
                print(f'\n{me} pessoas menores de idade.')

print(f'\n{ma} maioridade(s).\n{me} menoridade(s).')