num1 = float(input('Digite um valor numérico real qualquer: '))
num2 = float(input('Digite outro valor numérico real qualquer: '))
print('\n\n''\033[1;31m', ' -' * 30, '\033[m''\n')
if num1 > num2:
    print('\033[32m''       O primeiro número escolhido é maior que o segundo!!''\033[m')
elif num1 < num2:
    print('\033[35m''       O primeiro número escolhido é menor que o segundo!!''\033[m')
else:
    print('\033[36m''       O primeiro e o segundo número escolhidos são iguais!! ''\033[m')
print('\n''\033[1;31m', ' _' * 30, '\033[m')