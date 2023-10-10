entrant = input()
vogais = 0
frasco = 0
for letra in entrant:
    if (letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U' or letra == 'a' or letra == 'e' or 
            letra == 'i' or letra == 'o' or letra == 'u'):
        vogais += 1
if vogais % 3 == 0:
    frasco = 0
elif vogais % 3 == 1:
    frasco = 1
elif vogais % 3 == 2:
    frasco = 2
print('frasco ' + str(frasco))
