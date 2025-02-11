# Défi 1 : Générer les multiples d'un nombre jusqu'à une longueur spécifiée

# Demande à l'utilisateur de saisir un nombre et une longueur
number = int(input("Entrez un nombre: "))
length = int(input("Entrez la longueur: "))

# Génération de la liste des multiples
multiples = [number * i for i in range(1, length + 1)]

# Affichage de la liste des multiples
print(multiples)

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
