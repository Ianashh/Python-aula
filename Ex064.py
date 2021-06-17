from statistics import mean


n = []
cont = 0
p = []
soma = sum(p)
while p != 'N':
    p = input('\nDeseja digitar um número? Digite ''\033[1;32m''"S"''\033[m'' para sim ou''\033[1;31m'' "N"''\033[m'' para não: ').strip().title()
    if p == 'S':
        n.append(int(input('Digite um número: ')))
        print('\033[34m'f'A média até agora é de {mean(n)} sendo {max(n)} o maior número digitado e {min(n)} o menor.''\033[m')
    elif p == 'N':
        print('\033[31m'f'O programa foi encerrado!!\nA média foi de {mean(n)} sendo {max(n)} o maior número digitado e {min(n)} o menor.''\033[m')
    else:
        while p != 'S':
            if p != 'N':
                p = input('\033[33m''O valor digitado é inválido!!''\033[m'''
                '\nDigite ''\033[1;32m''"S"''\033[m'' para continuar ou''\033[1;31m'' "N"''\033[m'' para encerrar: ''\033[m').strip().title()
            else:
                print('\033[31m'f'O programa será encerrado!!'
                      f'\nA média até agora é de {mean(n)} sendo {max(n)} o maior número digitado e {min(n)} o menor.\n''\033[m')
                p = "S"
print('\033[32m'f'Os números digitados foram{n}')