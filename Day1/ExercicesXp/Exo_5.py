#  Exercice 5 : Numéros préférés
my_fav_numbers = {7, 13, 42}  # Mets tes numéros préférés
my_fav_numbers.update({99, 100})  # Ajoute deux nombres
my_fav_numbers.remove(max(my_fav_numbers))  # Supprime le dernier nombre

friend_fav_numbers = {3, 14, 27}  # Numéros de ton ami

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)