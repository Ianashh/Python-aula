nome = input('Digite seu nome: ').strip()
tratonome = nome.title()
divname = tratonome.split()
print(divname)

print('Seu primeiro nome é {} e seu último é {}.'.format(divname[0],divname[len(divname)-1]))
print(len(divname))
print(type(divname))