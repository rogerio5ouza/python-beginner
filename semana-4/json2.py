
import json
'''
Converter de Python para JSON

Se tivermos um objeto Python, poderemos convertê-lo em uma string JSON usando o método json.dumps().
'''
# um objeto Python (dict):

dados_pessoais = {
    "nome": "Rogerio",
    "idade": 30,
    "cidade": "Brasili-DF"
}

# converte para JSON:
dados_convertidos = json.dumps(dados_pessoais)

# o resultado será uma string:
print(dados_convertidos)
