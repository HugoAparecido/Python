import numpy.matlib
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

# Gerar matrizes especiais

# Gerar matriz vazia
V = np.matlib.empty((3, 4))
print("Matriz Gerada:\n", V)

# Gerar matriz preenchida com zeros
Z = np.matlib.zeros((3, 4))
print(f'\nMatriz 3x4 de zeros:\n {Z}')

# Gerar matriz preenchida com uns
U = np.matlib.ones((3, 4))
print(f'\nMatriz 3x4 de uns:\n {U}')

# Gerar matriz preenchida com uns
U2 = np.matlib.ones(shape=10, dtype=int)
print(f'\nArray de uma dimensão de uns:\n {U2}')

# Gerar matriz identidade 5x5
I = np.matlib.eye(5, k=0)
print(f'Matriz identidade 5x5:\n{I}')

I2 = np.matlib.identity(5)
print(f'Matriz identidade 5x5:\n{I2}')

# Remodelar um array 1D em array 2D

vetor = np.array([2, 4, 6, 1, 3, 5])
C = np.reshape(vetor, (2, 3))
print(f'Array original:\n{vetor}')
print(f'Array remodelado 2D:\n{C}')

# Concatenação de matrizes

# Concatenação na vertical
vertical = np.vstack((A, B))
print(f'Matrizes concatenadas na vertical:\n{vertical}')

# Concatenação na horizontal
horizontal = np.hstack((A, B))
print(f'Matrizes concatenadas na horizontal:\n{horizontal}')

# Funções estatísticas em matrizes

print(f'Média: {round(np.mean(A), 2)}')
print(f'Mediana: {np.median(A)}')
print(f'Mediana de cada coluna: {np.median(A, axis=0)}')
print(f'Valor mínimo: {np.min(A)}')
print(f'Valor máximo: {np.max(A)}')
print(f'Desvio padrão: {np.std(A)}')
print(f'25º percentil: {np.percentile(A, 25)}')

# Salvar a matriz em um arquivo de texto
# np.savetxt('dados.txt', B)

# Carregar os dados a partir de um arquivo de texto
dados = np.loadtxt('dados.txt')

print(dados)
