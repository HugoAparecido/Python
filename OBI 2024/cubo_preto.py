N = int(input())
VCubo = N**3
nenhuma = 0
uma = 0
duas = 0
tres = 8
if N != 2:
  nenhuma = (N-2) ** 3
  uma = 6 * (N-2) ** 2
  duas = VCubo - 8 - nenhuma - uma
print(nenhuma)
print(uma)
print(duas)
print(tres)