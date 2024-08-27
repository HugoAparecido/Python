N = int(input())
valores = [int(valor) for valor in input().split()]
qtd = 0
i = 0
while i < N - 2:
    valoresSem = valores[(i + 1) : -1]
    valoresSem2 = valores[(i + 2) :]
    # print(valoresSem)
    for j in valoresSem:
        # print(valoresSem2)
        for y in valoresSem2:
            if valores[i] < (j + y) and valores[i] + j > y and valores[i] + y > j:
                qtd += 1
        valoresSem2.pop(0)
    i += 1
print(qtd)
