'''
Python Casting (Fusão)

Especifica um tipo de variável

Pode haver momentos em que você queira especificar um tipo para uma variável. Isso pode ser feito com Casting.
Python é uma linguagem orientada a objetos e, como tal, usa classes para definir tipos de dados, incluindo seus 
tipos primitivos.

Casting em Python é, portanto, feita usando funções de construtor:

int() - constrói um número inteiro a partir de um literal int, um literal float (arredondando para baixo para o número
        int anterior) ou um literal string (desde que a string represente um número int).

float() - constrói um número float a partir de um literal int, um float literal ou um string literal (desde que a string
          represente um número inteiro ou flutuante).

str() - constrói uma string a partir de um ampla variedade de tipos de dados, incluindo strings, literais inteiros e literais float.
'''

# Exemplos

# Integers:

x = int(1)    # x será 1
y = int(2.8)  # y será 2
z = int('3')  # z será 3

print (x)
print (y)
print (type(z))


# Floats:

x = float(1)        # x será 1.0
y = float(2.8)      # y será 2.8
z = float('3')      # z será 3.0
w = float('4.2')    # w será 4.2

print (x)
print (y)
print (z)
print (type(w))

# Strings

x = str('s1')   # x será 's1'
y = str(2)      # y será '2'
z = str(3.0)    # z será '3.0'

print (x)
print (y)
print (type(z))
