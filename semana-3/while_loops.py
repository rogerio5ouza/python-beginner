'''
Python Loops

O Python possui dois comandos nativos de loop:

    - While loops
    - For loops
'''
# Com o while loop, podemos executar um conjunto de instruções desde que uma condição seja verdadeira:

i = 1
while i <= 10:
    print(i)
    i += 1

'''
The break Statement (Declaração break)

Com o break, podemos parar o loop mesmo se a condição while for verdadeira.
'''
# Exemplo:

i = 1
while i <= 10:
    print(i)
    if i == 5:
        break
    i += 1

'''
The continue Statement (Declaração continue)

Com a instrução continue, podemos parar a interação atual e continuar com a próxima.
'''
# Exemplo:

i = 0
while i < 7:
    i += 1
    if i == 3:
        continue
    print(i)

'''
 The else Statement (Declaração else)

 Com a declaração else, podemos executar um bloco de código uma vez, quando a condição não for mais verdadeira.
'''
# Imprimi a mensagem quando a condição for false:

i = 1
while i <= 10:
    print(i)
    i += 1
else:
    print('i não é menor do que 10')
