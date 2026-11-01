"""
First Project -- main.py

Steven, Salma, Ethil

A text-based shopping simulator where the user spends a fixed budget and
can gamble on lottery tickets.
"""

import random

# Kept as a named constant so the starting budget can be changed in one place.
STARTING_BUDGET = 15.00


def print_receipt(shopping_cart: list[str], cart_total: float, user_budget: float) -> None:
    """Display the final receipt, with the leftover budget shown as change."""
    print("")
    print("--- Receipt ---")
    for i, item in enumerate(shopping_cart):
        print(f"[{i + 1}] {item}")
    print("---         ---")
    print(f"Your total is ${cart_total:.2f}")
    print(f"Your change is ${user_budget:.2f}")
    print("---------------")


def call_user_input(num_options: int, can_go_back: bool) -> int:
    """
    Ask the user for a menu number until they enter a valid one.

    num_options is how many items the menu lists, and can_go_back says
    whether 0 ("Go Back") is a valid choice.
    """
    # The first menu has nothing to go back to, so 0 is only valid when:
    if can_go_back:
        lowest_choice = 0
    else:
        lowest_choice = 1

    while True:
        # int() raises ValueError on anything that isn't a whole number, so
        # catching it keeps a typo from crashing the program.
        try:
            user_choice = int(input("Type the number of the selection you would like to make: "))
        except ValueError, IndexError:
            print("\nTry typing in a valid answer please!\n")
            continue

        if user_choice < lowest_choice or user_choice > num_options:
            print("\nThat is not an option! Try that again please!\n")
            continue

        # Allows the input to be used as an index
        return user_choice - 1


def stage_1(shop_items: dict[str, dict[str, float]]) -> dict[str, float]:
    """
    Let the user pick a store category.

    Returns that category's items and prices
    """
    for i, category in enumerate(shop_items):
        print(f"[{i + 1}] {category}")

    category_index: int = call_user_input(len(shop_items), False)

    category_list = list(shop_items.keys())
    category_name = category_list[category_index]
    # Doing the logic here and returning a dictionary helps streamline future code

    return shop_items[category_name]


def stage_2(
    category_items: dict[str, float], user_budget: float) -> tuple[str | None, float, float]:
    """
    Let the user pick an item from a category and pay for it.

    Returns the item name, its price, and the remaining budget. The name is
    None (and the budget unchanged) if the user went back.
    """
    while True:
        print("What item would you like?")
        print("[0] Go Back")
        for i, item in enumerate(category_items):
            print(f"[{i + 1}] ${category_items[item]:.2f} for {item}")

        item_index: int = call_user_input(len(category_items), True)

        # The price and budget still have to be returned when going back so
        # the caller can unpack the same three values every time.
        if item_index == -1:
            return None, 0.0, user_budget

        item_list = list(category_items.keys())
        item_name = item_list[item_index]
        item_price = category_items[item_name]

        if user_budget < item_price:
            print(f"You can't afford that! You only have ${user_budget:.2f}!")
        else:
            user_budget = user_budget - item_price
            break

    return item_name, item_price, user_budget


def gambling(
    shopping_cart: list[str],
    cart_total: float,
    user_budget: float,
    ticket_prices: dict[str, float],
) -> tuple[float, float]:
    """
    Offer to redeem any lottery tickets in the cart.

    Redeemed tickets are removed from the cart and its price is taken off the total.
    The prize is added to the budget. 
    
    Returns the updated total and budget.
    """
    # Looping over ticket_prices (instead of checking for each ticket by name) 
    # means a new ticket added to the shop works here automatically.
    while any(ticket in shopping_cart for ticket in ticket_prices):
        print("You have a ticket!! Would you like to redeem it?")
        redeem_choice = input("Type here (Yes/No): ")

        if redeem_choice.lower() != "yes":
            break

        # Redeem one ticket per pass
        # The break keeps the user from redeeming several tickets on a single "yes".
        for ticket_name, ticket_price in ticket_prices.items():
            if ticket_name in shopping_cart:
                shopping_cart.remove(ticket_name)

                winnings = random.randint(0, int(ticket_price * 5))

                cart_total -= ticket_price
                user_budget += winnings
                print("")
                print(f"Congrats! You won ${winnings} from a {ticket_name}!!")
                break

    return cart_total, user_budget


def pre_checkout(cart_total: float, user_budget: float, shopping_cart: list[str]) -> bool:
    """
    Show the cart so far and ask whether the user wants to keep shopping.

    Returns True to keep shopping, or False to head to the receipt.
    """
    print("")
    print("--- SHOPPING LIST ---")
    # Reference for enumerate: https://realpython.com/python-enumerate/
    for i, item in enumerate(shopping_cart):
        print(f"[{i + 1}] {item}")
    print("---         ---")
    print(f"Your total is ${cart_total:.2f}")
    print(f"You have ${user_budget:.2f} left")
    print("---------------------")

    while True:
        print("Would you like to purchase something else? (Yes/No)")
        shop_again = input("type here: ").lower()
        print("")
        if shop_again == "no":
            return False
        if shop_again == "yes":
            return True
        print("\nTry typing that again please!\n")


def main() -> None:
    """
    Run the shopping program.

    Holds the shop's items and prices and loops through the menus until
    the user is done shopping.
    """

    shop_items: dict[str, dict[str, float]] = {
        "Snacks": {"Chips": 2.50, "Cookies": 3.20, "Pretzels": 2.48},
        "Food": {"Milk": 2.87, "Bread": 1.82, "Eggs": 3.89},
        "Drinks": {"Water": 1.00, "Juice": 1.50, "Soda": 2.15},
        "Lottery Ticket": {"$10 Ticket": 10.0, "$100 Ticket": 100.0},
    }

    cart_total: float = 0.0
    shopping_cart: list[str] = []
    user_budget: float = STARTING_BUDGET
    is_shopping: bool = True

    print("Welcome to Slow Way!\n")

    while is_shopping:
        print(f"Looks like you have a budget of ${user_budget:.2f}!")
        print("What are you looking for today?")

        chosen_category: dict[str, float] = stage_1(shop_items)

        chosen_item, item_price, user_budget = stage_2(chosen_category, user_budget)
        if chosen_item is None:
            continue

        shopping_cart.append(chosen_item)
        cart_total += item_price

        cart_total, user_budget = gambling(
            shopping_cart, cart_total, user_budget, shop_items["Lottery Ticket"]
        )
        is_shopping = pre_checkout(cart_total, user_budget, shopping_cart)

    print_receipt(shopping_cart, cart_total, user_budget)
    print("Thanks for shopping at Slow Way!")


if __name__ == "__main__":
    main()
