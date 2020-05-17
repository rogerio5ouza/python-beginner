'''
Tipos de Dados (Data Types)

Em programação, Data Types é um importante conceito.
Variáveis podem armazenar dados de diferentes tipos, e diferentes tipos podem fazer diferentes coisas.
Python possui os seguintes Data Types embarcaddos por default, nessas categorias:
'''

# Text Type:          str
# Numeric Types:      int, float, complex
# Sequence Types:     list, tuple, range
# Mapping Type:       dict
# Set Types:          set, frozenset
# Boolean Type:       bool
# Binary Types:       bytes, bytearray, memoryview

'''
Obtendo os Data Types

Podemos obter o Data Type de qualquer objeto usando a função type(): 
'''

x = 5
print(type(x)) # <class 'int'>

'''
Definindo o Data Type

Em Python, o data type é definido quando você atribue um valor para uma variável:
'''

# x = 'Hello World'                                     Data Type (str):

x = 'Hello World'
print(x)            # display x 
print(type(x))      # display the data type of x

# x = 20                                                Data Type (int):
# x = 20.5                                              Data Type (float)
# x = 1j                                                Data Type (complex)
# x = ['apple', 'banana', 'cherry']                     Data Type (list)
# x = ('apple', 'banana', 'cherry')                     Data Type (tuple)
# x = range(6)                                          Data Type (range)
# x = {'name' : 'John', 'age' : 32}                     Data Type (dict)
# x = {'apple', 'banana', 'cherry'}                     Data Type (set)
# x = frozenset({'apple', 'banana', 'cherry'})          Data Type (frozenset)
# x = True                                              Data Type (bool)
# x = b'Hello'                                          Data Type (bytes)
# x = bytearray(5)                                      Data Type (bytearray)
# x = memoryview(bytes(5))                              Data Type (memoryview)

'''
Podemos ainda, atribuir um específico data type.

Se voçê quer especificar o data type, você pode usar o seguinte construtor de funções:
'''

# x = str('Hello World')                                     Data Type (str)

x = str('Hello World')
print(x)                # display x
print(type(x))          # display the data type of x    

# x = int(20)                                                Data Type (int)
# x = float(20.5)                                            Data Type (float)
# x = complex(1j)                                            Data Type (complex)
# x = list(('apple', 'banana', 'cherry'))                    Data Type (list)
# x = tuple(('apple', 'banana', 'cherry'))                   Data Type (tuple)
# x = range(6)                                               Data Type (range)
# x = dict(name='John', age : 32)                            Data Type (dict)
# x = set(('apple', 'banana', 'cherry'))                     Data Type (set)
# x = frozenset(('apple', 'banana', 'cherry'))               Data Type (frozenset)
# x = boo(5)                                                 Data Type (bool)
# x = bytes(5)                                               Data Type (bytes)
# x = bytearray(5)                                           Data Type (bytearray)
# x = memoryview(bytes(5))                                   Data Type (memoryview)                                          