# Coffee Machine Application

## **[100 Days of Code: The Complete Python Pro Bootcamp for 2025](https://www.udemy.com/course/100-days-of-code/)**

By Dr. Angela Yu

*Day 15 of 100:* Coffee Machine with Procedural Programming

## Project Overview

This project involves creating a virtual coffee machine using Python. The application allows users to select from three types of coffee drinks: espresso, latte, and cappuccino. It handles payments, returns change if necessary, and updates the available resources (water, milk, coffee) after each transaction.

### Main Features

- **Menu Selection**: Users can choose from espresso, latte, or cappuccino.
- **Resource Management**: The application checks and updates the available resources for each drink.
- **Payment Processing**: Users can insert coins to pay for their drink, and the application calculates and returns change if necessary.
- **Manager Functions**: Managers can generate a report of current resources and total money earned or turn off the machine.

## Usage & Requirements

This project is structured using functions to handle different aspects of the coffee machine's operation:
- **Resource Checking**: Functions to check if there are enough resources to make a drink.
- **Payment Processing**: Functions to handle coin insertion and change calculation.
- **Coffee Preparation**: Functions to update resources and prepare the drink.

## Workflow

1. **Menu Selection**: The user is prompted to select a drink from the menu.
2. **Resource Check**: The application checks if there are enough resources to make the selected drink.
3. **Payment**: The user is prompted to insert coins to pay for the drink.
4. **Transaction Completion**: If the payment is sufficient and resources are available, the drink is prepared, and resources are updated.
5. **Manager Functions**: Managers can enter `report` to view current resources and money earned or `off` to turn off the machine.

### Manager Functions

- **Report**: Displays the current resources and total money earned.
  ```
  Water: 100ml
  Milk: 50ml
  Coffee: 76g
  Money: $2.5
  ```
- **Off**: Turns off the coffee machine.

# Author & Credits

Programmed by **Artur Dragunov** under the instructional guidance of **[Dr. Angela Yu](https://www.udemy.com/user/4b4368a3-b5c8-4529-aa65-2056ec31f37e/)** via **[Udemy.com](udemy.com)**.