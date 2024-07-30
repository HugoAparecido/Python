entrada = input().split()
qtdCidades = int(entrada[0])
qtdCaminhos = int(entrada[1])
caminhos = []
destino = input().split()
passou = []
while(qtdCaminhos):
    entradaAtual = input().split()
    caminhos.append(entradaAtual)
    qtdCaminhos -= 1
destinoAtual = [destino[1]]
qtdKilometros = 0
i = 0
while(True):
    for caminho in caminhos:
        if(caminho[0] == destino[0] and caminho[1] == destino[1]):
            qtdKilometros += int(caminho[2])
            break
        elif(caminho[1] == destinoAtual):
            passou.append(caminho)
            destinoAtual.append(caminho[0])
    i += 1
print(passou)
print(f"Percurso:")