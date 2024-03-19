from data import MENU, resources




def check_resources(water,milk,coffee):
    print(water)
    print(milk)
    print(coffee)
def process_coin():
    pass
def coin_return():
    pass

def add_coin_into_data():
    pass

def update_data(water,milk,coffee):
    pass
def coffee_machine():
    user_choice = input('''Enter your choice from following options : 
    1. Latte
    2. Cappuccino
    3. Espresso
    4. Report
    5. Off\n\n
    ''')


    if user_choice == "1":

        check_resources(resources["water"],resources["milk"],resources["coffee"])
        if check_resources == True:
            print('Please enter coins')
            process_coin()
            if process_coin() >= 2.50:
                coin_return()
                add_coin_into_data()
                update_data(45,12,12)
                print('Enjoy your coffee...')
                coffee_machine()
            else:
                print('Insufficient fund\nPlease enter more funds')
        else:
            print('Sorry..\n We don\'t have enough resources to process your Coffee')


    elif user_choice == "2":
        # Code for handling choice 2 goes here
        pass

    elif user_choice == "3":
        # Code for handling choice 3 goes here
        pass

    elif user_choice == "4":
        print("\n".join("{}\t{}".format(k, v) for k, v in resources.items()))
        coffee_machine()

    elif user_choice == "5":
        print('\nGood Bye\nShutting Down.....')

    else:
        print('\nEnter valid choice\n')
        coffee_machine()


coffee_machine()