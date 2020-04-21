'''
Tipos de Variáveis em Python 

    str (-ing)  'Texto entre aspas', 'palavra'
    bool (-lean) True ou False
    int (-eger)  1, 2, 10, 5000
    float        3.5432, 9.8, 1.61803398875
    list         [ 'palavra', True, 1, 3.1415]
    dict         { 'prop':'nome', 'tem':True }
    tuple        ( 'palavra', True, 1, 3.1415)
    type         Tipo dos tipos

'''

# Variáveis - Reserva um espaço na memória para armazenar um dado/valor de um determinado tipo, e o associa a um nome.
var_1 = 5
var_2 = 10
total = var_1 + var_2

print(total)

# tipagem dinâmica: o último valor atribuído à variável indicará o tipo dela.
var_1 = "valor"           # atribuição de string
var_2 = 'valor'           # atribuição de string
var_1 = 5                 # atribuição de inteiro
var_2 = 3.1337            # atribuição de float
a, b, c = 1, 2, 'teste'   # múltiplas atribuições

# str - tipo composto por um conjunto 'imutável' de caracteres, texto.
fruta = "banana"
marca = """Tesla"""
str_1 = 'abc'
str2 = '''teste'''
len(fruta)           # retorna o comprimento, 6.
fruta[0]             # retorna 'b'
fruta[2:5]           # retorna 'nan'
fruta.upper()        # retorna 'BANANA'

# bool - verdadeiro ou falso.
var1 = True   # verdadeiro
var2 = False  # falso

# int números inteiros - sem limites de bits.
var1 = 1991
var2 = 2020


# float - números decimais (double).
var_1 = 1.2345
var_2 = 3.141592
