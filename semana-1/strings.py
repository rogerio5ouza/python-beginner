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

'''
String Length (Comprimento da String)

Para obter o comprimento de uma string, usamos a função len().
'''
# A função len() retorna o comprimento de uma String ():

a = 'Hello, World!'
print(len(a))

'''
Métodos de String

O Python possui um conjunto de métodos internos que você pode usar em Strings.
'''

# O método strip() remove qualquer espaço do início ou do final da string:

a = ' Hello, Wolrd! '
print(a.strip())    # retorna 'Hello, World!'

# O método lower() retorna a string em letras minúsculas:

a = 'Hello, World!'
print(a.lower())

# O método upper() retorna a string em letras maiúsculas:

a = 'Hello, World!'
print(a.upper())

# O método replace() substitui uma string por outra string:

a = 'Hello, World!'
print(a.replace('H', 'J'))

# O método split() divide a sequência em substrings se encontrar instâncias do separador:

a = 'Hello, World!'
print(a.split(','))  # retorna ['Hello', 'World!']

'''
Check String (Verificar String)

Para verificar se uma determinada frase ou caracter está presente em uma string, podemos usar
as palavras-chvave in ou not in.
'''

# Exemplo - Check se a frase 'ain' está presente no seguinte texto:

txt = 'The rain in Spain stays mainly in the plain.'
x = 'ain' in txt
print(x)

# Exemplo - Check se na frase 'ain' NÃO está presente no seguinte texto:

txt = 'The rain in Spain stays mainly in the plain.'
x = 'ain' not in txt
print(x)

'''
String Concatenation (Concatenação de strings)

Para concatenar ou combinar duas sequências, podemos usar o operador +.
'''
# Exemplo:
# Mesclar a variável A com a variável B dentro da variável C:

a = 'Hello '
b = 'World'
c = a + b
print(c)

'''
String Format (Formato de cadeia)

Não podemos combinar (concatenar) uma sequência do tipo String com um Integer, isso resultará em TypeError.
'''

# Exemplo:

age = 36
txt = 'My name is John, I am ' + age
print(txt)

'''
Mas podemos combinar Strings com Números usando o método format().

O método format() pega os argumentos passados, formata-os e coloca-os na String 
em que os espaços reservados {} estão.
'''
# Exemplo:
# Use o método format() para inserir Números dentro de Strings:

age = 36
txt = 'My name is John, and I am {}'
print(txt.format(age))

# O método format() recebe um número ilimitado de argumentos que são colocados nos respectivos espaços reservados:

quantity = 3
itemno = 567
price = 49.95
myorder = 'I want {} pieces of item {} for {} dollars.'
print(myorder.format(quantity, itemno, price))

# Podemos usar números de índice {0} para garantir que os argumentos sejam colocados nos espaços reservados corretamente:

quantity = 3
itemno = 567
price = 49.95
myorder = 'I want to pay {2} dollars for {0} pieces of item {1}.'
print(myorder.format(quantity, itemno, price))

'''
Escape Character (Caracteres de Escape)

Para inserir caracteres que são ilegais em uma string, usamos Caracteres de Escape.
Um Caractere de Escape é uma barra invertida '\' seguida pelo caractere que você deseja inserir.
Um exemplo de Caractere ilegal é uma aspas duplas dentro de uma string que é cercada por aspas duplas.
'''
# Você receberá um erro se usar aspas duplas dentro de uma string cercada por aspas duplas:

# txt = "We are the so-called "Vikings" from the north."
print(txt)

# Para corrigir esse problema, usamos o caractere de escape \".
# O caracter de escape permite que você use aspas duplas quando normalmente não seria permitido:

txt = "We are the so-called \"Vikings\" from the north."
print(txt)

# Outros caracteres de escape usados em Python:

# \' -> Single Quote (Aspas simples)
txt = 'It\'s alright.'
print(txt)

# \\ -> Backslash (Barra invertida)
txt = 'This will insert one \\ (backslash).'
print(txt)

# \n -> New Line (Nova linha)
txt = 'Hello\nWorld!'
print(txt)

# \r -> Carriage Return
txt = 'Hello\rWorld!'
print(txt)

# \t -> Tab (Tabulação/Espaço)
txt = 'Hello\tWorld!'
print(txt)

# \b -> Backspace (Retrocesso)
txt = 'Hello \bWorld!'
print(txt)

# \ooo -> Octal value (Valor octal)
txt = '\110\145\154\157'
print(txt)

# \xhh -> Hex value (Valor hexadecimal)
txt = '\x48\x65\x6c\x6c\x6f'
print(txt)
