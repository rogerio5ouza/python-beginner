import json

'''
Python JSON

JSON é uma sintaxe para armazenamento e troca de dados.

JSON é um texto escrito com notação de objeto JavaScript.

Python tem um pacote integrado chamado json, que pode ser usado para trabalhar com dados JSON.
'''
# Exemplo
# Importa o módulo json:

# import json

'''
Parse JSON - Converte de JSON para Python

Se tivermos uma string JSON, podemos analisá-la usando o método json.loads(). 
'''
# Exemplo
# Converte de JSON para Python:

# JSON:

string_json = '{"nome":"John", "idade":32, "cidade":"Salvador-BA"}'
# x = '{ "nome":"John", "idade":30, "cidade":"Salvador-BA"}'

# parse string_json:

parse_json_para_python = json.loads(string_json)
# y = json.loads(x)

# o resultado e um dicionario Python:

print(parse_json_para_python["idade"])
# print(y["idade"])
