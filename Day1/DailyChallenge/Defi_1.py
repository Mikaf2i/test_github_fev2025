# Défi 1 : Générer les multiples d'un nombre jusqu'à une longueur spécifiée

# Demande à l'utilisateur de saisir un nombre et une longueur
number = int(input("Entrez un nombre: "))
length = int(input("Entrez la longueur: "))

# Génération de la liste des multiples
multiples = [number * i for i in range(1, length + 1)]

# Affichage de la liste des multiples
print(multiples)