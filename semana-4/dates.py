'''
Datas

Uma data em Python não é um tipo de dado próprio, mas podemos importar um módulo denominado 'datetime' para 
trabalhar com datas como objetos de data.
'''
# Exemplo
# Importa o módulo 'datetime' e exibe a data atual:

import datetime

hora_atual = datetime.datetime.now()
print(hora_atual)

'''
Date Output

A data de saída do código acima contém dia-mes-ano e a horário contém hora-minuto-segundo-microssegundo.

O módulo datetime possui muitos métodos para retornar informações sobre o objeto date.
'''

# Exemplo
# Retorna o ano e o nome do dia da semana


data_hora_atual = datetime.datetime.now()

print(data_hora_atual.year)
print(data_hora_atual.strftime("%A"))
