ch_let = ord(input("choisir une lettre : "))
lettre = ord('a')
ligne_debut = ((ch_let-97)*'.' + str(chr(lettre)) + (ch_let-97)*'.')
# 1ere ligne
print(ligne_debut)
pc = ch_let-1-97
pm = 1
lettre += 1
# lignes debut
while lettre != ch_let:
    print(pc*"." + str(chr(lettre)) + pm*"." + str(chr(lettre)) + pc*".")
    pc -= 1
    pm += 2
    lettre += 1
# lignes fin
while lettre != ord("a"):
    print(pc*"." + str(chr(lettre)) + pm*"." + str(chr(lettre)) + pc*".")
    pc += 1
    pm -= 2
    lettre -= 1
# derniere ligne
print(ligne_debut)