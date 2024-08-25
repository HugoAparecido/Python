linha = input().split()
N = int(linha[0])
Q = int(linha[1])
numeros = input().split()
# Loop para processar cada uma das Q consultas
for _ in range(Q):
    linha_atual = input().split()
    inicio = int(linha_atual[0]) - 1
    fim = int(linha_atual[1])
    numeros_atual = numeros[inicio:fim]
    # Calcular a soma dos potenciais diretamente
    soma_potenciais = 0
    tamanho = len(numeros_atual)
    
    for i in range(tamanho):
        for j in range(tamanho):
            if i != j:
                soma_potenciais += int(numeros_atual[i] + numeros_atual[j])
    
    print(soma_potenciais)
