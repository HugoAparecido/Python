linha = input().split()
N = int(linha[0])
Q = int(linha[1])
numeros = input().split()
while Q:
  linha_atual = input().split()
  potencial = []
  numeros_atual = numeros[int(int(linha_atual[0])-1):int(linha_atual[1])]
  for indice, caractere in enumerate(numeros_atual):
    for indice_segundo, segundo_caracter in enumerate(numeros_atual):
      if (indice_segundo != indice):
        potencial.append(int(str(caractere) + str(segundo_caracter)))
  print(sum(potencial))
  Q -= 1