linha = input().split()
matriz = []
controlador = int(linha[0])
while controlador:
  matriz.append([int(num) for num in input().split()])
  controlador -= 1
print(matriz)
print(matriz[0])
for i in matriz:
  # for j in matriz[i]:
    print(matriz[i])
    # poder = []
    # inverter = +1
    # local = i
    # while len(matriz) > 1:
    #   if(local < 0):
    #     local = 0
    #     inverter = -1
    #   if(local > len(matriz) + 2):
    #     local = len(matriz) - 1
    #     local = 1
    #   if(matriz[0][local+inverter] < matriz[0][local]):
    #     print(matriz[0][local] + matriz[0][local + inverter])
    #     del matriz[0][i + inverter]
    #     poder.append(matriz[0][0])
    #     print(poder)
    #   elif(matriz[0][local - inverter] < matriz[0][local]):
    #     print(matriz[0][local] + matriz[0][local - inverter])
    #     del matriz[0][i + inverter]
    #     poder.append(matriz[0][0])
    #     print(poder)
    # print("".join(poder))