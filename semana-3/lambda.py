'''
Lambda Function (Função Lambda)

Uma função lambda é uma pequena função anônima.
Uma função lambda pode receber qualquer número de argumentos, mas pode ter apenas uma expressão.
'''
# Exemplo - Uma função lambda que adiciona 10 ao número passado como argumento e imprime o resultado:


def x(numero_x): return numero_x + 10


print(x(5))

'''
As funções lambdas podem receber qualquer número de argumentos.
'''
# Exemplo - Uma função lambda que multiplica o parâmetro passado A pelo parâmetro B e imprime o resultado:


def y(a, b): return a * b


print(y(10, 5))

# Exemplo - Uma função lambda que soma os parâmetros A, B, e C e imprime o resultado:


def z(a, b, c): return a + b + c


print(z(2, 3, 5))
