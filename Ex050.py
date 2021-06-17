s = 0
# serve de start pro loop e não de parâmetro fixo. Pertence ao passado mas é extremamente necessário.

for c in range(0,6):
# montando o loop pra testar antes de fazer o completo

    n = int(input('\nDigite um numero: '))
# crio a variável n para me pedir um int

    if n %2 == 0:
# função "SE" e parâmetro pra retornar apenas numeros pares. Ou seja, quando divididos por 2 tem resto de divisão = 0

       s = s + n
# "S" recebe s(10) la de cima + n. Quando o ciclo fecha o s deixa de valer 10 e passa a valer o numero atribuido no presente.

print('\nA soma dos números pares é igual a {}'.format(s))
# Apenas entrega o resultado da soma dos numeros pares digitados.

