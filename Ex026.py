frase = input('Digite uma frase: ').strip()
tratoA = frase.lower()
procuraA = tratoA.find('a')+1
contarA = tratoA.count('a')
print('A letra a aparece {} vezes da frase,sendo sua aprarição na posição {} e sua última na posição {}.'
       .format(contarA,procuraA,tratoA.rfind('a')+1))
