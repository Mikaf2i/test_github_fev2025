# 🌟 Exercice 1 : Quelle est la saison ?
mois = int(input("Entrez un mois (1-12) : "))

if 3 <= mois <= 5:
    print("Spring")
elif 6 <= mois <= 8:
    print("Summer")
elif 9 <= mois <= 11:
    print("Autumn")
else:
    print("Winter")

# 🌟 Exercice 2 : Boucle For
for i in range(1, 21):
    print(i)

print("\nNombres avec index pair :")
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# 🌟 Exercice 3 : Boucle While
mon_nom = "TonNomIci"
nom_utilisateur = ""
while nom_utilisateur != mon_nom:
    nom_utilisateur = input("Entrez votre nom : ")
print("Bonjour, nous avons le même nom !")

# 🌟 Exercice 4 : Vérifier l'index
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
nom_recherche = input("Entrez un nom : ")
if nom_recherche in names:
    print(f"L'index de {nom_recherche} est :", names.index(nom_recherche))
else:
    print("Nom non trouvé.")

# 🌟 Exercice 5 : Le plus grand nombre
nb1 = int(input("Input the 1st number: "))
nb2 = int(input("Input the 2nd number: "))
nb3 = int(input("Input the 3rd number: "))
print("The greatest number is:", max(nb1, nb2, nb3))

# 🌟 Exercice 6 : Nombre aléatoire
import random

games_won = 0
games_lost = 0
while True:
    user_number = input("Devinez un nombre entre 1 et 9 (ou 'exit' pour quitter) : ")
    if user_number.lower() == 'exit':
        break
    user_number = int(user_number)
    random_number = random.randint(1, 9)
    if user_number == random_number:
        print("Gagnant !")
        games_won += 1
    else:
        print("Meilleure chance la prochaine fois.")
        games_lost += 1

print(f"Total des parties gagnées : {games_won}")
print(f"Total des parties perdues : {games_lost}")
