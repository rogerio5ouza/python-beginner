"""
Formart the Result

O método json.dumps() possui parâmetros para facilitar a leitura do resultado.
"""

import json

x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

# Usamos quatro recuos para facilitar a leitura do resultado:

print(json.dumps(x, indent=4))


"""
Podemos também definirmos os separadores, o valor padrão é (", ", ": "), que significa usar uma vírgula e um espaço para
separarmos cada objeto, e dois pontos e um espaço para separar as chaves dos valores:
"""

x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

print(json.dumps(x, indent=4, separators=(". ", " = ")))
