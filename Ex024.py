cidade = input('Digite o nome de uma cidaade: ')
trato = cidade.title()
climpa = trato.split()
verificarsanto = 'Santo' in climpa[0]
print(verificarsanto)
print(climpa[0])