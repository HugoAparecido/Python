# entrada do usuário
entrada = input()
# dividindo a entrada em uma lista de strings
numeros_str = entrada.split()
# convertendo a lista de stings para uma lista de inteiros
numeros = [int(num) for num in numeros_str]
qtd_pilotos = numeros[0]
qtd_voltas = numeros[1]
qtd_voltas_invalidas = numeros[2]
participantes = []
voltas = []
nomes = 1
while nomes <= qtd_pilotos:
    participantes.append(input())
    nomes += 1
volta = 0
while volta < qtd_voltas:
    voltas.append(str(input()))
    volta += 1
voltas.pop(qtd_voltas_invalidas)
nomes = 0
volta = 0
while volta < qtd_voltas - qtd_voltas_invalidas:
    while nomes < len(participantes):
        print(participantes[nomes])
        '''if participantes[nomes][-4] != '.' and participantes[nomes][0] == voltas[volta][0]:'''
        participantes[nomes] += voltas[volta][3:]
        print(participantes[nomes])
        nomes += 1
    print(voltas[volta])
    volta += 1
nomes = 1
primeiro_lugar = participantes[0]
while nomes <= qtd_pilotos:
    nomes += 1
saida = 1
while saida <= qtd_pilotos:
    print(str(saida) + ' ' + participantes[saida - 1])
    saida += 1
