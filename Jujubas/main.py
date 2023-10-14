P = input().split()
P_nums = [int(num) for num in P]
N = int(input())
T = [[], []]
controle = 0
controle2 = 2
while controle < N:
    T.append(controle)
    acertos = 0
    while controle2 < len(P):
        T[controle].append(int(input()))
        if T[controle][controle2] == P_nums[controle2]:
            controle += 1
        controle2 += 1
    controle += 1
M = int(input())
controle = 0
perc_considerar = []
while controle < M:
    perc_considerar.append((float(input()) / 100))
    controle += 1
