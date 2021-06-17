n = 0
cont = 0

while n != 999:
    n = int(input('Digite um numero ou 999 para parar: '))
    cont += n
    print(f'O número escolhido foi {n} e a soma até agora é de {cont}')
    if n == 999:
        cont - cont - 999
        print(f'O programa foi encerrado e a soma até agora é de {cont}')