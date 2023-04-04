from data import *

end_proccess = False
profit = 0
def info_report(resources, profit):
    resources['money'] = profit
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


def check_ingredients(menu, resourses, user_ask):
    if menu[user_ask]:
        ingredients = menu[user_ask]['ingredients']
        for item in ingredients:
            if ingredients[item] < resourses[item]:
                return True
            else:
                return False
    else:
        print("Menu that you chose does not exists")

def check_coins():
    print("Insert coins: ")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.1
    total += int(input("How many nickles? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01

    return round(total)


while not end_proccess:
    user_ask = input("What would you like? (espresso/latte/cappuccino): ")
    if user_ask == "report":
        info_report(resources, profit)
    elif user_ask == "off":
        end_proccess = True
    else:
        if check_ingredients(MENU, resources, user_ask) == True:
            total = check_coins()
            if total >= MENU[user_ask]['cost']:
                refund = total - MENU[user_ask]['cost']
                profit = total - refund
                print(f"Here is {total} in change.")
                print(f"Here is your refund {refund}$")
                print(f"Here is your {user_ask} ☕️. Enjoy!")
                for item in MENU[user_ask]['ingredients']:
                    resources[item] -= MENU[user_ask]['ingredients'][item]
        else:
            for ingredient in MENU[user_ask]['ingredients']:
                if resources[ingredient] < MENU[user_ask]['ingredients'][ingredient]:
                    print(f"Sorry there is not enough {ingredient}")
