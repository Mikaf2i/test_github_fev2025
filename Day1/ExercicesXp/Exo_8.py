#  Exercice 8 : Commandes de sandwichs
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
