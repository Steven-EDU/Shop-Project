"""
    First Project -- main.py

    Steven, Salma, Ethil

    
"""

import random

def print_receipt(cart: list[str], total: float, user_budget: float) -> None:
    """Display the shopping receipt."""
    print("")
    print("--- Receipt ---")
    for i, item in enumerate(cart):
        print(f"[{i + 1}] {item}")
    print("---         ---")
    print(f"Your total is ${total:.2f}")
    print(f"Your change is ${user_budget:.2f}")
    print("---------------")



def call_user_input() -> int:
    """
        Asks user for input
        Prevents errors
    """
    while True:
        try:
            userNum = int(input("Type the number of the selection you would like to make:"))
            
        except (ValueError, IndexError):
            print("Try typing that again please!")
            continue
        
        userNum = userNum - 1
            
        if userNum < -1 or userNum > 3:
            print("Try typing that again please!")
            continue

        if userNum == -1: #Go back option
            return -1
        return userNum

def stage_1(original_shop:dict[str, dict[str, float]]) -> dict[str, float] | None:
    """
   User is able to select store category.
   Display's items within category
    """
    for i, category in enumerate(original_shop):
        print(f"[{i + 1}] {category}") # prints [number] "Item Name"

    category_index: int = call_user_input()
    
    if category_index == -1:
        return None
    
    category_list = list(original_shop.keys())
    user_cat_name = category_list[category_index]
    user_cat_dict = original_shop[user_cat_name]
    
    return user_cat_dict

def stage_2(category:dict[str, float], budget:float) -> tuple[str| None, float, float]:
    """
    Display shop items in category.
    Checks if user can afford it in their budget.
    """
    while True:
        print("What item would you like?")
        print("[0] Go Back")
        for i, item in enumerate(category):
            print(f"[{i + 1}] ${category[item]:.2f} for {item}") #prints [number] "Item Name" for "Price"

        item_Index:int = call_user_input() #Go back option
        if  item_Index == -1:
            return None, 0.0, budget
        if item_Index >= 3: #Catches if user selects category above range
            print("Try that again please")
            continue
        
        item_list = list(category.keys())
        item_name = item_list[item_Index]
        item_price = category[item_name]

        if budget < item_price:
            print(f"You can't afford that! You only have ${budget:.2f}!")
        
        else:
            budget = budget - item_price
            break

    return item_name, item_price, budget


def gambling(cart: list[str], total: float, user_budget:float)-> tuple[float, float]:
    """
    Checks if Lottery ticket in cart.
    Generates a random number for user winning.
    Adds winnings to budget.
    """
    while "$10 Ticket" in cart or "$100 Ticket" in cart:
        print("")
        print("You have a ticket!! Would you like to redeem it?")
        choice = input("Type here (Yes/No): ")

        if choice.lower() != "yes":
            break
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
    return total, user_budget

def preCheckout(total: float, budget: float, cart:list[str]) -> bool:

    """
    Display's total and shopping list.
    Asks if they want to continue shopping.
    """
    print("")
    print("--- SHOPPING LIST ---")
    for i, item in enumerate(cart): # https://realpython.com/python-enumerate/
        print(f"[{i + 1}] {item}")
    print("---         ---")
    print(f"Your total is ${total:.2f}")
    print(f"You have ${budget:.2f} left")
    print("---------------------")
 
    while True:
        print("Would you like to purchase something else? (Yes/No)")
        user_input2 = input("type here: ").lower()
        print("")
        if user_input2 == "no":
            return False
        if user_input2 == "yes":
            return True
        else:
            print("Try typing that again please!")


def main() -> None:
    """
    Main function for the shopping program.
    Contains shop and mechanism for shopping logic.
    """
    # Dictionary + Prices
    Shop: dict[str, dict[str, float]] = {
        "Snacks": {"Chips": 2.50, "Cookies": 3.20,"Pretzels": 2.48},
        "Food":  {"Milk": 2.87,"Bread": 1.82,"Eggs": 3.89},
        "Drinks": {"Water": 1.00, "Juice": 1.50, "Soda": 2.15},
        "Lottery_Ticket": {"$10 Ticket": 10.0, "$100 Ticket": 100.0}
        }
    
    total: float = 0
    cart: list[str] = []
    budget= 15.00

    print("Welcome to Slow Way!\n")
    
    #shopping loop, handles buying items logic, and user interaction.
    is_shopping: bool= True
    while is_shopping:
        print(f"Looks like you have a budget of ${budget:.2f}! What are you looking for today?")
        
        chosen_category:dict[str, float] = stage_1(Shop)
        if chosen_category is None:
            continue
        
        chosen_item, item_price, budget = stage_2(chosen_category, budget)
        if chosen_item is None:
            continue

        cart.append(chosen_item)
        total+= item_price
        total, budget= gambling(cart, total, budget)
        is_shopping = preCheckout(total, budget, cart)

    print_receipt(cart, total, budget)
    print("Thanks for shopping at Slow way!")

if __name__ == "__main__":
    main()
