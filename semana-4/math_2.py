'''
O módulo Math

Python possui um módulo integrado chamado Math, que estende uma lista de funções matemáticas.

Para usá-lo, devemos importá-lo.

Depois de importá-lo, podemos começar a usar os métodos e constantes.
'''

# O método math.sqrt() retorna a raiz quadrada de um número:

import math

numero_quadrado = math.sqrt(49)
print(numero_quadrado)

'''
O método math.ceil() arredonda um número para cima, para seu inteiro mais próximo, e o método math.floor() 
arredonda um número para baixo, para seu inteiro mais próximo e retorna o resultado.
'''
# Exemplo:

arredonda_pra_cima = math.ceil(1.4)
arredonda_pra_baixo = math.floor(1.4)

print(arredonda_pra_cima)
print(arredonda_pra_baixo)

# A constante math.pi retorna o valor de PI(3,14...):

numero_pi = math.pi

print(numero_pi)
