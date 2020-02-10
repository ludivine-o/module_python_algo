import struct

# on enregistre un entier, un réel et 4 caractères
integer = 10
string = "Python is fun !"

# ouverture, lecture et ecriture se fait de la meme maniere que pour un fichier texte.
# Il suffit de rajouter un b apres le choix du type : wb, rb,


# écriture
def
    with open("test.bin", "wb") as file:
    # le module struct.pack permet d'ecrire
    # (write(struct.pack( type de donnée, donnée)
        file.write(struct.pack("i", integer))
        octets = string.encode("ascii")
        file.write(struct.pack("4s", octets))

# lecture
with open("info.bin", "rb") as file:
    i = struct.unpack("i", file.read(4))
    x = struct.unpack("d", file.read(8))
    s = struct.unpack("4s", file.read(4))

def write_bin(file_name, text):
    with open(file_name, "wb") as bin_file:
        bin_file.write(b"COUCOU ")
        bin_file.write(bytes(str(text), encoding='utf8'))


# affichage pour vérifier que les données ont été bien lues
print(i)
print(x)
print(s)




# with open('fichier.bin', 'rb') as f:
#     donnees = f.read(16)
#     texte = donnees.decode('utf-8')
#
# with open('fichier.bin', 'wb') as f:
#     texte = 'Python est amusant'
#     f.write(texte.encode('utf-8'))
#
