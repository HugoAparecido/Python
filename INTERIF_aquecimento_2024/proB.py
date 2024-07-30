palavra = list(input())
elementos = list(set(palavra))
restoQtd = []
for elemento in elementos:
    restoQtd.append(palavra.count(elemento) % 2)
if(restoQtd.count(1) == 1):
    print("1")
else:
    print("0")