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
            "coffee": 24,
            "milk": 150,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100,
        },
        "cost": 3.0,
    },
}

profit = 0
resources = {
    "water": 300,
    "coffee": 100,
    "milk": 200,
}


def report(resources_left, profit_earn):
    water = resources_left["water"]
    coffee = resources_left["coffee"]
    milk = resources_left["milk"]
    money = profit_earn
    print(f"Water: {water}ml")
    print(f"Coffee: {coffee}g")
    print(f"Milk: {milk}ml")
    print(f"Money: ${money}")

def coffee(user_choice, resources_left):
    global MENU
    profit_earn = 0
    check = check_resource(user_choice, resources_left)
    if check == False:
        return 0, resources_left
    else:
        profit_earn = process_coin(user_choice)
        if profit_earn == 0:
            return 0, resources_left
        else:
            resources_left["water"] -= MENU[user_choice]["ingredients"]["water"]
            resources_left["coffee"] -= MENU[user_choice]["ingredients"]["coffee"]

            if user_choice != "espresso":
                resources_left["milk"] -= MENU[user_choice]["ingredients"]["milk"]

            print(f"Here is your {user_choice} \U00002615 Enjoy!")
            return profit_earn, resources_left

def check_resource(user_choice, resources_left):
    global MENU
    if user_choice == "latte" or user_choice == "cappuccino":
        water_require = MENU[user_choice]["ingredients"]["water"]
        coffee_require = MENU[user_choice]["ingredients"]["coffee"]
        milk_require = MENU[user_choice]["ingredients"]["milk"]
    else: 
        water_require = MENU[user_choice]["ingredients"]["water"]
        coffee_require = MENU[user_choice]["ingredients"]["coffee"]
        milk_require = 0

    water = resources_left["water"]
    coffee = resources_left["coffee"]
    milk = resources_left["milk"]

    if water > water_require and coffee > coffee_require and milk > milk_require:
        return True
    else:
        if water_require > water:
            print("Sorry there is not enough water.")
        elif coffee_require > coffee:
            print("Sorry there is not enough coffee.")
        else:
            print("Sorry there is not enough milk.")
        return False

def process_coin(user_choice):
    global MENU
    print("Please insert coins.")
    no_of_quarters = int(input("How many quarters? "))
    no_of_dimes = int(input("How many dimes? "))
    no_of_nickles = int(input("How many nickles? "))
    no_of_pennies = int(input("How many pennies? "))

    insert_amt = no_of_quarters * 0.25 + no_of_dimes * 0.1 + no_of_nickles * 0.05 + no_of_pennies * 0.01
    cost_require = MENU[user_choice]["cost"]

    if cost_require > insert_amt:
        print("Sorry that's not enough money. Money refunded.")
        return 0
    elif insert_amt == cost_require:
        return cost_require
    else:
        change = insert_amt - cost_require
        print(f"Here is ${round(change, 2)} dollars in change.")
        return cost_require


option = [report, coffee]

is_turn_off = False
while not is_turn_off:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "report":
        option[0](resources, profit)
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        profit_earn, resources_left = option[1](choice, resources)
        profit += round(profit_earn, 2)
        resources = resources_left
    elif choice == "off":
        is_turn_off = True
        print("The coffee machine is turn off.")
    else:
        print("Wrong option!")
