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
            print(f"Sorry, there is not enough {ingredient} for that drink.")
            return False
    return True

def calculate_coins():
    drink_total = drink["cost"]
    input("Please insert coins.")
    quarters = int(input("How many quarters do you have?"))
    dimes = int(input("How many dimes do you have?") )
    nickels = int(input("How many nickels do you have?"))
    pennies = int(input("How many pennies do you have?"))
    total = float((quarters * .25) + (dimes * .1) + (nickels * .05) + (pennies * .01))
    if total > drink_total:
        change = total - drink_total
        profit_so_far =- change
        print(f"Your change is {change}.")



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
            calculate_coins()

