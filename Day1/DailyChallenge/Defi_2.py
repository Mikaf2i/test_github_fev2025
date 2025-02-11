# Défi 2 : Supprimer les caractères consécutifs en double d'une chaîne

# Demande à l'utilisateur de saisir un mot
user_word = input("Entrez un mot: ")

# Crée une nouvelle chaîne sans caractères consécutifs en double
result = ""

for i in range(len(user_word)):
    if i == 0 or user_word[i] != user_word[i - 1]:
        result += user_word[i]

# Affiche le résultat
print(result)
