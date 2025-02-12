class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height


    def bark(self):
        print(f"{self.name} fait ouaf ouaf!")

    def jump(self):
        print(f"{self.name} fait des sauts {self.height*2} cm de haut!")

davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Teacup", 20)
davids_dog.bark()
davids_dog.jump()
sarahs_dog.bark()
sarahs_dog.jump()

def highest_dog(dogs):
    highest_dog_height = 0
    highest_dog = None  
    for dog in dogs:
        if dog.height > highest_dog_height:
            highest_dog_height = dog.height  
            highest_dog = dog  
    return highest_dog

# Trouver le plus grand chien
highest = highest_dog([davids_dog, sarahs_dog])
print(f"Le chien le plus grand est {highest.name}, il mesure {highest.height} cm.")



 