import json

'''
Quando convertemos de Python para JSON, os objetos Python são convertidos
ao equivalente no JSON (JavaScript):

PYTHON      JSON

dict    ->  Object
list    ->  Array
tuple   ->  Array
str     ->  String
int     ->  Number
float   ->  Number
True    ->  true
False   ->  false
None    ->  null

'''

# Exemplo
# Conversão de um objeto Python contendo todos os tipos de dados legais:

x = {
    "nome": "John",
    "idade": 30,
    "casado": True,
    "divorciado": False,
    "criancas": ("Ana", "Billy"),
    "pets": None,
    "carros": [
        {"modelo": "Volkswagen Gol", "ano": 2020},
        {"modelo": "Ford Focus", "ano": 2019}
    ]
}

print(json.dumps(x))
