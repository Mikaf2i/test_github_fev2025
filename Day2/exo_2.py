family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
def calculate_price(age):
    if age < 3 :
        return 0
    elif age  > 3 and age < 12 :
        return 10
    else:
        return 15
    

cout_total = 0
for name, age in family.items():
        price = calculate_price(age)
        print(f"{name} doit payer {price} euros")
        cout_total += price
print(f"la famille doit payer {cout_total} euros")