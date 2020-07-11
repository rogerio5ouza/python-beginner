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

'''
Else no loop For

O else especifica um bloco de código a ser executado quando o loop for concluído.
'''
# Exemplo - imprima todos os números de 0 a 20 e imprima uma mensagem quando o loop terminar:

for x in range(20):
    print(x)
else:
    print('Fim!')

'''
Loops Aninhados

Um loop aninhado é um loop dentro de outro loop.
O 'loop interno' será executado uma vez para cada iteração do 'loop externo'.
'''
# Exemplo - imprima um adjetivo para cada fruta:

adjetivo = ['vermelho(a)', 'grande', 'saboroso(a)']
frutas = ['maçã', 'banana', 'cereja']

for x in adjetivo:
    for y in frutas:
        print(x, y)

'''
A Declaração pass

Os loops for não podem estar vazios, mas se, por algum motivo, tivermos um loop sem conteúdo, inserimos a instrução PASS para evitar erros.
'''
# Exemplo:

for numeros in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    pass
