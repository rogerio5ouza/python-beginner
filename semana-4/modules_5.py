'''
Uso da função dir()

Existe uma função embutida no Python para listar todos os nomes de função(ou nomes de variáveis) em um módulo.
'''
# Lista todos os nomes definidos pertencentes ao módulo da plataforma:

import platform

x = dir(platform)
print(x)
