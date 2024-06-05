from Data import MENU

WATER = 500
MILK = 400
COFFEE = 300
TURN_ON = True


def has_money():
    global wish
    hundred = int(input("How many Hundreds? "))
    fifty = int(input("How many Fifties? "))
    ten = int(input("How many Tens? "))

    money = (hundred * 100) + (fifty * 50) + (ten * 10)

    if money > MENU[wish]["cost"]:
        print(f"Here's you change of {money - MENU[wish]['cost']}")
        return True

    elif money == MENU[wish]["cost"]:
        return True

    print("Sorry You don't have sufficient Money")
    return False


def has_sufficient_resources():
    global WATER, MILK, COFFEE

    if (wish == "espresso" or wish == "latte" or wish == "cappuccino") and MENU[wish]["ingredients"]["water"] <= WATER and MENU[wish]["ingredients"]["milk"] <= MILK and MENU[wish]["ingredients"]["coffee"] <= COFFEE:
        return True

    elif wish != "espresso" and wish != "latte" and wish != "cappuccino":
        print("Sorry, this is not Available")

    elif MENU[wish]["ingredients"]["water"] > WATER:
        print("Sorry, there is not sufficient Water")

    elif MENU[wish]["ingredients"]["milk"] > MILK:
        print("Sorry, there is not sufficient Milk")

    elif MENU[wish]["ingredients"]["coffee"] <= COFFEE:
        print("Sorry, there is not sufficient Coffee")

    return False


while TURN_ON:
    wish = input("What would you like? (Espresso/ Latte/ Cappuccino): ").lower()

    if wish != "close" and has_sufficient_resources() and has_money():
        WATER -= MENU[wish]["ingredients"]["water"]
        MILK -= MENU[wish]["ingredients"]["milk"]
        COFFEE -= MENU[wish]["ingredients"]["coffee"]

        print("Here's your Drink. Have a nice day")

    else:
        TURN_ON = False

