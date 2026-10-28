
import random

#Setting Variables
total: float = 0
cart = []
is_Shopping = True
is_Choosing = True
shop_category = 0
user_budget = 15


# Dictionary + Prices

}


#Code For Entering Shop
print("Welcome to Slow Way!\n")

while is_Shopping:
    while True:
        # --- CHOOSING CATEGORY --- #
        print(f"Looks like you have a budget of ${user_budget}! What are you looking for today?")
        for i, category in enumerate(Shop):
            print(f"[{i + 1}] {category}") # prints [number] "Item Name"

        user_category = int(input("Type the number of the item you want here:"))
def print_category() -> None:
    for i, category in enumerate(Shop):
        print(f"[{i + 1}] {category}") # prints [number] "Item Name"
        
def print_product(userNum: int) -> None:
    category = category_logic(userNum)
    print("What item would you like?")
    print("[0] Go Back")
    for i, item in enumerate(category):
        print(f"[{i + 1}] ${category[item]:.2f} for {item}") #prints [number] "Item Name" for "Price"

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
@@ -108,39 +111,59 @@
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

