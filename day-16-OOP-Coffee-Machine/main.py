from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def main():
	cm = CoffeeMaker()
	mm = MoneyMachine()
	menu = Menu()
	order = ""
	while order != 'off':
		order = input(f'What would you like? {menu.get_items()}: ')
		if order == 'off':
			break
		if order == 'report':
			cm.report()
			mm.report()
			continue
		menu_item = menu.find_drink(order)
		if not menu_item:
			continue
		if not cm.is_resource_sufficient(menu_item):
			continue
		if not mm.make_payment(menu_item.cost):
			continue
		cm.make_coffee(menu_item)

if __name__ == '__main__':
	main()
	