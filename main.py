"""
    First Project -- main.py

    Steven, Salma, Ethil

    
"""

import random



# Dictionary + Prices
Shop = {
    "Snacks": {"Chips": 2.50, "Cookies": 3.20,"Pretzels": 2.48},
    "Food":  {"Milk": 2.87,"Bread": 1.82,"Eggs": 3.89},
    "Drinks": {"Water": 1.00, "Juice": 1.50, "Soda": 2.15},
    "Lottery_Ticket": {"$10 Ticket": 10.0, "$100 Ticket": 100.0}
}




def print_category() -> None:
    for i, category in enumerate(Shop):
        print(f"[{i + 1}] {category}") # prints [number] "Item Name"
        
def print_product(userNum: int) -> None:
    category = category_logic(userNum)
    print("What item would you like?")
    print("[0] Go Back")
    for i, item in enumerate(category):
        print(f"[{i + 1}] ${category[item]:.2f} for {item}") #prints [number] "Item Name" for "Price"


def category_logic(userNum: int) -> dict[str, float]:
    shopList = list(Shop.keys())
    user_category = Shop[shopList[userNum - 1]]
    return user_category

def call_user_input() -> int:
    """
        Asks user for input
        Prevents errors
    """
    userNum = int(input("Type the number of the selection you would like to make:"))
    userNum = userNum - 1
    if userNum < -1 or userNum > 3:
        print("Try typing that again please!")
        call_user_input()
    elif userNum == -1:
        return 0
    else:
        return userNum


def shop_logic(itemIndex, categoryIndex, cart: list[str], budget):
    item_prices = list(Shop[categoryIndex].values())   # Unit 12.3  -- dict.values
    
    
    if budget < item_prices[itemIndex]:
        print(f"You can't afford that! You only have ${budget:.2f}!")
    else:
        budget = budget - item_prices
        checkedItem = list(Shop[categoryIndex].keys())
        cart.append(checkedItem[itemIndex])
        return cart, budget
    
def purchase_sequence(total, cart, budget):
    """
    output:
    - shop_category

    """
    #Code For Entering Shop
    print("Welcome to Slow Way!\n")
    print(f"Looks like you have a budget of ${user_budget}! What are you looking for today?")
    print_category()
    userCategory = call_user_input()
    print_product(userCategory)
    userItem = call_user_input()

    cart, budget = shop_logic(userCategory, userItem, cart, budget)

def gamble():
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
def preCheckout():
    """
    item
    item_prices
    user_item
    cart
    """

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

def print_receipt(final_cart: list[str]) -> None:
    print("")
    print("--- Receipt ---")
    for i, paid_item in enumerate(final_cart): # https://realpython.com/python-enumerate/
        print(f"[{i + 1}] {paid_item}")
    print("---         ---")
    print(f"Your total is ${total:.2f}")
    print(f"Your change is ${user_budget:.2f}")
    print("---------------")

    print("Thank you for shopping at Slow Way!!\n\n")
    return



def main() -> None:
    #Setting Variables
    total: float = 0
    cart = []
    user_budget = 15
    purchase_sequence(total, cart, user_budget)

    print_receipt(cart)
    pass

if __name__ == "__main__":
    main()


