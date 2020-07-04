'''
If...Else 

O Python suporta as condições usuais lógicas da matemática:

* É iguala: a == b
* Diferente: a! = B
* Menor que: a < b
* Menor ou igual a: a <= b
* Maior que: a > b
* Maior que ou Igual a: a >= b 

Essas condições podem ser usadas de várias formas, mais comumente em 'instruções if' e loops.
'''
# Exemplo:

a = 14
b = 30
if b > a:
    print('b é maior que a.')

'''
Elif

A palavra-chave Elif é uma forma do Python dizer 'se a condição anterior não for verdadeira, tente esta condição'.
'''
# Exemplo:

a = 7
b = 7
if a > b:
    print('b é maior do que a.')
elif a == b:
    print('a e b são iguais.')

'''
Else 

O Else captura qualquer coisa que não seja capturada pelas condições anteriores.
'''
# Exemplo:

a = 20
b = 10
if b > a:
    print('b é maior que a.')
elif a == b:
    print('a e b são iguais.')
else:
    print('a é maior que b.')

# Se tivermos apenas uma instrução para executar, podemos colocá-la na mesma linha que o If:
a = 200
b = 100

# if a > b: print('a é maior que b.')

# Se tivermos apenas uma instrução para executar, uma para If e outra para Else, podemos também colocá-las na mesma linha:

a = 500
b = 1000
print('A') if a > b else print('B')

# Podemos ainda colocar várias instruções Else na mesma linha:

a = 1000
b = 1000
print('A') if a > b else print('=') if a == b else print('B')