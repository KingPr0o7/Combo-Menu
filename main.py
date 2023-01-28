import os
from datetime import date
from prettytable import PrettyTable
from prettytable import SINGLE_BORDER
from prettytable import DOUBLE_BORDER

# Combo Menu Configuration
cart_items = []
cart_item_prices = []
cart_total_cost = 0

# Global Functions
def clear_console():
	os.system('cls')
	os.system('clear')

class str_format:
    # Single
	PASS = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	# Combinations
	BOLD_UNDERLINE = '\033[1m\033[4m'
	PASS_BOLD = '\033[92m\033[1m'
	PASS_UNDERLINE = '\033[92m\033[4m'
	PASS_BOLD_UNDERLINE = '\033[92m\033[1m\033[4m'
	WARNING_BOLD = '\033[93m\033[1m'
	WARNING_UNDERLINE = '\033[93m\033[4m'
	WARING_BOLD_UNDERLINE = '\033[93m\033[1m\033[4m'
	FAIL_BOLD = '\033[91m\033[1m'
	FAIL_UNDERLINE = '\033[91m\033[4m'
	FAIL_BOLD_UNDERLINE = '\033[91m\033[1m\033[4m'
	# End
	END = '\033[0m'

def format_str(style, text):
	style_map = {
    # Single
	'PASS': str_format.PASS,
	'WARNING': str_format.WARNING,
	'FAIL': str_format.FAIL,
	'BOLD': str_format.BOLD,
	'UNDERLINE': str_format.UNDERLINE,
	# Combinations 
	'BOLD_UNDERLINE': str_format.BOLD_UNDERLINE,
	'PASS_BOLD': str_format.PASS_BOLD,
	'PASS_UNDERLINE': str_format.PASS_UNDERLINE,
	'PASS_BOLD_UNDERLINE': str_format.PASS_BOLD_UNDERLINE,
	'WARNING_BOLD': str_format.WARNING_BOLD,
	'WARNING_UNDERLINE': str_format.WARNING_UNDERLINE,
	'WARING_BOLD_UNDERLINE': str_format.WARING_BOLD_UNDERLINE,
	'FAIL_BOLD': str_format.FAIL_BOLD,
	'FAIL_UNDERLINE': str_format.FAIL_UNDERLINE,
	'FAIL_BOLD_UNDERLINE': str_format.FAIL_BOLD_UNDERLINE,
    'END': str_format.END
    }
	return f'{style_map.get(style, "") + text + str_format.END}'

# Receipt Setup/Configuration
receipt = PrettyTable()
today = date.today()
receipt.set_style(DOUBLE_BORDER)
receipt.title = f'RECEIPT | {today.month}/{today.day}/{today.year}'
receipt.field_names = ['TYPE', 'NAME', 'SIZE', 'PRICE']

# Options Table (Setup/Configuration)
options = PrettyTable()
options.set_style(SINGLE_BORDER)
options.title = 'ITEM OPTIONS'
options.field_names = ['NAME', 'SIZE', 'PRICE']

# Error Setup/Configuration
error = PrettyTable()
error.set_style(SINGLE_BORDER)
error.title = format_str('FAIL_BOLD', 'TYPE ERROR')
error.field_names = [format_str('BOLD', 'TYPE'), format_str('BOLD', 'REQUIRED ARGUMENTS')]


def error_handle(type, item_type):
	error.clear_rows()
	if type == 'yes no':
		error.add_row(['STRING', format_str('PASS_BOLD_UNDERLINE', 'Y') + ' or ' + format_str('PASS_BOLD_UNDERLINE', 'YES')])
		error.add_row(['STRING', format_str('PASS_BOLD_UNDERLINE', 'N') + ' or ' + format_str('PASS_BOLD_UNDERLINE', 'NO')])
	elif type == 'food selection':
		if item_type == 'sandwitch':
			item_list = sandwitchs.names
		elif item_type == 'beverage':
			item_list = beverages.sizes
		elif item_type == 'fries':
			item_list = fries.sizes
		for index, item in enumerate(item_list):
			error.add_row(['STRING', format_str('BOLD_UNDERLINE', item[index][0]) + item[index][1:]])
	print(error)

def addToCart(item_type, item_name, items_list, items_sizes, items_prices):
	global cart_total_cost
	if item_type == 'Beverage':
		for index, item in enumerate(items_sizes):
			if str(item_name).lower() == str(items_sizes[index]).lower():
				cart_items.append(item)
				item_price = items_prices[index]
				cart_item_prices.append(items_prices[index])
				cart_total_cost += float(items_prices[index])
				clear_console()
				if len(receipt.rows) >= 2:
					receipt.del_row(-1)
					receipt.del_row(-1)
				receipt.add_row([
					str(item_type).upper(), str(items_list), str(items_sizes[index]), '$' + str(item_price)])
				receipt.add_row(['', '', '', ''])
				receipt.add_row(['TOTAL', '', '', '$' + "{:.2f}".format(cart_total_cost)])
				print(receipt)
	else:
		for index, item in enumerate(items_list):
			if str(item_name).lower() == str(items_list[index]).lower():
				cart_items.append(item)
				item_price = items_prices[index]
				cart_item_prices.append(items_prices[index])
				cart_total_cost += float(items_prices[index])
				clear_console()
				if len(receipt.rows) >= 2:
					receipt.del_row(-1)
					receipt.del_row(-1)
				receipt.add_row([str(item_type).upper(), str(item), str(items_sizes), '$' + str(item_price)])
				receipt.add_row(['', '', '', ''])
				receipt.add_row(['TOTAL', '', '', '$' + "{:.2f}".format(cart_total_cost)])
				print(receipt)


# Sandwitch Configuration
class sandwitchs:
	type = 'Sandwitch'
	names = ['Chicken', 'Beef', 'Tofu']
	sizes = 'Regular'
	prices = ['5.25', '6.25', '5.75']

def sandwitchTable():
	options.title = 'SANDWITCH OPTIONS'
	options.sortby = 'PRICE'
	options.reversesort = True
	#error_handle('food selection', 'sandwitch')
	for index in range(len(sandwitchs.names)):
		options.add_row([format_str('BOLD_UNDERLINE', sandwitchs.names[index][0]) + sandwitchs.names[index][1:], sandwitchs.sizes, '$' + sandwitchs.prices[index]])
	print(options)
	print(format_str('WARNING_BOLD_UNDERLINE', 'You can type the whole name or just the first letter!'))

# Beverage Configuration
class beverages:
	type = 'Beverage'
	names = 'Fountain'
	sizes = ['Small', 'Medium', 'Large']
	prices = ['1.00', '1.75', '2.25']

def beverageTable():
	options.title = 'BEVERAGE OPTIONS'
	for index in range(len(beverages.names)):
		options.add_row([beverages.names[index], beverages.sizes[index], '$' + beverages.prices[index]])
	print(options)

# Fries Configuration
class fries:
	type = 'Side'
	names = 'Fries'
	sizes = ['Small', 'Medium', 'Large']
	prices = ['1.00', '1.50', '2.00']


# Sandwitch Selection
def sandwitch_selection(stage):
	if stage == 'agreement':
		sandwitch_agreement = input(f'Would you like a sandwitch? ({format_str("BOLD_UNDERLINE", "Y")}es | {format_str("BOLD_UNDERLINE", "N")}o) ')
		if 'yes' in sandwitch_agreement.lower() or sandwitch_agreement.lower() == 'y':
			sandwitch_selection('choose')
		elif 'no' in sandwitch_agreement.lower() or sandwitch_agreement.lower() == 'n':
			beverage_selection()
		else:
			error_handle('yes no', 'sandwitch')
			sandwitch_selection('agreement')
	elif stage == 'choose':
		sandwitchTable()
		sandwitch_selected = input('What type of sandwitch would you like? ')
		if sandwitch_selected.lower() == 'c' or 'chicken' in sandwitch_selected.lower():
			sandwitch_selected = 'chicken'
		elif sandwitch_selected.lower() == 'b' or 'beef' in sandwitch_selected.lower():
			sandwitch_selected = 'beef'
		elif sandwitch_selected.lower() == 't' or 'tofu' in sandwitch_selected.lower():
			sandwitch_selected = 'tofu'
		else:
			print('ERROR')
			print(error)
			sandwitch_selection('choose')
		addToCart(sandwitchs.type, sandwitch_selected, sandwitchs.names, sandwitchs.sizes, sandwitchs.prices)
		beverage_selection()


# Drink Selection
def beverage_selection():
	print(f'Options: \n- {format_str("BOLD_UNDERLINE", "Y")}es\n- {format_str("BOLD_UNDERLINE", "N")}o')
	beverage_agreement = input('Whould you like a beverage? ')
	if 'yes' in beverage_agreement.lower() or beverage_agreement.lower() == 'y':
		beverage_size = input('What size of beverage? ')
		addToCart(beverages.type, beverage_size, beverages.names, beverages.sizes, beverages.prices)
	elif 'no' in beverage_agreement.lower() or beverage_agreement.lower() == 'n':
		print('hello')
	else:
		print('ERROR')

sandwitch_selection('agreement')

# Fries Selection
#fries_agreement = input('Would you like fries? ')
#if (fries_agreement.lower() in ['yes','y']):
#	fries_size = input('What size of fries? ')
#	if fries_size.lower() == 'small':
#		fries_upgrade = input('Would you like to mega-size your fries? ')
#		if fries_upgrade.lower() in ['yes','y']:
#add cart
#		if fries_upgrade.lower() in ['no','n']:
#add cart
#	else:
#add cart

# Ketchup Selection
#ketchup_ask = input('How many ketchup packets do you want? ')
#if int(ketchup_ask) > 0:
#	ketchup_amount = ketchup_ask
#	print('You got: ' + ketchup_amount + ' packets!')
