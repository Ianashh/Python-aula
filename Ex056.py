#media de idade
#homem mais velho
#mulheres com menos de 20 anos


# Passo 1: Criar variáveis e importar libs

from statistics import mean #pegando a média
from time import sleep
nomem , nomef = [],[] #separando nomes em listas por sexo
idadem , idadef = [],[] #separando idades em listas por sexo
sexo_marculino , sexo_feminino = [],[] #separando listas por sexo
cont = 0 # Atribuindo variável de contagem

# Passo 2: Inputs das informações necessárias

for i in range(0,4): # Estabelecendo numeros de laços e separação das listas
    sexo = (input('\nDigite (M) para Masculino ou (F) para Feminino: ')).capitalize()
    sleep(0.5)
    if sexo == 'M':
        sexo_marculino.append('M')
    elif sexo == 'F':
        sexo_feminino.append('F')
    else:
        print('Você digitou um valor inválido.\nPor favor, reinicie o programa!!\n')
        break
    if sexo == 'M':
        nomem.append (input('\nDigite seu nome: ').strip().title())
    else:
        nomef.append(input('\nDigite seu nome: ').strip().title())
    if sexo == 'M':
        idadem.append(int(input('\nDigite sua idade: ')))
    else:
        idadef.append(int(input('\nDigite sua idade: ')))

# Passo 3: Criar variáveis para resolução do 2º problema (nome do homem mais velho)

hmax = max(idadem) # atribuir idade máxima a uma variável
hmaxp = idadem.index(hmax) # ************ Localiza a posição na lista de acordo com o parametro"()" ******************

# Passo 4: Criar variáveis para resolução do 3º problema (mulheres abaixo dos 20 anos)

fmen = 0
fm = []
for f in idadef:
    if f <= 20:
#       print(f)
#       print(fmen)
       f = fmen + 1
       fm.append(f)
# Passo 5: Imprimir as informações solicitadas

print(f'\nA média das idades é {mean(idadem+idadef):.2f}.' # Chamo a função média da LIB statistcs
      f'\nO homen mais velho é {nomem[hmaxp]}' # Chamo o format da lista "nomem" passando o parametro da hmaxp 
      # achado atravez do index
      f'\nA quantidade de mulheres abaixo de 20 anos é de {len(fm)}')

#print(fm)

#print(f'{nomem}\n{nomef}\n{idadem}\n{idadef}\n{sexo_marculino}\n{sexo_feminino}')
#print(hmaxp)
#print(hmax)



#hmax = max(idadem) #atribuir idade máxima a uma variável """ex linha 28"""
#for hmax in idadem: ex linha 29
#    while idadem != hmax:
#        print('.')
#        cont += 1
#print(cont)
