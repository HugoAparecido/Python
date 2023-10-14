# entrada do usuário para os números
entrada = input()
# dividindo a entrada em uma lista de strings (a cada espaço terá uma nova posição
numeros_str = entrada.split()
# convertendo a lista de stings para uma lista de inteiros
numeros = [int(num) for num in numeros_str]
# posição 0 corresponde ao número de pilotos
qtd_pilotos = numeros[0]
# posição 1 corresponde ao número de voltas
qtd_voltas = numeros[1]
# posição 2 corresponde ao número de voltas inválidas
qtd_voltas_invalidas = numeros[2]
# declaração de listas (vetores)
participantes = []
voltas = []
melhor_volta = []
# Pegando os nomes dos corredores e colocando-os no vetor participantes
controle = 0
while controle < qtd_pilotos:
    participantes.append(input())
    controle += 1
# Pegando as informações das voltas e colocando-as no vetor voltas
controle = 0
while controle < qtd_voltas:
    voltas.append(input())
    controle += 1
# Retirando as voltas inválidas
voltas.pop(qtd_voltas_invalidas)
controle = 0
while controle < len(voltas):
    # Colocando as primeiras voltas de cada corredor
    if controle < qtd_pilotos:
        melhor_volta.append(voltas[controle])
    # Percorrendo a lista em que está armazenadas as melhores voltas
    else:
        controle2 = 0
        while controle2 < len(melhor_volta):
            # Se a sigla da volta for igual a da melhor volta
            if voltas[controle][0:3] == melhor_volta[controle2][0:3]:
                # Comparando os minutos da volta para ver se eles são menores do que a da melhor volta
                if int(voltas[controle][4]) < int(melhor_volta[controle2][4]):
                    # Deleto primeiro o valor da volta_melhor correspondente a condição acima, e na linha seguinte
                    # adiciono o valor da volta atual, já que ela foi melhor do que a armazenada em melhor_volta
                    del melhor_volta[controle2]
                    melhor_volta.append(voltas[controle])
                # Comparando os segundos e os milissegundos, sendo estes casas decimais dos segundos
                elif voltas[controle][4] == melhor_volta[controle2][4] and not float(
                        voltas[controle][6:]) >= float(melhor_volta[controle2][6:]):
                    # Deleto primeiro o valor da volta_melhor correspondente a condição acima, e na linha seguinte
                    # adiciono o valor da volta atual, já que ela foi melhor do que a armazenada em melhor_volta
                    del melhor_volta[controle2]
                    melhor_volta.append(voltas[controle])
            controle2 += 1
    controle += 1
controle = 0
# Adiciono a melhor_volta a seu participante correspondente
while controle < len(participantes):
    controle2 = 0
    while controle2 < len(melhor_volta):
        if participantes[controle][0] + participantes[controle][1:3].upper() == melhor_volta[controle2][0:3]:
            participantes[controle] += " " + melhor_volta[controle2][4:]
        controle2 += 1
    controle += 1
controle = 1
# Reorganizando a lista em ordem crescente numérica
participantes = sorted(participantes, key=lambda x: int(''.join(filter(str.isdigit, x))))
# Imprimindo os valores
while controle <= qtd_pilotos:
    print(str(controle) + ' ' + participantes[controle - 1])
    controle += 1
