'''
PYTHON LISTS
PYTHON COLLECTIONS (Arrays)

Existem quatro tipos de coleção de dados na linguagem de programação Python:

- List (lista) é uma coleção que é ordenada e mutável. Permite membros duplicados.
- Tuple (tupla) é uma coleção ordenada e imutável. Permite membros duplicados.
- Set (conjunto) é uma coleção não ordenada e não indexada. Nenhum membro duplicado.
- Dictionary (dicionário) é uma coleção desordenda, mutável e indexada. Nenhum membro duplicado.

Ao escolher um tipo de coleção, é útil entender as propriedades desse tipo. Escolher o tipo certo
para um conjunto de dados específico pode significar retenção de significado e, também, aumento de eficiência ou segurança.
'''

# List
thislist = ['apple', 'banana', 'cherry']

print(thislist)

# Itens de acesso - podemos acessar os itens da lista consultando o número do índice:
thislist = ['apple', 'banana', 'cherry']

print(thislist[1])

# Indexação negativa (Negative Indexing)- significa que começa no final, -1 refere-se ao último item, -2 refere-se ao segundo último item etc...
thislist = ['apple', 'banana', 'cherry']

print(thislist[-1])

# Intervalo de índices (Range of Indexes) - podemos especificar um intervalo de índices especificando por onde começar e por onde terminar o intervalo.
# Ao especificar um intervalo, o valor retornado será uma nova lista com os itens especificados.
thislist = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']

print(thislist[2:5])

# Deixando de fora o valor inicial, o intervalo comecará no primeiro item:
thislist = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']

print(thislist[:4])

# Deixando de fora o valor final, o intervalo continuará no final da lista:
thislist = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']

print(thislist[2:])

# Intervalo de índices negativos (Range of Negative Indexes) - para especificar índices negativos do final da lista:
thislist = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']

print(thislist[-4:-1])

# Intervalo de índices negativos (Range of Negative Indices)
# Muda o segundo item:

thislist = ['apple', 'banana', 'cherry']
thislist[1] = 'blackcurrant'
print(thislist)

# Loop através de uma lista
# Podemos percorrer os itens de uma lista usando loop for:

thislist = ['apple', 'banana', 'cherry', 'melon']
for x in thislist:
    print(x)


# Verifica se o item existe (Check if Item Exists)
# Para determinar se um item específico está presente em uma lista, usamos a palavra-chave IN:

thislist = ['apple', 'banana', 'cherry']
if 'apple' in thislist:
    print("Yes, 'apple' is in the list")

# Comprimento da lista (List Length)
# Para determinar quantos itens uma lista possui, usamosa a função len():

thislist = ['apple', 'banana', 'cherry']
print(len(thislist))

# Adicionar itens (Add Items)
# Para adicionar um item ao final da lista, usamos o método APPEND():

thislist = ['apple', 'banana', 'cherry']
thislist.append('orange')
print(thislist)

# Para adicionar um item ao índice especificado, usamos o método INSERT():

thislist = ['apple', 'banana', 'cherry']
thislist.insert(1, 'orange')
print(thislist)

# Remover item (Remove Item)
# Existem vários métodos para remover itens de uma lista:

thislist = ['apple', 'banana', 'cherry']
thislist.remove('banana')
print(thislist)

# O método pop() remove um índice específico (ou o último item se o índice não for especificado):

thislist = ['apple', 'banana', 'cherry']
thislist.pop()
print(thislist)

# A palavra chave DEL remove um índice específico:

thislist = ['apple', 'banana', 'cherry']
del thislist[0]
print(thislist)

# A palavra chave DEL também pode deletar uma lista completa:

thislist = ['apple', 'banana', 'cherry']
del thislist

# O método clear() esvazia uma lista:

thislist = ['apple', 'banana', 'cherry']
thislist.clear()
print(thislist)

'''
COPIAR UMA LISTA (Copy a List)

Não podemos copiar uma lista simplesmente digitando list2 = list1, porque: list2 será apenas uma referência à list1 e as alterações feitas em list1 
também serão automaticamente feitas em list2.

Existem maneiras de se fazer uma cópia, e uma maneira é por meio do método de lista embutido copy().
'''
# Exemplo:

thislist = ['apple', 'banana', 'cherry']
mylist = thislist.copy()
print(mylist)

# Outra maneira de se fazer uma cópia, é usando o método de lista embutido list():

thislist = ['apple', 'banana', 'cherry']
mylist = list(thislist)
print(mylist)

'''
UNINDO DUAS LISTAS (Join Two Lists)

Existem várias maneiras de inserir ou concatenar duas ou mais listas.
Uma maneira fácil é fazendo uso do operador +.
'''

# Exemplo:

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# Outro maneira de unir listas é anexando(appending) todos os itens da list2 na list1, um por um:

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)

print(list1)

# Ou ainda podemos usar o método extend(), cujo objetivo é adicionar elementos de uma lista para outra lista (o método extend() adiciona a list2 no final da list1):

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

'''
CONSTRUTOR list() - The list() Constructor

É possível usar o construtor list() para fazer uma nova lista.
'''
# Exemplo:

thislist = list(('apple', 'banana', 'cherry'))
print(thislist)

'''
LISTA DE MÉTODOS (List Methods)

Python possui um conjunto de métodos nativos que pode ser usado em listas:

- append() -> Adiciona um elemento no final de uma lista.
- clear()  -> Remove todos os elementos da lista.
- copy()   -> Retorna uma cópia da lista.
- count()  -> Retorna o número de elementos com o específico valor.
- extend() -> Adiciona elementos de uma lista para o final da lista.
- index()  -> Retorna o índice do primeiro elemento com o valor especificado.
- insert() -> Adiciona um elemento em uma posição específica da lista.
- pop()    -> Remove o elemento da posição especificada.
- remove() -> Remove o item com um valor específico.
- reverse()-> Reverte a ordem da lista.
- sort()   -> Ordena a lista.

'''
