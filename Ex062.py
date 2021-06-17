# Passo 1: Fibonacci = 1º termo somado ao termo anterior dele mesmo.
# O resultado é somado da conta anterior somasse ao primeiro termo da conta anterior.
print('\n***SEQUÊNCIA DE FIBONACCI***\n')
fim = int(input('Digite em que termo deseja parar: '))
ft = 0
sd = 1
termo = ''
print(f'\n{ft} -> {sd} -> ',end = '')
while fim != 0:
    fim -= 1
    termo = ft +sd
    ft = sd
    sd = termo
    print(termo,end = '')
    print(' -> ' if fim != 0 else "\n",end = '')




