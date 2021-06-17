x = int(input('Digite o 1º número: '))
y = int(input('Digite o 2º número: '))
z = int(input('Digite o 3º número: '))

if x > y:
    max = x
else:
    max = y
if max < z:
    max = z

if x < y:
    mini = x
else:
    mini = y
if mini > z:
    mini = z

print('\nO maior numero é {}.\n'.format(max))
print('O menor numero é {}.'.format(mini))

print('_____________FIM_____________')
