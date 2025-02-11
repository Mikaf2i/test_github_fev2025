# Exercice 1 : Prédire les résultats des extraits de code

# Extrait 1
print(3 <= 3 < 9)  # True : 3 <= 3 est vrai et 3 < 9 est aussi vrai.

# Extrait 2
print(3 == 3 == 3)  # True : 3 == 3 et 3 == 3 sont tous les deux vrais.

# Extrait 3
print(bool(0))  # False : 0 est interprété comme False en booléen.

# Extrait 4
print(bool(5 == "5"))  # False : 5 (int) n'est pas égal à "5" (str).

# Extrait 5
print(bool(4 == 4) == bool("4" == "4"))  # True : les deux sont vrais, donc l'expression est True.

# Extrait 6
print(bool(bool(None)))  # False : None est False, et donc bool(None) donne False.

# Extrait avec les variables x, y, a et b
x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

print("x is", x)  # True
print("y is", y)  # False
print("a:", a)  # 5
print("b:", b)  # 10


# Exercice 2 : Le mot le plus long sans caractère spécifique

longest_phrase = ""
while True:
    user_input = input("Entrez une phrase sans le caractère 'A' : ")
    if 'a' not in user_input.lower() and len(user_input) > len(longest_phrase):
        longest_phrase = user_input
        print("Félicitations ! Nouve
              lle phrase la plus longue sans 'A'.")


