# Coffee Machine Program

## Overview
This Python program simulates a simple coffee machine that allows users to order espresso, latte, or cappuccino, check resource levels, and turn off the machine. It manages resources (water, coffee, milk) and tracks profit based on user payments.

## Features
- **Menu**: Offers three drink options (espresso, latte, cappuccino) with predefined ingredients and costs.
- **Resource Management**: Tracks water, coffee, and milk, ensuring sufficient resources before making a drink.
- **Payment Processing**: Accepts coins (quarters, dimes, nickels, pennies) and calculates change if overpaid.
- **Report Generation**: Displays current resource levels and total profit.
- **Turn Off**: Allows the user to shut down the machine.

## How to Run
1. Run the program using the command:
   ```bash
   python main.py
   ```
2. Follow the prompt to select a drink (`espresso`, `latte`, `cappuccino`), view the report (`report`), or turn off the machine (`off`).

## Usage
- **Ordering a Drink**: Enter `espresso`, `latte`, or `cappuccino`. The program checks if there are enough resources, prompts for coin input, and processes the payment. If successful, it dispenses the drink and updates resources and profit.
- **Viewing Report**: Enter `report` to see current levels of water, coffee, milk, and total profit.
- **Turning Off**: Enter `off` to exit the program.
- **Invalid Input**: Any other input will display "Wrong option!" and prompt again.

## Code Structure
- **MENU**: Dictionary defining drinks, their ingredients, and costs.
- **resources**: Dictionary tracking available water, coffee, and milk.
- **profit**: Global variable tracking total earnings.
- **Functions**:
  - `report()`: Prints resource levels and profit.
  - `coffee()`: Handles drink preparation, resource deduction, and payment.
  - `check_resource()`: Verifies if sufficient resources are available.
  - `process_coin()`: Processes user payment and calculates change.
- **Main Loop**: Continuously prompts for user input until the machine is turned off.

## Example Interaction
```plaintext
What would you like? (espresso/latte/cappuccino): report
Water: 300ml
Coffee: 100g
Milk: 200ml
Money: $0
What would you like? (espresso/latte/cappuccino): latte
Please insert coins.
How many quarters? 12
How many dimes? 12
How many nickles? 10
How many pennies? 10
Here is $2.3 dollars in change.
Here is your latte ☕ Enjoy!
What would you like? (espresso/latte/cappuccino): espresso
Please insert coins.
How many quarters? 1 
How many dimes? 0
How many nickles? 0
How many pennies? 0
Sorry that's not enough money. Money refunded.
What would you like? (espresso/latte/cappuccino): espresso
Please insert coins.
How many quarters? 10
How many dimes? 4
How many nickles? 3
How many pennies? 2
Here is $1.57 dollars in change.
Here is your espresso ☕ Enjoy!
What would you like? (espresso/latte/cappuccino): report
Water: 50ml
Coffee: 58g
Milk: 50ml
Money: $4.0
What would you like? (espresso/latte/cappuccino): off
The coffee machine is turn off.
```

## License
This project is unlicensed; feel free to use and modify it as needed.
