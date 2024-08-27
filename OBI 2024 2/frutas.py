entrada = input().split()
Reais = int(entrada[0])
N = int(entrada[1])
valorAtual = 0
numeroFrutas = 0
Frutas = []
TestedeSoUm = []
while N:
    entradaAtual = input().split()
    Frutas.append({"nome": int(entradaAtual[0]), "valor": int(entradaAtual[1])})
    TestedeSoUm.append(entradaAtual[0])
    N -= 1
TestedeSoUm = list(set(TestedeSoUm))
FrutasOrdenadas = sorted(Frutas, key=lambda x: x["valor"])
FrutasFinal = []
if len(TestedeSoUm) != 1:
    for i in FrutasOrdenadas:
        if not i["nome"] in FrutasFinal:
            FrutasFinal.append(i)
            if valorAtual + i["valor"] > Reais:
                break
            valorAtual += i["valor"]
            numeroFrutas += 1
elif valorAtual + FrutasOrdenadas[0]["valor"] <= Reais:
    numeroFrutas += 1
print(numeroFrutas)
