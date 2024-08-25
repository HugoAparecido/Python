def verificar_simetria(array):
    n = len(array)
    for num in range(n // 2):
        if array[num] != array[n - num - 1]:
            return False
    return True


def somar_consecutivos(array, posicao):
    resultado = array
    j = posicao
    qtd_somas = 0
    while not verificar_simetria(resultado) and j < len(resultado):
        qtd_somas += 1
        if j + 1 == len(resultado):
            soma = resultado[j] + resultado[j - 1]
            del resultado[j - 1]
            resultado[j - 1] = soma
        else:
            soma = resultado[j] + resultado[j + 1]
            del resultado[j + 1]
            resultado[j] = soma
        j += 1
    if verificar_simetria(resultado):
        return qtd_somas
    else:
        return None


N = input()
linha = input().split()
Numeros = [int(num) for num in linha]
Mudancas = []
if not verificar_simetria(Numeros):
    for i in range(len(Numeros)):
        Mudancas.append(somar_consecutivos(Numeros, i))
        Numeros = [int(num) for num in linha]
else:
    Mudancas.append(0)
Mudancas = [x for x in Mudancas if x != None]
Mudancas = sorted(Mudancas)
print(Mudancas[0])
