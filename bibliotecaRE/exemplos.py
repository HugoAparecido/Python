import re

# . - Entende qualquer valor exceto uma nova linha
# \. - Para buscar o caracter "."
texto = '''
ar\nra
arara
arbra
'''
padrao = re.compile('ar.ra')
check = padrao.findall(texto)
print(check)  # ['arara', 'arbra']

# ^ - Irá testar o início da string
# [^] - Irá considerar todos os caracteres EXCETO o indicado
texto = 'arsdadadadaara'
p1 = re.compile('^a')
p2 = re.compile('[^a]')
check1 = p1.findall(texto)
check2 = p2.findall(texto)
print(check1)  # ['a']
print(check2)  # ['r', 's', 'd', 'd', 'd', 'd', 'r']

# \d - Qualquer caracter que SEJA um algarismo de 0 a 9
# \D - Qualquer caracter que NÃO SEJA um algarismo de 0 a 9
texto = 'arara1992'
p1 = re.compile(r'\d')
p2 = re.compile(r'\D')
check1 = p1.findall(texto)
check2 = p2.findall(texto)
print(check1)  # ['1', '9', '9', '2']
print(check2)  # ['a', 'r', 'a', 'r', 'a']

# \s - Qualquer caracter que SEJA vazio
# \S - Qualquer caracter que NÃO SEJA vazio
texto = '''

arara 1992

'''

p1 = re.compile(r'\s')
p2 = re.compile(r'\S')
check1 = p1.findall(texto)
check2 = p2.findall(texto)
print(check1)   # ['\n', '\n', ' ', '\n', '\n']
print(check2)  # ['a', 'r', 'a', 'r', 'a', '1', '9', '9', '2']

# \w - Qualquer caracter que SEJA alfanumérico
# \W - Qualquer caracter que NÃO SEJA alfanumérico
texto = '''

_arara@ 1992_

'''

p1 = re.compile(r'\w')
p2 = re.compile(r'\W')
check1 = p1.findall(texto)
check2 = p2.findall(texto)
print(check1)  # ['_', 'a', 'r', 'a', 'r', 'a', '1', '9', '9', '2', '_']
print(check2)  # ['\n', '\n', '@', ' ', '\n', '\n']

# Métodos para checagem:
texto = 'arara'
p1 = re.compile(r'r')
check_findall = p1.findall(texto)
check_match = p1.match(texto)  # no início da string
check_search = p1.search(texto)  # qualquer parte da string
check_finditer = p1.finditer(texto)  # cria um iterador
print(check_findall)  # ['r', 'r']
print(check_match)  # None
print(check_search)  # <re.Match object; span=(1, 2), match='r'>
print(check_finditer)  # <re.Match object; span=(1, 2), match='r'>
correspondencias = check_finditer
for correspondencia in correspondencias:
    print(correspondencia)
    # <re.Match object; span=(1, 2), match='r'>
    # <re.Match object; span=(3, 4), match='r'>

# Estruturas

# Character set
texto = '''
Arara 1992
'''
p = re.compile(r'[a-zA-Z0-9]')
correspondencias = p.finditer(texto)
for correspondencia in correspondencias:
    print(correspondencia)
    # <re.Match object; span=(1, 2), match='A'>
    # <re.Match object; span=(2, 3), match='r'>
    # <re.Match object; span=(3, 4), match='a'>
    # <re.Match object; span=(4, 5), match='r'>
    # <re.Match object; span=(5, 6), match='a'>
    # <re.Match object; span=(7, 8), match='1'>
    # <re.Match object; span=(8, 9), match='9'>
    # <re.Match object; span=(9, 10), match='9'>
    # <re.Match object; span=(10, 11), match='2'>
texto = '''
Arara 1992
'''
p = re.compile(r'[a-zA-Z] [0-9]')
correspondencias = p.finditer(texto)
for correspondencia in correspondencias:
    print(correspondencia)  # <re.Match object; span=(5, 8), match='a 1'>
texto = '''
Arara 1992
Ara 192
'''
p = re.compile(r'[a-zA-Z]+ [0-9]+')
correspondencias = p.finditer(texto)
for correspondencia in correspondencias:
    print(correspondencia)
    # <re.Match object; span=(1, 11), match='Arara 1992'>
    # <re.Match object; span=(12, 19), match='Ara 192'>

# Quantificadores:

# * - 0 ou mais
texto = '''
Arara
'''
p = re.compile(r'[ra]*')
correspondencias = p.finditer(texto)
for correspondencia in correspondencias:
    print(correspondencia)
    # <re.Match object; span=(0, 0), match=''>
    # <re.Match object; span=(1, 1), match=''>
    # <re.Match object; span=(2, 6), match='rara'>
    # <re.Match object; span=(6, 6), match=''>
    # <re.Match object; span=(7, 7), match=''>
# + - 1 ou mais
texto = '''
Arara
'''
p = re.compile(r'[ra]+')
correspondencias = p.finditer(texto)
for correspondencia in correspondencias:
    print(correspondencia)  # <re.Match object; span=(2, 6), match='rara'>
# ? - 0 ou 1
texto = '''
Arara
'''
p = re.compile(r'[ra]?')
correspondencias = p.finditer(texto)
for correspondencia in correspondencias:
    print(correspondencia)
    # <re.Match object; span=(0, 0), match=''>
    # <re.Match object; span=(1, 1), match=''>
    # <re.Match object; span=(2, 3), match='r'>
    # <re.Match object; span=(3, 4), match='a'>
    # <re.Match object; span=(4, 5), match='r'>
    # <re.Match object; span=(5, 6), match='a'>
    # <re.Match object; span=(6, 6), match=''>
    # <re.Match object; span=(7, 7), match=''>
# {3} - número exato de repetições
texto = '''
Arara
'''
p = re.compile(r'[ra]{2}')
correspondencias = p.finditer(texto)
for correspondencia in correspondencias:
    print(correspondencia)
    # <re.Match object; span=(2, 4), match='ra'>
    # <re.Match object; span=(4, 6), match='ra'>
# {3,4} - de 3 a 4 min e max
texto = '''
Arara
'''
p = re.compile(r'[ra]{2,4}')
correspondencias = p.finditer(texto)
for correspondencia in correspondencias:
    print(correspondencia)  # <re.Match object; span=(2, 6), match='rara'>

# ()Grupos
texto = '''
Arara 1992
arara 1993
'''
p = re.compile(r'(A|a)?[a-z]{4} [0-9]+')

correspondencias = p.finditer(texto)
for correspondencia in correspondencias:
    print(correspondencia)
    print(correspondencia.group(0))
    print(correspondencia.group(1))
    # <re.Match object; span=(1, 11), match='Arara 1992'>
    # Arara 1992
    # A
    # <re.Match object; span=(12, 22), match='arara 1993'>
    # arara 1993
    # a
