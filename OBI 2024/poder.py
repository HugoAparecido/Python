def pegar_vizinho_nao_nulo_minimo(arr, pos):
  """
  Encontra o menor vizinho não nulo em ambos os lados da posição dada em `pos` no array `arr`.
    
  Args:
  arr (list): O array de onde buscar os vizinhos.
  pos (int): A posição atual no array.
    
  Returns:
  int ou None: O menor valor do vizinho não nulo ou `None` se não houver tal vizinho.
  """
  menor_vizinho = None
    
  # Verifica o vizinho à esquerda
  for i in range(pos - 1, -1, -1):
      if arr[i] is not None:
        if menor_vizinho is None or arr[i] < menor_vizinho:
                menor_vizinho = arr[i]

  # Verifica o vizinho à direita
  for i in range(pos + 1, len(arr)):
    if arr[i] is not None:
      if menor_vizinho is None or arr[i] < menor_vizinho:
        menor_vizinho = arr[i]

    return menor_vizinho
linha = input().split()
matriz = []
controlador = int(linha[0])
while controlador:
  matriz.append([int(num) for num in input().split()])
  controlador -= 1
print(matriz)
print(matriz[0])
# for i in matriz: