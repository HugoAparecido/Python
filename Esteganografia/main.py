entrant = input()
nova_string = ""
texto_final = ""
for letra in entrant:
    if letra.isupper():
        nova_string += 'B'
    elif letra.islower():
        nova_string += 'A'
for i in range(0, len(nova_string), 5):
    substring = nova_string[i:i + 5]
    print(substring)
    if substring == "AAAAA":
        texto_final += "A"
    elif substring == "AAAAB":
        texto_final += "B"
    elif substring == "AAABA":
        texto_final += "C"
    elif substring == "AAABB":
        texto_final += "D"
    elif substring == "AABAA":
        texto_final += "E"
    elif substring == "AABAB":
        texto_final += "F"
    elif substring == "AAABB":
        texto_final += "G"
    elif substring == "AABBB":
        texto_final += "H"
    elif substring == "ABAAA":
        texto_final += "I"
    elif substring == "ABAAB":
        texto_final += "J"
    elif substring == "ABABA":
        texto_final += "K"
    elif substring == "ABABB":
        texto_final += "L"
    elif substring == "ABBAA":
        texto_final += "M"
    elif substring == "ABBAB":
        texto_final += "N"
    elif substring == "ABBBA":
        texto_final += "O"
    elif substring == "ABBBB":
        texto_final += "P"
    elif substring == "BAAAA":
        texto_final += "Q"
    elif substring == "BAAAB":
        texto_final += "R"
    elif substring == "BAABA":
        texto_final += "S"
    elif substring == "BAABB":
        texto_final += "T"
    elif substring == "BABAA":
        texto_final += "U"
    elif substring == "BABAB":
        texto_final += "V"
    elif substring == "BABBA":
        texto_final += "W"
    elif substring == "BABBB":
        texto_final += "X"
    elif substring == "BBAAA":
        texto_final += "Y"
    elif substring == "BBAAB":
        texto_final += "Z"
    elif substring == "BBBBB":
        texto_final += " "
print(texto_final)
