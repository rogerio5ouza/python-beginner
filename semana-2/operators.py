'''
Operators (Operadores)

Operadores em Python são usados para executar operações em variáveis e valores.
Python divide os Operadores nos seguintes grupos:
'''

# Arithmetic operators (Operadores aritméticos)
# Assignment operators (Operadores de atribuição)
# Comparison operators (Operadores de comparação)
# Logical operators    (Operadores lógicos)
# Identity operators   (Operadores de identidade)
# Membership operators (Operadores de associação)
# Bitwise operators    (Operadores bit a bit)

'''
Arithmetic operators (Operadores aritméticos)

São usados com valores numéricos para executar operações matemáticas comuns.
'''
# Operador Addition (+)
x = 5
y = 3
print(x + y)

# Operador Subtraction (-)
x = 5
y = 3
print(x - y)

# Operador Multiplication (*)
x = 5
y = 3
print(x * y)

# Operador Division (/)
x = 12
y = 3
print(x / y)

# Operador Modulus (%)
x = 5
y = 2
print(x % y)

# Operador Exponentiation (**)
x = 2
y = 5
print(x ** y)  # igual a 2*2*2*2*2

# Operador Floor Division (//)
x = 15
y = 2
print(x // y)  # a divisão // arredonda o resultado para o número inteiro mais próximo

'''
Assignment operators (Operadores de atribuição)

São usados para atribuir valores a variáveis.
'''

# Operador (=) igual a (x = 5)

x = 5
print(x)

# Operador (+=) igual a (x = x + 3)

x = 5
x += 3

print(x)

# Operador (-=) igual a (x = x - 3)

x = 5
x -= 3

print(x)

# Operador (*=) igual a (x = x * 3)

x = 5
x *= 3

print(x)

# Operador (/=) igual a (x = x / 3)

x = 5
x /= 3

print(x)

# Operador (%=) igual a (x = x % 3)

x = 5
x %= 3

print(x)

# Operador (//=) igual a (x = x // 3)

x = 5
x //= 3

print(x)

# Operador (**=) igual a (x = x ** 3)

x = 5
x **= 3

print(x)

# Operador (&=) igual a (x = x & 3)

x = 5
x &= 3

print(x)

# Operador (|=) igual a (x = x | 3)

x = 5
x |= 3

print(x)

# Operador (^=) igual a (x = x ^ 3)

x = 5
x ^= 3

print(x)

# Operador (>>=) igual a (x = x >> 3)

x = 5
x >>= 3

print(x)

# Operador (<<=) igual a (x = x << 3)

x = 5
x <<= 3

print(x)

'''
Operadores de comparação
São usados para comparar dois valores.
'''

# Exemplo:
# Operador Igual (==)
x = 5
y = 3

print(x == y)

# Operador Não igual (!=)
x = 5
y = 3

print(x != y)

# Operador Maior que (>)
x = 5
y = 3

print(x > y)

# Operador Menor que (<)
x = 5
y = 3

print(x < y)

# Operador Maior do que ou Igual a (>=)
x = 5
y = 3

print(x >= y)

# Operador Menor do que ou Igual a (<=)
x = 2
y = 3

print(x <= y)

'''
Operadores Lógicos

São usados para combinar declarações condicionais.
'''

# Operador AND (retorna True se ambas declarações forem verdadeiras).
x = 5

print(x > 3 and x < 10)

# Operador OR (retorna True se uma das declarações for verdadeira).
x = 5

print(x > 3 or x < 4)

# Operador NOT (reverte o resultado, retorna False se o resultado for verdadeiro).
x = 5

print(not(x > 3 and 5 < 10))

'''
OPERADORES DE IDENTIDADE

Os operadores de Identidade são usados para comparar os objetos, não se forem iguais,
mas se forem realmente o mesmo objeto, com o mesmo local na memória.
'''
# Operador IS (retorna True se ambas variáveis forem um objeto):

x = ['apple', 'banana']
y = ['apple', 'banana']
z = x

print(x is z)

# retorna True porque Z é o mesmo objeto que X

print(x is y)

# retorna False poque X não é o mesmo objeto que Y, mesmo se eles tiverem o mesmo conteúdo.

print(x == y)

# para demonstrar a diferença entre "is" e "==": essa comparação retorna True porque x é igual a y.

# Operador IS NOT (retorna True se ambas variáveis não forem o mesmo objeto).

x = ['apple', 'banana']
y = ['apple', 'banana']
z = x

print(x is not z)

# retorna False porque Z é o mesmo objeto x

print(x is not y)

# retorna True porque X não é o mesmo objeto que Y, mesmo se eles tiverem o mesmoconteúdo.

print(x != y)

# para demonstrar a difernça entre "NOT IS" e "!="...essa comparação retorna False porque X é igual a Y.

'''
OPERADORES DE ASSOCIAÇÃO (Membership Operators)

Os Operadores de Associação são usados se uma sequência é apresentada em um objeto.
'''
# Operador IN (retorna True se a sequência com o valor especificado estiver presente no objeto)

x = ['apple', 'banana']

print('banana' in x)

# Operador NOT IN (retorna True se uma sequência com o valor especificado não estiver presente no objeto)

x = ['apple', 'banana']

print('pineapple' not in x)

'''
OPERADORES BITWISE (Bitwise Operators)

Operadores Bitwise (bit a bit) são usados para comparar números (binários):

- Operador & = AND (define cada bit como 1 se ambos bits forem 1)
- Operador | = OR (define cada bit como 1 se um dos dois bits for 1)
- Operador ^ = XOR (define cada bit como 1 se somente um dos dois bits for 1)
- Operador ~ = NOT (invert todos os bits)
- Operador << = Zero desvio à esquerda (desloca-se para a esquerda pressionando os zeros da direita e deixando os bits à esquerda de fora)
- Operador >> = Mudança à direita (desloca-se para a direita empurrando cópias do bit mais à esquerda da esquerda e deixa os bits mais à direita de fora)

'''
