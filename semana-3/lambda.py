'''
Lambda Function (Função Lambda)

Uma função Lambda é uma pequena função anônima.
Uma função Lambda pode receber qualquer número de argumentos, mas pode ter apenas uma expressão.
'''
# Exemplo - Uma função lambda que adiciona 10 ao número passado como argumento e imprime o resultado:


def x(numero_x): return numero_x + 10


print(x(5))

'''
As funções Lambdas podem receber qualquer número de argumentos.
'''
# Exemplo - Uma função lambda que multiplica o parâmetro passado A pelo parâmetro B e imprime o resultado:


def y(a, b): return a * b


print(y(10, 5))

# Exemplo - Uma função lambda que soma os parâmetros A, B, e C e imprime o resultado:


def z(a, b, c): return a + b + c


print(z(2, 3, 5))

'''
Por que usar funções Lambda?

O poder do Lambda é mostrado melhor quando a usamos como uma função anônima dentro de outra função.
Digamos que temos uma definição de função que aceite um parâmetro e esse parâmetro será multiplicado por um número desconhecido.
'''
# Exemplo:


def minha_funcao_anonima(n):
    return lambda numero_x: numero_x * n

# Usamos essa definição de função para criar uma função que sempre dobre o número que enviamos por parâmetro:


def minha_funcao_anonima_2(n):
    return lambda numero_x: numero_x * n


meu_dobrador = minha_funcao_anonima_2(2)
print(meu_dobrador(10))
