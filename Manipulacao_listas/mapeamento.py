# Função map()
# map(função, iterável)

# Lista de valores iniciais
from functools import reduce
valores = [1000, 1500, 2000, 2500, 3000]
print("Valores iniciais:", valores)

# Função para calcular o juro de 2%


def calcular_juro(valor): return valor * 1.02


# Usar map()
valores_com_juro = list(map(calcular_juro, valores))

# Exibir os valores com juro de 2%
print("Valores com juro de 2% aplicados:", valores_com_juro)

# Função map() com lambda
valores_inicias = [5000, 5500, 6000, 6500, 7000]
print("Valores iniciais:", valores_inicias)
valores_com_juro = list(map(lambda valor: valor*1.02, valores_inicias))
print("Valores com juro de 2% aplicados:", valores_com_juro)
print()

# Função filter
# filter(função, iterável)


def verificar_numero_par(x):
    return x % 2 == 0


# Lista de números
numeros = [1, 2, 3, 4, 5, 6]

# Usar filter() para filtrar números pares
pares = filter(verificar_numero_par, numeros)

# Converter o resultado para uma lista e imprimir
print(list(pares))

# Função filter() com lambda
numeros = [10, 11, 12, 13, 14, 15, 16]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)
print()

# Função reduce()
# reduce(função, iterável, valor_inicial)

# Nota: Em python 3, reduce() está disponível no módulo functools


def soma(a, b):
    return a+b


# Lista de números
numeros = [1, 2, 3, 4, 5]

# Usar reduce() para somar todos os elementos da lista
total = reduce(soma, numeros)
print(total)

# Função reduce() com lambda
numeros = [1, 2, 3, 4, 5]
total = reduce(lambda a, b: a+b, numeros, 50)
print(total)
