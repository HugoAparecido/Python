N = int(input())
Numeros = [int(n) for n in str(N)]
numeroMudancas = 0
if N % 2 != 0:
    while N != 0:
        print(Numeros)
        N -= Numeros[0]
        numeroMudancas += 1
        if (N < 0) or N == 0:
            break
        Numeros = [int(n) for n in str(N)]
        Numeros.sort(reverse=True)
        N -= Numeros[0]
        numeroMudancas += 1
        print(Numeros)
        Numeros = [int(n) for n in str(N)]
        Numeros.sort(reverse=True)
else:
    while N != 0:
        print(Numeros)
        Numeros.sort(reverse=True)
        N -= Numeros[0]
        numeroMudancas += 1
        if (N < 0) or N == 0:
            break
        Numeros = [int(n) for n in str(N)]
        Numeros.sort(reverse=True)
        N -= Numeros[0]
        numeroMudancas += 1
        print(Numeros)
        Numeros = [int(n) for n in str(N)]
        Numeros.sort(reverse=True)
print(numeroMudancas)
