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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    'money': 0
}

def check_resources(order):
    """Check if there are enough resources to make the drink."""
    for ingredient, required_amount in MENU[order]['ingredients'].items():
        if resources[ingredient] < required_amount:
            print(f'Sorry there is not enough {ingredient}!')
            return False
    return True

def process_coins():
    """Process the inserted coins and return the total amount."""
    print("Please insert coins.")
    try:
        quarters = int(input('How many quarters?: '))
        dimes = int(input('How many dimes?: '))
        nickles = int(input('How many nickles?: '))
        pennies = int(input('How many pennies?: '))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return 0

    total_inserted = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    return total_inserted

def make_coffee(order):
    """Deduct the resources and prepare the coffee."""
    for ingredient, amount in MENU[order]['ingredients'].items():
        resources[ingredient] -= amount
    print(f'Here is your {order}. Enjoy!')

def main():
    order = ""
    while order != 'off':
        order = input('What would you like? (espresso/latte/cappuccino): ')
        if order not in ['espresso', 'latte', 'report', 'cappuccino', 'off']:
            print("Sorry, unexpected input")
        elif order == 'off':
            print('Switching off')
        elif order == 'report':
            print(f'Water: {resources["water"]}ml')
            print(f'Milk: {resources["milk"]}ml')
            print(f'Coffee: {resources["coffee"]}g')
            print(f'Money: ${resources["money"]}')
        else:
            if not check_resources(order):
                continue

            price = MENU[order]['cost']
            print(f'{order} costs ${price}.')
            total_inserted = process_coins()

            if total_inserted >= price:
                print(f'Thank you!')
                resources['money'] += price
                if total_inserted > price:
                    print(f'Here is ${round(total_inserted - price, 2)} in change.')
                make_coffee(order)
            else:
                print("Sorry, that's not enough money. Money refunded.")

if __name__ == "__main__":
    main()
