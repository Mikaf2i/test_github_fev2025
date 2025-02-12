class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

cat1 = Cat("Mika", 23)
cat2 = Cat("Sarah", 31)
cat3 = Cat("Olga", 38)


def oldest_cat(cats):
    oldest_age = 0
    for cat in cats:
        if cat.age > oldest_age:
            oldest_age = cat.age
            oldest_cat = cat
    return oldest_cat

oldest = oldest_cat([cat1, cat2, cat3])
print(f"The oldest cat is {oldest.name}, aged {oldest.age}.")
            