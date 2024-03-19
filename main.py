from data import MENU, resources

resources["money"] = 0


def add_coin_into_data(added_money):
    resources["money"] += added_money


def update_data(water, milk, coffee):
    resources["water"] -= water
    resources["milk"] -= milk
    resources["coffee"] -= coffee


def coffee_machine():
    user_choice = input('''
\nEnter your choice from following options : 
1. Latte
2. Cappuccino
3. Espresso
4. Report
5. Off\n
''')

    def check_resources(require_water, require_milk, require_coffee):
        if resources["water"] >= require_water and resources["milk"] >= require_milk and resources[
            "coffee"] >= require_coffee:
            return True
        else:
            return False

    def process_coin():
        total_inserted_coins = (float(input("\nHow many quarters ? ")) * 0.25) + (
                    float(input("How many dimes ? ")) * 0.10) + (float(input("How many nickels ? ")) * 0.05) + (
                                           float(input("How many pennies ? ")) * 0.01)
        return total_inserted_coins

    def coin_return(sum_of_inserted_coin, coffee_money):
        coin_in_change = round((sum_of_inserted_coin - coffee_money), 2)
        print(f"\nHere is your coin in change ${coin_in_change}, Please collect it")

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
            # print("\n".join("{}\t{}".format(k, v) for k, v in resources.items()))
            print(f'Enjoy your {coffee_name}...')
            coffee_machine()

        # else:
        #     print('Insufficient fund\nPlease enter more funds')
        #     inserted_coins += round(process_coin(),2)

    def process_coffee(coffee_name):
        require_water_for_coffee = MENU[coffee_name]["ingredients"]["water"]
        require_milk_for_coffee = MENU[coffee_name]["ingredients"]["milk"]
        require_coffee_for_coffee = MENU[coffee_name]["ingredients"]["coffee"]

        # print(require_water_for_coffee)
        # print(require_milk_for_coffee)
        # print(require_coffee_for_coffee)

        if check_resources(require_water_for_coffee, require_milk_for_coffee, require_coffee_for_coffee):
            # print('Please enter coins')
            # inserted_coins = round(process_coin(),2)
            coins_and_coffee(coffee_name, require_water_for_coffee, require_milk_for_coffee, require_coffee_for_coffee)
        else:
            print('Sorry..\n We don\'t have enough resources to process your Coffee')

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


coffee_machine()
