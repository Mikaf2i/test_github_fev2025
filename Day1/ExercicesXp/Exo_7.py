#  Exercice 7 : Liste
basket = ["Banana", "Apples", "Oranges", "Blueberries"]

basket.remove("Banana")  # Supprimer Banana
basket.remove("Blueberries")  # Supprimer Blueberries
basket.append("Kiwi")  # Ajouter Kiwi
basket.insert(0, "Apples")  # Ajouter Apples au début

print("Nombre de pommes :", basket.count("Apples"))  # Compter les pommes

basket.clear()  # Vider la liste
print(basket)  # Afficher la liste vide