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
    """Checks to see if enough resources to make drink. Returns True or False."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item} for that drink.")
            return False
    return True


def calculate_coins():
    """Calculates coins inserted and dispenses change to user"""
    print("Please insert coins.")
    quarters = int(input("How many quarters do you have?")) * .25
    dimes = int(input("How many dimes do you have?")) * .1
    nickels = int(input("How many nickels do you have?")) * .05
    pennies = int(input("How many pennies do you have?")) * .01
    total = float(quarters + dimes + nickels + pennies)
    return total


def successful_transaction(money_given, drink_total):
    """Checks to see if payment is accepted, returns False if insufficient funds"""
    if money_given >= drink_total:
        global profit_so_far
        profit_so_far += drink_total
        change = round(money_given - drink_total, 2)
        print(f"Your change is ${change}.")
        return True
    else:
        print("Sorry, not enough money.")
        return False


def make_coffee(user_choice, order_ingredients):
    """Deduct ingredients from user selection from overall resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {user_choice}! Enjoy! ☕")


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
        if check_resources(drink["ingredients"]):
            user_total = calculate_coins()
            if successful_transaction(user_total, drink["cost"]):
                make_coffee(choice, drink["ingredients"])