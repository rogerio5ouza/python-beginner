'''
For Loops

Um loop for é usado para iterar sobre uma sequência (percorre uma lista, tupla, dicionário, conjunto de string).
'''
# Exemplo:

frutas = ['amora', 'banana', 'cereja', 'goiaba', 'morango', 'uva']
for f in frutas:
    print(f)

'''
Loop atrevés de uma String

Mesmo as Strings são objetos iteráveis, elas contém uma sequência de caracteres.
'''
# Exemplo:

for f in 'banana':
    print(f)

'''
A declaração Break

Com o Break, podemos parar o loop antes que ele percorra todos os itens.
'''
# Exemplo 1 - saia do loop quando f for 'cereja':

frutas = ['amora', 'banana', 'cereja', 'goiaba', 'morango', 'uva']
for f in frutas:
    print(f)
    if f == 'cereja':
        break

# Exemplo 2 - saia do loop quando f for 'cereja', mas desta vez a quebra ocorre antes do print:

frutas = ['amora', 'banana', 'cereja', 'goiaba', 'morango', 'uva']
for f in frutas:
    if f == 'cereja':
        break
    print(f)

'''
A declaração Continue

Com a declaração continue, podemos parar a iteração atual do loop a continuar com a próxima
'''
# Exemplo - não imprima 'cereja':

frutas = ['amora', 'banana', 'cereja', 'goiaba', 'morango', 'uva']
for f in frutas:
    if f == 'cereja':
        continue
    print(f)
frutas = ['amora', 'banana', 'cereja', 'goiaba', 'morango', 'uva']
for f in frutas:
    if f == 'cereja':
        break
    print(f)

'''
A função range()

Para percorrer um conjunto de itens um número específico de vezes, podemos usar a função range().

A função range() retorna uma sequência de números, iniciando em 0 por padrão e incrementando em 1 (por padrão), e termina em um número especificado.
'''
# Exemplo:

for numeros in range(7):
    print(numeros)

# É possível especificar o valor inicial adicionando uma parâmetro: range(2,7), que significa de 2 a 7 (mas não inclui o 7):

for numeros in range(2, 7):
    print(numeros)

# A função range() por padrão incrementa de 1 em 1, no entanto, é possível especificar o valor do incremento adicionando um terceiro parâmetro: range(2,20,2):

for numeros in range(2, 20, 2):
    print(numeros)
