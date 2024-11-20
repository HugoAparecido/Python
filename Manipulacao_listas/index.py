# Manipulação de Listas
print("***************************")
print("** Manipulação de Listas **\n")
print("***************************")
# Criar uma lista
frutas = ["maçã", "banana", "laranja"]
print(frutas)

# Adicionar um item
frutas.append("uva")
print(frutas)

# Remover um item
frutas.remove("banana")
print(frutas)

# Acessar item pelo índice
print(f"Saída: {frutas[1]} \n")  # Saída laranja

# Iterar sobre a lista
for fruta in frutas:
    print(fruta)

# Manipulação de Tuplas
print("***************************")
print("** Manipulação de Tuplas **\n")
print("***************************")
# Criar uma tupla
usuario = ("Cesar", "cesar@celke.com.br")

# Acessar item pelo índice
print(usuario[0])  # Saída: Cesar

# Desempacotar tuplas
nome, email = usuario
print(f"Nome: {nome}, E-mail: {email}")

# Tentar modificar a tupla (gera erro)
# usuario[0] = 15 # TypeError: 'tuple' object does not support item assigment

# Manipulação de Dicionários
print("\n********************************")
print("** Manipulação de Dicionários **\n")
print("********************************")

# Criar um dicionário
aluno = {"nome": "Cesar", "idade": 18, "cidade": "Curitiba"}
print(aluno)

# Adicionar ou atualizar uma chave-valor
aluno["idade"] = 19
print(aluno)

# Acessar um valor pela chave
print(aluno["nome"])

# Iterar sobre chaves e valores
for chave, valor, in aluno.items():
    print(f"{chave}: {valor}")

# Remover uma chave-valor
del aluno["cidade"]
print(aluno)

# Manipulação de Conjuntos
print("\n******************************")
print("** Manipulação de Conjuntos **\n")
print("******************************")

# Criar um conjunto
numeros = {1, 2, 3, 4, 5}
print(numeros)

# Adicionar um elemento
numeros.add(6)
print(numeros)

# Remover um elemento
numeros.remove(4)
print(numeros)

# Operação de união e intersecção com outro conjunto
pares = {2, 4, 6, 8}
print("Pares:", pares)

uniao = numeros.union(pares)
print("União:", uniao)

intersecao = numeros.intersection(pares)
print("Interseção:", intersecao)

# Verificar se um elemento está no conjunto
print(3 in numeros)  # Saída: True
print(7 in numeros)  # Saída: False
