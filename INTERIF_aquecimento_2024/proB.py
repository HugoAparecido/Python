palavra = list(input())
elementos = list(set(palavra))
restoQtd = []
print(elementos)
for elemento in elementos:
    restoQtd.append(palavra.count(elemento) % 2)
print(restoQtd)
if(restoQtd.count(1) == 1):
    print(1)
else:
    print(0)