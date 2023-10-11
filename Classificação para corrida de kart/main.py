def minimo(lista):
    minimo_atual = lista[0]  # Começa com o primeiro elemento da lista
    for item in lista[1:]:  # Percorre o restante da lista
        if item < minimo_atual:
            minimo_atual = item  # Encontra um novo mínimo
    return minimo_atual
qtd_pilotos = int(input())
qtd_voltas = int(input())
qtd_voltas_invalidas = int(input())
participantes = [[], []]
voltas = []
nomes = 1
while nomes <= qtd_pilotos:
    participantes.append(input())
    nomes += 1
volta = 1
nomes = 1
while volta <= qtd_voltas:
    voltas.append(str(input()))
    while nomes <= qtd_pilotos:
        if str(voltas[volta-1][0] + voltas[volta-1][1] + voltas[volta-1][2]) == str(participantes[volta-1][0] +
                                                                                    participantes[volta-1][1].lower() +
                                                                                    participantes[volta-1][2].lower()):
            participantes[volta-1].append(" " + voltas[volta-1])
        nomes += 1
    volta += 1
voltas.pop(qtd_voltas_invalidas)
nomes = 1
primeiro_lugar = participantes[0]
while nomes <= qtd_pilotos:
    nomes += 1
saida = 1
while saida <= qtd_pilotos:
    print(str(saida) + ' ' + participantes[saida-1])
    saida += 1
