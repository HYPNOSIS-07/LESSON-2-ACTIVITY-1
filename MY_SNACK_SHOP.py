snack_name = "Chocolate" 
price = 67.67 

quantity = 67 

is_available = True # bool — True or False

print("Snack:", snack_name)

print("Price: $", price)

print("In Stock:", quantity)

print("Available?", is_available)

print(type(snack_name))

print(type(price))

print(type(quantity))

print(type(is_available))

total = price * quantity

print("Total value: $", total)

print("Sale price: $", price - 0.25)

print("Double stock:", quantity * 2)
# PART 3 — COMPARISON OPERATORS

print("Is price under $20?", price < 20)

print("More than 100 in stock?", quantity > 100)

print("Is price exactly $67.67?", price == 67.67)

shop_name = "Happy" + " " + "Meals"

print("Shop name:", shop_name)

print("Letters in snack name:", len(snack_name))

print("First letter:", snack_name[0])
# PART 5 — SWAPPING VALUES

price_a = 67.67

price_b = 70

print("Before:", price_a, "and", price_b)

temp = price_a

price_a = price_b

price_b = temp

print("After:", price_a, "and", price_b)