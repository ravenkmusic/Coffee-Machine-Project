MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit_so_far = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

print("Welcome to the Coffee Shop!")

def check_resources(order_ingredients):
    for ingredient in order_ingredients:
        if order_ingredients["item"] >= resources["item"]:
            print(f"Sorry, there is not enough {item} for that drink.")
            return False
    return True

def calculate_coins():
    input("Please insert coins.")

coffee_machine = True

while coffee_machine:
    choice = input("What would you like? An espresso, a latte or a cappuccino? ")
    if choice == "off":
        coffee_machine = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit_so_far}")
    else:
        drink = MENU[choice]
        if check_resources(drink['ingredients']):
