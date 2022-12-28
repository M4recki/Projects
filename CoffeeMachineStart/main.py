from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Objects
MoneyMachine = MoneyMachine()
Menu = Menu()
CoffeeMaker = CoffeeMaker()

MachineOn = True
while MachineOn:
    Drink = input(f"What would you like to drink? {Menu.get_items()} ")
    if Drink == "off":
        MachineOn = False
    elif Drink == "report":
        MoneyMachine.report()
        CoffeeMaker.report()
    else:
        Drink2 = Menu.find_drink(Drink)
        if CoffeeMaker.is_resource_sufficient(Drink2) == True:
            if MoneyMachine.make_payment(Drink2.cost) == True:
                CoffeeMaker.make_coffee(Drink2)
                continue
            else:   
                MachineOn = False
        else:
            print(f"{Drink} is not sufficient")
            MachineOn = False