"""
    First Project -- main.py

    Steven, Salma, Ethil

    
"""

import random

def print_receipt(cart: list, total: float, user_budget: float) -> None:
    """Display the shopping receipt."""
    print("")
    print("--- Receipt ---")
    for i, item in enumerate(cart):
        print(f"[{i + 1}] {item}")
    print("---         ---")
    print(f"Your total is ${total:.2f}")
    print(f"Your change is ${user_budget:.2f}")
    print("---------------")
    
#Setting Variables
total: float = 0
cart = []
is_Shopping = True
is_Choosing = True
shop_category = 0
user_budget = 15


# Dictionary + Prices
Shop = {
    "Snacks": {"Chips": 2.50, "Cookies": 3.20,"Pretzels": 2.48},
    "Food":  {"Milk": 2.87,"Bread": 1.82,"Eggs": 3.89},
    "Drinks": {"Water": 1.00, "Juice": 1.50, "Soda": 2.15},
    "Lottery_Ticket": {"$10 Ticket": 10.0, "$100 Ticket": 100.0}
}

#test
#Code For Entering Shop
print("Welcome to Slow Way!\n")

while is_Shopping:
    while True:
        # --- CHOOSING CATEGORY --- #
        print(f"Looks like you have a budget of ${user_budget}! What are you looking for today?")
        for i, category in enumerate(Shop):
            print(f"[{i + 1}] {category}") # prints [number] "Item Name"

        user_category = int(input("Type the number of the item you want here:"))

        if user_category > 0 and user_category <= 4:
            shop_category = Shop[list(Shop.keys())[user_category - 1]]  # Takes the number from user, finds the according category, assigns the according dictionary to the variable
            break

        else:
            print("Try typing that again please!")


    while True:
        # --- CHOOSING ITEM --- #
        bought_item = False
        print("")


        #DISPLAY
        print("What item would you like?")
        print("[0] Go Back")
        for i, item in enumerate(shop_category):
            print(f"[{i + 1}] ${shop_category[item]:.2f} for {item}") #prints [number] "Item Name" for "Price"
            
        # USER INPUT
        user_item = int(input("Type the number of the item you want here: "))

        # SHOP LOGIC
        if user_item == 0: 
            break # "Go Back" Button -- Breaks and loops back to "While is_Shopping"

        elif user_item > 0 and user_item <= 4:
            item_prices = list(shop_category.values())   # Unit 12.3  -- dict.values
            user_item -= 1
            if user_budget < item_prices[user_item]:
                print(f"You can't afford that! You only have ${user_budget:.2f}!")
            else:
                cart.append(list(shop_category.keys())[user_item])
                bought_item = True
                break # Since brought_item is TRUE, it goes into checkout

        else:
            print("Try typing that again please!")



    if bought_item == True:
        #GAMBLE LOOP
        while "$10 Ticket" in cart or "$100 Ticket" in cart:
            print("")
            print("You have a ticket!! Would you like to redeem it?")
            choice = input("Type here (Yes/No): ")

            if choice.lower() == "yes":
                if "$10 Ticket" in cart:
                    cart.remove("$10 Ticket")
                    random_number = random.randint(0,50)
                    total -= 10
                    user_budget += random_number
                    print("")
                    print(f"Congrats! You won ${random_number} from a $10 Ticket!!")

                elif "$100 Ticket" in cart:
                    cart.remove("$100 Ticket")
                    random_number = random.randint(0,500)
                    total -= 100
                    user_budget += random_number
                    print("")
                    print(f"Congrats! You won ${random_number} from a $100 Ticket!!")

                else:
                    break
            else:
                break

        # Pre-Checkout -- Display total and ask if they desire to shop more
        total += item_prices[user_item]
        user_budget = user_budget - item_prices[user_item]

        # Receipt
        print("")
        print("--- SHOPPING LIST ---")
        for i, item in enumerate(cart): # https://realpython.com/python-enumerate/
            print(f"[{i + 1}] {item}")
        print("---         ---")
        print(f"Your total is ${total:.2f}")
        print(f"You have ${user_budget:.2f} left")
        print("---------------")
        print("Would you like to purchase something else? (Yes/No)")
        user_input2 = input("type here: ")
        print("")
        if user_input2 == "no" or user_input2 == "No":
            break



print("")
print("--- Receipt ---")
for i, item in enumerate(cart): # https://realpython.com/python-enumerate/
    print(f"[{i + 1}] {item}")
print("---         ---")
print(f"Your total is ${total:.2f}")
print(f"Your change is ${user_budget:.2f}")
print("---------------")

print("Thank you for shopping at Slow Way!!\n\n")
quit()



