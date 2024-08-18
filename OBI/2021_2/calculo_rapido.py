S = int(input())
A = int(input())
B = int(input())
qtd_somas = 0
while A <= B:
    numero_str = str(A)
    numeros = [int(digito) for digito in numero_str]
    if sum(numeros) == S:
        qtd_somas += 1
    A += 1
print(qtd_somas)
