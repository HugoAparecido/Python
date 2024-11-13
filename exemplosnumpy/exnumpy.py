import numpy as np

# Criar e inicializar as matrizes A e B
A = np.array([[1, 14, 6], [4, 5, 9], [13, 11, 2]])
B = np.array([[7, 15, 18], [9, 10, 12], [8, 16, 9]])
# Mostrar as matrizes criadas
print(f"Matriz A:\n{A}")
print(f"Matriz A:\n{B}")
# Verificar o formato dem uma matriz
print(f"\nFormato da matriz A:\n{A.shape}")
# Número de elementos da matriz A
print(f"\nNúmero de elementos da matriz A:\n{A.size}")
# Tipo dos dados da matriz A
print(f"\nTipo de dados da matriz A:\n{A.dtype}")
# Métodos para aritmética com matrizes
# Somar as matrizes
print("\nA soma dos elementos das duas matrizes é")
print(np.add(A, B))
# Subtração das matrizes
print("\nA diferença dos elementos das duas matrizes é")
print(np.subtract(A, B))
# Multiplicação das matrizes
print("\nO produto dos elementos das duas matrizes é")
print(np.multiply(A, B))
# Divisão das matrizes
print("\nA divisão dos elementos das duas matrizes é")
print(np.divide(A, B))
# Multiplicação das matrizes utilizando produto matricial
print("\nO produto matricial é:")
print(np.dot(A, B))
# Mais operações sobre matrizes
print("\nRaiz quadrada de cada elemento da matriz A")
print(np.sqrt(A))
print("\nSomatório dos elemntos de B")
print(np.sum(B))
print("\nSomatório de cada coluna da matriz")
print(np.sum(B, axis=0))
print("\nMatriz transposta de A:")
print(A.T)
print("\n Determinante da matriz B:")
det = np.linalg.det(B)
print(det)
