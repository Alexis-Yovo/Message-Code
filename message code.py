import random

# On définit 2 types de listes pour faire le cryptage
liste_clair = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
liste_code = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26']

# L'utilisateur saisit un message clair
message_clair = input('Saisir un message clair: ')
message_code = ""

# On doit parcourir chaque lettre de message clair
for lettre in message_clair:
    indice = liste_clair.index(lettre)
    message_code += liste_code[indice]

print("Message codé:", message_code)
