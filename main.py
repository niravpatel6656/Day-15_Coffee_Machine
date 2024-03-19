# Importing necessary resources from data
from data import MENU, resources

# Initializing money resource
resources["money"] = 0


# Function to add coins into the data
def add_coin_into_data(added_money):
    resources["money"] += added_money


# Function to update resources data after processing coffee
def update_data(water, milk, coffee):
    resources["water"] -= water
    resources["milk"] -= milk
    resources["coffee"] -= coffee


# Main function for the coffee machine
def coffee_machine():
    # Prompting user for their choice
    user_choice = input('''
\nEnter your choice from following options : 
1. Latte
2. Cappuccino
3. Espresso
4. Report
5. Off\n
''')

    # Function to check if resources are sufficient for making a coffee
    def check_resources(require_water, require_milk, require_coffee):
        if resources["water"] >= require_water and resources["milk"] >= require_milk and resources["coffee"] >= require_coffee:
            return True
        else:
            return False

    # Function to process the coins inserted by the user
    def process_coin():
        total_inserted_coins = (float(input("\nHow many quarters ? ")) * 0.25) + (
                    float(input("How many dimes ? ")) * 0.10) + (float(input("How many nickels ? ")) * 0.05) + (
                                           float(input("How many pennies ? ")) * 0.01)
        return total_inserted_coins

    # Function to return the remaining coins after coffee purchase
    def coin_return(sum_of_inserted_coin, coffee_money):
        coin_in_change = round((sum_of_inserted_coin - coffee_money), 2)
        print(f"\nHere is your coin in change ${coin_in_change}, Please collect it")

    # Function to handle coin insertion and coffee dispensing
    def coins_and_coffee(coffee_name, require_water_for_coffee, require_milk_for_coffee, require_coffee_for_coffee):
        print('\nPlease enter coins')
        inserted_coins = 0.0
        while inserted_coins < MENU[coffee_name]["cost"]:
            inserted_coins += round(process_coin(), 2)
        print(f"\nYou have inserted ${inserted_coins}")
        coffee_cost = MENU[coffee_name]["cost"]
        if inserted_coins >= coffee_cost:
            coin_return(inserted_coins, coffee_cost)
            add_coin_into_data(coffee_cost)
            update_data(require_water_for_coffee, require_milk_for_coffee, require_coffee_for_coffee)
            print(f'Enjoy your {coffee_name}...')
            coffee_machine()

    # Function to process the selected coffee choice
    def process_coffee(coffee_name):
        require_water_for_coffee = MENU[coffee_name]["ingredients"]["water"]
        require_milk_for_coffee = MENU[coffee_name]["ingredients"]["milk"]
        require_coffee_for_coffee = MENU[coffee_name]["ingredients"]["coffee"]

        if check_resources(require_water_for_coffee, require_milk_for_coffee, require_coffee_for_coffee):
            coins_and_coffee(coffee_name, require_water_for_coffee, require_milk_for_coffee, require_coffee_for_coffee)
        else:
            print('Sorry..\n We don\'t have enough resources to process your Coffee')

    # Handling user's choice
    if user_choice == "1":
        process_coffee("latte")
    elif user_choice == "2":
        process_coffee("cappuccino")
    elif user_choice == "3":
        process_coffee("espresso")
    elif user_choice == "4":
        print("\n".join("{}\t{}".format(k, v) for k, v in resources.items()))
        coffee_machine()
    elif user_choice == "5":
        print('\nGood Bye\nShutting Down.....')
    else:
        print('\nEnter valid choice\n')
        coffee_machine()


# Initiating the coffee machine
coffee_machine()
