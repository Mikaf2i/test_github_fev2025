# 🌟 Exercice 1 : Bonjour le monde
print("Hello world\nHello world\nHello world\nHello world")

# 🌟 Exercice 2 : Un peu de maths
resultat = (99 ** 3) * 8
print(resultat)

# 🌟 Exercice 3 : Comment t'appelles-tu ?
mon_nom = "TonNomIci"  # Remplace par ton vrai nom
nom_utilisateur = input("Quel est ton nom ? ")

if nom_utilisateur == mon_nom:
    print("Wow ! On a le même nom ! 😃")
else:
    print(f"Enchanté {nom_utilisateur}, joli nom ! 😊")

# 🌟 Exercice 4 : Assez grand pour faire des montagnes russes
taille = int(input("Quelle est votre taille en cm ? "))

if taille > 145:
    print("Vous êtes assez grand pour monter à bord ! 🎢")
else:
    print("Désolé, vous devez encore grandir un peu. 😔")

# 🌟 Exercice 5 : Numéros préférés
my_fav_numbers = {7, 13, 42}  # Mets tes numéros préférés
my_fav_numbers.update({99, 100})  # Ajoute deux nombres
my_fav_numbers.remove(max(my_fav_numbers))  # Supprime le dernier nombre

friend_fav_numbers = {3, 14, 27}  # Numéros de ton ami

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

# 🌟 Exercice 6 : Tuple
# Réponse : Non, on ne peut pas modifier un tuple directement car il est immuable.
mon_tuple = (1, 2, 3)
nouveau_tuple = mon_tuple + (4, 5)
print(nouveau_tuple)

# 🌟 Exercice 7 : Liste
basket = ["Banana", "Apples", "Oranges", "Blueberries"]

basket.remove("Banana")  # Supprimer Banana
basket.remove("Blueberries")  # Supprimer Blueberries
basket.append("Kiwi")  # Ajouter Kiwi
basket.insert(0, "Apples")  # Ajouter Apples au début

print("Nombre de pommes :", basket.count("Apples"))  # Compter les pommes

basket.clear()  # Vider la liste
print(basket)  # Afficher la liste vide

# 🌟 Exercice 8 : Commandes de sandwichs
sandwich_orders = [
    "Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", 
    "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", 
    "Pastrami sandwich"
]

print("Désolé, il n'y a plus de Pastrami ! 😕")
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")  # Retirer tous les pastramis

finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop(0)  # Retirer le premier sandwich
    print(f"I made your {sandwich}")  # Message client
    finished_sandwiches.append(sandwich)  # Ajouter aux sandwichs finis

print("\nTous les sandwichs préparés :", finished_sandwiches)
