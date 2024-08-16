def verificar_simetria(array):
    n = len(array)
    for i in range(n // 2):
        if array[i] != array[n - i - 1]:
            return False
    return True
def substituir_valores(array, comeco):
        array[comeco] = array[comeco] + array[comeco + 1]
        del array[comeco+1]
N = input()
linha = input().split()
Numeros = [int(num) for num in linha]
Mudancas = [0]
for i in range(len(Numeros)):
    print(i)
    Mudancas.append(0)
    j = i
    while (not verificar_simetria(Numeros)) or int(5/2) > j:
        Mudancas[i+1] += 1
        substituir_valores(Numeros, j)
        print(Numeros)
        print(Mudancas)
        j += 1
        print(j)
    Numeros = [int(num) for num in linha]
Mudancas = sorted(Mudancas)
print(Mudancas[0])