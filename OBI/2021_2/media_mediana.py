linha = input()
A, B = linha.split(" ")
A = int(A)
B = int(B)
C = 0
mediana = sorted([A, B, C])
while ((A+B+C)/3) != mediana[1]:
    C += 1
    mediana = sorted([A, B, C])
print(C)
