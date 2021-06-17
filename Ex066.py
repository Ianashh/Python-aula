n = soma = cont = 0
while n != 999:
    n = int(input('Digite um numero ou 999 para parar: '))
    if n == 999:
        break
    cont += 1
    soma += n

print(f'O programa foi encerrado e a soma dos {cont} valores digitados é de {soma}')