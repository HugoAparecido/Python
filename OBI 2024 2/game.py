N = int(input())
posicoes = [str(letra) for letra in input()]
# E = 2i
# D = 2i+1
porta = 1
for letra in posicoes:
    if letra == "E":
        porta *= 2
    else:
        porta = porta * 2 + 1
print(porta)
