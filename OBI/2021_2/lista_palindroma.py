N = input()
Numeros = input().split()
for i in range(len(Numeros)):
    
    if(Numeros[i] == Numeros[N-i+1]):
        break