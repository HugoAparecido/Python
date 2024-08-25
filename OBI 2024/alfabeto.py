linha = input().split()
K = linha[0]
N = linha[1]
palavras_alien = list(input())
palavras_normal = list(input())
mensagem_escrita = True
for i in palavras_normal:
  if i in palavras_alien:
    mensagem_escrita = True
  else:
    mensagem_escrita = False
    break
if mensagem_escrita:
  print('S')
else:
  print('N')