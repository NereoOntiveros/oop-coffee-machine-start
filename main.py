from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
machine_is_on = True
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

while machine_is_on:
    menu_options = menu.get_items()
    user_choice = input(f"What would you like? ({menu_options}):").lower()
    drink = menu.find_drink(user_choice)
    if user_choice == 'off':
        machine_is_on = False
    elif user_choice == 'report':
        resources_report = coffee_maker.report()
        money_report = money_machine.report()
        print(resources_report)
        print(money_report)
    else:
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
