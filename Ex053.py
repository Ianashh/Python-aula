frase = input('Digite sua frase: ').strip().upper() # tiro o espaço inicial e final da frase e coloco-a em maiúsculas
separa = frase.split() # separa palavras da frase em listas
s = ('') # crio uma variável de str pra posterior soma

for c in separa[0:]: # faço o laço correr as letras dentro da lista de "separa" para poder invertê-las futuramente.
    s = s + c # "s" recebe a soma das letras de cada lista sem espaços
inv = s[::-1] # As letras geradas em "s" são invertidas.
if inv == s: # Aqui há uma simples comparação das posições das letras
    print('A frase {} é um palíndromo, \nou seja, \né igual lida de trás para frente!!'.format(frase))
else:
    print('Essa frase não é um palíndromo!')


