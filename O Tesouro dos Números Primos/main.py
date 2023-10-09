def primo(numerous):
    if numerous == 1:
        return False
    i = 2
    while i * i <= numerous:
        if numerous % i == 0:
            return False
        i += 1
    return True


x = int(input())  # trasnforma o valor digitado no console em inteiro e armazena na variável x
primos = []
for n in range(1, x + 1):  # para n entre 1 e x + 1
    if primo(n):
        primos.append(str(n))  # Trnasforma o inteiro n em string e adiciona ela ao vetor primos
print(' '.join(primos))  # join percorre todos os valores do vetor primos
