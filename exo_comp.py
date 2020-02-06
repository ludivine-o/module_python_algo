ch_let = ord(input("choisir une lettre : "))
print(ch_let)
lettre = ord('a')
ligne_début = ((ch_let-97)*'.' + str(chr(lettre)) + (ch_let-97)*'.')

# 1ere ligne
print(ligne_début)
pc = ch_let-1-97
pm = 1
lettre += 1


# lignes descendantes
while lettre != ch_let:
    print(pc*"." + str(chr(lettre)) + pm*"." + str(chr(lettre)) + pc*".")
    pc -= 1
    pm += 2
    lettre += 1
# lignes montantes
while lettre != ord("a"):
    print(pc*"." + str(chr(lettre)) + pm*"." + str(chr(lettre)) + pc*".")
    pc += 1
    pm -= 2
    lettre -= 1

# derniere ligne
print(ligne_début)