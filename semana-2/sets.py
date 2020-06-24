'''
SET (Conjunto)

Um Set é uma coleção de itens não ordenada e nem indexada. Em Python Sets são escritos entre colchetes {}.
'''
# Exemplo:

set_de_animais_felinos = {
    'Tigre', 'Leao', 'Lince', 'Onca-pintada', 'Leopardo-das-neves', 'Guepardo'
}

print(set_de_animais_felinos)

print(type(set_de_animais_felinos))

'''
  Acesso de itens (Access Items)

  Não podemos acessar itens de um conjunto consultando seu índice, pois os conjuntos são desordenados e seus itens não possuem índice.
  Mas podemos percorrer os itens do conjunto usando um loop for ou perguntar se um valor específico está presente em um conjunto, usando a in keyword.
'''
# Exemplo:

set_de_animais_felinos = {
    'Tigre', 'Leao', 'Lince', 'Onca-pintada', 'Leopardo-das-neves', 'Guepardo'
}

for x in set_de_animais_felinos:
    print(x)

# Verifica se 'Guepardo' está presente no conjunto:

set_de_animais_felinos = {'Tigre', 'Leao', 'Lince',
                          'Onca-pintada', 'Leopardo-das-neves', 'Guepardo'}

print('Guepardo' in set_de_animais_felinos)

'''
Adição de Itens (Add Items)

Para adicionar um item em um conjunto, usamos o método add().
Para adicionar mais de um item, usamos o método update().
'''
# Exemplo de add():

set_de_animais_felinos = {'Tigre', 'Leao', 'Lince'}

set_de_animais_felinos.add('Guepardo')

print(set_de_animais_felinos)

# Exemplo de update():

set_de_animais_felinos = {'Tigre', 'Leao', 'Lince'}

set_de_animais_felinos.update(['Guepardo', 'Gato', 'Jaguar'])

print(set_de_animais_felinos)
