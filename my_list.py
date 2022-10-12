# A simple python program that stores a collection of items in a list and then prints
# different personalized messages for each item in the collection.

cars = ["tundra", "toyota", "benz", "ford"]

messages = ["I would love to own a", "I love", "are super clean", "is my favourite"]

print(f"{messages[0]} {cars[0].title()} ride.")
print(f"\n{messages[1]} {cars[1].title()} cars.")
print(f"\n{cars[2].title()} {messages[2].title()} rides.")
print(f"\n{cars[3].title()} {messages[3].title()} ride.")
