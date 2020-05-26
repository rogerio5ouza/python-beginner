'''
Python Numbers (Números em Ptyhon)

Existem três tipos numéricos em Ptyhon:
'''
 # int
 # float
 # complex

'''
Variáveis de tipos numéricos são criadas quando você atribui um valor para elas:
'''

x = 1       # int
y = 2.8     # float
z = 1j      # complex

'''
Para verificar o tipo de qualquer objeto em Python, use a função type():'''

print (type(x))
print (type(y))
print (type(z))

'''
Int

Int, ou inteiro, é um número inteiro, positivo ou negativo, sem decimais, de comprimento ilimitado.
'''
# Integers:

x = 1
y = 35656222554887711
z = -325522

print (type(x))
print (type(y))
print (type(z))

'''
Float

Float ou "número de ponto flutuante" é um número, positivo ou negativo, contendo uma ou mais casas decimais.
'''

# Floats:

x = 1.10
y = 1.0
z = 35.59

print (type(x))
print (type(y))
print (type(z))

'''
Float também pode ser um número científico com um "e" para indicar a potência 10.
'''

# Floats:

x = 35e3
y = 12E4
Z = -87.7e100

print (type(x))
print (type(y))
print (type(z))

'''
Complex

Números complexos são escritos com um "j" como a parte imaginária:
'''

# Complex

x = 3+5j
y = 5j
z = -5j

print (type(x))
print (type(y))
print (type(z))

'''
Type Conversion (Conversão de Tipo)

Voçê pode converter de um tipo para outro com os métodos int(), float() e complex():
'''

# Converter de um tipo para outro:

x = 1       # int
y = 2.8     # float
z = 1j      # complex

# converte de int para float:

a = float (x)

# converte de float para int:

b = int (y)

# converte de int para complex:

c = complex (x)

print (a)
print (b)
print (c)

print (type(a))
print (type(b))
print (type(c))

'''
Random Number (Número Randômico)

O Python não possui uma função random() para criar um núemro aleatório, mas o Python possui um módulo interno chamado
ramdom que pode ser usado para criar números aleatórios:
'''

# Importe o módulo aleatório e exiba um número aleatório entre 1 e 9:

import random

print (random.randrange(1, 10))











