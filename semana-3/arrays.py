'''
Arrays

O que é um Array?

Um Array é uma variável especial, que pode conter mais de um valor.

Um Array pode conter muitos valores com um único nome e podemos acessar esses valores consultando um número do índice.

Nota: O Python não possui suporte nativo para matrizes, mas as listas do Python podem ser usadas como Arrays.
No entanto para trabalhar com matrizes no Python, precisamos importar uma biblioteca, como a NumPy.

Arrays são usados para armazenar múltiplos valores em uma variável.
'''
# Exemplo:
carros = ['Fiat', 'Ford', 'Volkswagen', 'Toyota']
print(carros)

'''
Acessando elementos de Array

Podemos acessar os elementos de uma Array através de seu índice.
'''
# Exemplo:

carros = ['Fiat', 'Ford', 'Volkswagen', 'Toyota']
elementos_carros = carros[1]
print(elementos_carros)

# Modificando o valor de um item de Array:

carros = ['Fiat', 'Ford', 'Volkswagen', 'Toyota']
carros[2] = 'Nissan'
print(carros)

'''
Comprimento de um Array

Usamos o método len() para rtornar o comprimento de um Array.
'''
# Exemplo:

carros = ['Fiat', 'Ford', 'Volkswagen', 'Toyota']
comprimento_carros = len(carros)
print(comprimento_carros)

'''
Loop de elementos em um Array

Podemos usar o loop FOR IN para percorrer todos os elementos de um Array.
'''
# Exemplo:

carros = ['Fiat', 'Ford', 'Volkswagen', 'Toyota']
for elementos in carros:
    print(elementos)

'''
Adding Array Elements (Adicionando elementos de Array)

Podemos usar o método append() para adicionar elemento em um Array.
'''
# Exemplo:

carros = ['Fiat', 'Ford', 'Volkswagen', 'Toyota']
carros.append('Honda')
print(carros)
