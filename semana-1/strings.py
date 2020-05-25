'''
Python Strings

Strings literais

Strtings literais em Python são declaradas entre aspas simples ou duplas.

Você pode exibir uma String literal com a função print().
'''

# Exemplo:

print('Hello')
print("Hello")

''' 
Atribuição de String a uma Variável

Atribuir uma String a uma Variável é feita com o nome da Variável seguida por um sinal de igual e a String:
'''

a = "Hello"
print(a)

'''
Strings de Multilinhas

Você pode atribuir uma String de multilinhas para uma variável, usando três aspas simples/duplas:
'''
# Exemplo:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

print(a)

'''
Strings são Arrays

Como muitas outras linguagens de programação populares, as Strings no Python são matrizes de bytes que representam caracteres unicode.

No entanto, o Python não possui um tipo de dados de caractere; um único caractere é simplesmente uma String com comprimento 1.

Parênteses retos podem ser usados para acessar elementos da sequência.
'''

# Exemplo
# Coloque o caracter na posição 1 (lembre-se de que o primeiro caracter tem a posição 0):

a = 'Hello, World!'
print(a[1])

'''
Slicing (Fatiamento)

Você pode retornar um intervalo de caracteres usando a sintaxe Slice.

Especifique o índice inicial e o final, separados por dois pontos, para retornar uma parte da sequência.
'''

# Exemplo:
# Coloque os caracteres da posição 2 para a posição 5 (não incluídos):

b = "Hello, World!"
print(b[2:5])

'''
Negative Indexing (Indexação Negativa)

Podemos usar índices negativos para iniciar o slice do final de uma String.
'''
# Exemplo:

b = 'Hello, Wolrd!'
print(b[-5:-2])
