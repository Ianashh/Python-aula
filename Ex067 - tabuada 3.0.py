from time import sleep
print('>'*60)
n = int(input('Digite o numero do qual gostaria de saber a tabuada: '))
print('<'*60)
while True:
    for c in range(1, 11):
        print(f"\n{n:2} x {c:2} = {n * c:2}")
    sleep(2)
    print('-' * 60)
    n = int(input('Digite o numero do qual gostaria de saber a tabuada: '))
    print('-' * 60)
    if n < 0:
        sleep(2)
        print('Programa encerrado!!')
        break


