menu = {
    1: ("Burger", 5),
    2: ("Pizza", 8),
    3: ("Pasta", 7),
    4: ("Salad", 4),
    5: ("Fries", 3),
    6: ("Sandwich", 6),
    7: ("Steak", 15),
    8: ("Tacos", 9),
    9: ("Sushi", 12),
    10: ("Ice Cream", 4),
    11: ("Coffee", 2),
    12: ("Tea", 1),
    13: ("Cake", 5),
}

cart = {}


def display_menu(menu):
    print("......................Menu......................")
    for key, (item, price) in menu.items():
        print(f"{key}. {item}: ₹{price}")
    print()


def add_to_cart(menu, cart):
    while True:
        display_menu(menu)
        food_key = input("Enter the number of the food item to buy (q to quit, d to remove an item): ").lower()

        if food_key == 'q':
            break
        elif food_key == 'd':
            remove_item(cart)
        elif food_key.isdigit() and int(food_key) in menu:
            item_name, item_price = menu[int(food_key)]
            cart[item_name] = item_price
            print(f"{item_name} has been added to your cart.")
        else:
            print("Invalid input. Please choose a valid number from the menu.")
        print()


def remove_item(cart):
    if not cart:
        print("Your cart is empty. No items to remove.")
        return

    display_cart(cart)
    remove_key = input("Enter the number of the item you want to remove: ")

    if remove_key.isdigit() and 1 <= int(remove_key) <= len(cart):
        item_to_remove = list(cart.keys())[int(remove_key) - 1]
        del cart[item_to_remove]
        print(f"{item_to_remove} has been removed from your cart.")
    else:
        print("Invalid input. Please choose a valid number from your cart.")
    print()


def display_cart(cart):
    if not cart:
        print("Your cart is empty.")
        return
    print("......................Your Cart......................")
    for i, (food, price) in enumerate(cart.items(), start=1):
        print(f"{i}. {food}: ₹{price}")
    print()


def calculate_total(cart):
    return sum(cart.values())


add_to_cart(menu, cart)
display_cart(cart)

total_price = calculate_total(cart)

if total_price > 0:
    print(f"Your total is ₹{total_price}")
else:
    print("You have not purchased any items.")
