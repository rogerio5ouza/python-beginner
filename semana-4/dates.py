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

'''
Creating Date Objects

Para criar uma data, usamos a classe datetime() (constructor) do módulo datetime.

A classe datetime() requer três parâmetros para criação de uma data: ano, mês, dia.
'''
# Exemplo

data = datetime.datetime(2020, 9, 8)
print(data)

'''
A classe datetime() também usa parâmetros para hora e fuso horário(hora, minuto, segundo, microssegundo, tzone),
mas eles são opcionais e possuem valor padrão de 0, (Nenhum para fuso horário).
'''
