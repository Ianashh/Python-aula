n = int(input('Digite um numero: '))
b = n + 1
a = n - 1

print('O número de sua escolha foi o {}{}{}, seu antecessor é o número {}{}{} e seu sucessor é o número {}{}{}'.format(
    '\033[34m', n, '\033[m', '\033[31m', b, '\033[m', '\033[4;32m', a, '\033[m'))
