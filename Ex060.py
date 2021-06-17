n = int(input('Digite um número para descobrir seu fatorial: '))
cont = 0
num = n
num2 = n
while num != 0:
    n = n*(-num)
    cont = cont+n
    num -= 1


print(f'O número escolhido foi o {num2} e seu valor fatorial é {cont}')