
entrees={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total=0.0 # Initialize total cost

while True:
     try:
        order = input("Item: ").title()

     #check if order in dict
        if order in entrees:
            print(f'Item: {order}')
            price=entrees.get(order)
            total+= price
            print(f'Total: ${total:.2f}')

     except EOFError:
         print()
         break

