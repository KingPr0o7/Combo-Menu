# ░█████╗░░█████╗░███╗░░░███╗██████╗░░█████╗░  ███╗░░░███╗███████╗███╗░░██╗██╗░░░██╗
# ██╔══██╗██╔══██╗████╗░████║██╔══██╗██╔══██╗  ████╗░████║██╔════╝████╗░██║██║░░░██║
# ██║░░╚═╝██║░░██║██╔████╔██║██████╦╝██║░░██║  ██╔████╔██║█████╗░░██╔██╗██║██║░░░██║
# ██║░░██╗██║░░██║██║╚██╔╝██║██╔══██╗██║░░██║  ██║╚██╔╝██║██╔══╝░░██║╚████║██║░░░██║
# ╚█████╔╝╚█████╔╝██║░╚═╝░██║██████╦╝╚█████╔╝  ██║░╚═╝░██║███████╗██║░╚███║╚██████╔╝
# ░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚═════╝░░╚════╝░  ╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░╚═════╝░
# ️          ⚠ CANNOT BE RUN ON TRINKET OR OTHERS WITHOUT LIBRARY SUPPORT
# Made By Nathan Parker (KingPr0o7)

import os
import time
import re
from datetime import date
from prettytable import PrettyTable
from prettytable import SINGLE_BORDER
from prettytable import DOUBLE_BORDER

#
# Settings / Configuration
#

# Used for clearing the console. (Replit uses Linux) 
system = 'Windows'

# Combo Menu Setup
cart_items = []
cart_item_types = []
cart_item_prices = []
cart_total_cost = 0

# REGEX PATTERN
pattern = "^[0-9]+$"

# Menu Items
class sandwichs:
	type = 'Sandwich'
	names = ['Chicken', 'Beef', 'Tofu']
	sizes = 'Regular'
	prices = ['5.25', '6.25', '5.75']

class beverages:
	type = 'Beverage'
	names = 'Fountain'
	sizes = ['Small', 'Medium', 'Large']
	prices = ['1.00', '1.75', '2.25']

class fries:
	type = 'Side'
	names = 'Fries'
	sizes = ['Small', 'Medium', 'Large']
	prices = ['1.00', '1.50', '2.00']

class ketchup:
    type = 'Extra'
    names = 'Ketchup'
    sizes = 'Regular'
    prices = 0.25

# Global Functions
def clear_console(system):
	if str(system).lower() == 'windows' or str(system).lower() == 'win':
		os.system('cls')
	elif str(system).lower() == 'linux':
		os.system('clear')

# String Formatter (Colors & Display Style)
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
	WARNING_BOLD_UNDERLINE = '\033[93m\033[1m\033[4m'
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
	'WARNING_BOLD_UNDERLINE': str_format.WARNING_BOLD_UNDERLINE,
	'FAIL_BOLD': str_format.FAIL_BOLD,
	'FAIL_UNDERLINE': str_format.FAIL_UNDERLINE,
	'FAIL_BOLD_UNDERLINE': str_format.FAIL_BOLD_UNDERLINE,
    'END': str_format.END
    }
	return f'{style_map.get(style, "") + text + str_format.END}'

#
# Information Display Table(s) (IDF(s)) [Prettytables]
#

receipt = PrettyTable()
today = date.today()
receipt.set_style(DOUBLE_BORDER)
receipt.title = format_str("BOLD", f"RECEIPT | {today.month}/{today.day}/{today.year}")
receipt.field_names = [format_str("BOLD", "QUANTITY"), format_str("BOLD", "TYPE"), format_str("BOLD", "NAME"), format_str("BOLD", "SIZE"), format_str("BOLD", "PRICE")]

# Options Table (Setup/Configuration)
options = PrettyTable()
options.set_style(SINGLE_BORDER)
options.title = 'ITEM OPTIONS'
options.field_names = [format_str("BOLD", "QUANTITY"), format_str("BOLD", "NAME"), format_str("BOLD", "SIZE"), format_str("BOLD", "PRICE")]
options.sortby = format_str("BOLD", "PRICE")
options.reversesort = True

# Error Setup/Configuration
error = PrettyTable()
error.set_style(SINGLE_BORDER)
error.title = format_str('FAIL_BOLD', 'TYPE ERROR')
error.field_names = [format_str('BOLD', 'TYPE'), format_str('BOLD', 'REQUIRED ARGUMENTS')]

#
# Error Handling (via a IDF)
#

def error_handle(type, item_type, user_input):
	clear_console(system)
	error.clear_rows()
	if type == 'yes no':
		error.add_row(['STRING', format_str('PASS_BOLD_UNDERLINE', 'Y') + ' or ' + format_str('PASS_BOLD_UNDERLINE', 'YES')])
		error.add_row(['STRING', format_str('PASS_BOLD_UNDERLINE', 'N') + ' or ' + format_str('PASS_BOLD_UNDERLINE', 'NO')])
	elif type == 'food selection':
		if item_type == 'sandwich':
			item_list = sandwichs.names
		elif item_type == 'beverage':
			item_list = beverages.sizes
		elif item_type == 'fries':
			item_list = fries.sizes
		for index in range(len(item_list)):
			error.add_row(['STRING', f'{format_str("PASS_BOLD_UNDERLINE", item_list[index][0])} or {format_str("PASS_BOLD_UNDERLINE", item_list[index])}'])
	elif type == 'food amount':
		error.add_row(['INTEGER', format_str('PASS_BOLD_UNDERLINE', '>=1 && !== 0')])
	print(error)
	print('You entered:', format_str("FAIL", user_input))
	time.sleep(5)
	clear_console(system)

#
# Shopping Cart (via a IDF)
#

def addToCart(item_quantity, item_type, item_name, items_list, items_sizes, items_prices):
	global cart_total_cost
	if item_type == 'Beverage' or item_type == 'Side':
		for index, item in enumerate(items_sizes):
			if str(item_name).lower().strip() == str(items_sizes[index]).lower().strip():
				cart_items.append(item)
				cart_item_types.append(item_type)
				item_price = float(items_prices[index]) * int(item_quantity)
				cart_item_prices.append(item_price)
				cart_total_cost += float(item_price)
				clear_console(system)
				if len(receipt.rows) >= 2:
					receipt.del_row(-1)
					receipt.del_row(-1)
				receipt.add_row([item_quantity, str(item_type).upper(), str(items_list), str(items_sizes[index]), '$' + "{:.2f}".format(float(item_price)) + f' (${items_prices[index]}ea)'])
				receipt.add_row(['', '', '', '', ''])
				receipt.add_row([format_str('BOLD', 'TOTAL'), '', '', '', format_str('BOLD', f'${"{:.2f}".format(cart_total_cost)}')])
		print(receipt)
	elif item_type == 'Sandwich':
		for index, item in enumerate(items_list):
			if str(item_name).lower().strip() == str(items_list[index]).lower().strip():
				cart_items.append(item)
				cart_item_types.append(item_type)
				item_price = float(items_prices[index]) * int(item_quantity)
				cart_item_prices.append(item_price)
				cart_total_cost += float(item_price)
				clear_console(system)
				if len(receipt.rows) >= 2:
					receipt.del_row(-1)
					receipt.del_row(-1)
				receipt.add_row([item_quantity, str(item_type).upper(), str(item), str(items_sizes), '$' + "{:.2f}".format(float(item_price)) + f' (${items_prices[index]}ea)'])
				receipt.add_row(['', '', '', '', ''])
				receipt.add_row([format_str('BOLD', 'TOTAL'), '', '', '', format_str('BOLD', f'${"{:.2f}".format(cart_total_cost)}')])
		print(receipt)
	# Extras
	else:
		discount = None
		cart_items.append(item_name)
		cart_item_types.append(item_type)
		item_price = float(items_prices) * int(item_quantity)
		cart_item_prices.append(item_price)
		cart_total_cost += float(item_price)
		clear_console(system)
		if len(receipt.rows) >= 2:
			receipt.del_row(-1)
			receipt.del_row(-1)     
		receipt.add_row([item_quantity, str(item_type).upper(), item_name, items_sizes, f'${"{:.2f}".format(float(item_price))} (${items_prices}ea)'])
		if 'Sandwich' in cart_item_types:
			if 'Beverage' in cart_item_types:
				if 'Side' in cart_item_types:
					cart_total_cost -= 1.00
					discount = True
					receipt.add_row(['', '', '', '', ''])
					receipt.add_row([format_str('UNDERLINE', 'DISCOUNT'), '', '', '', format_str('UNDERLINE', '$1.00')])		
		if discount is None:
			receipt.add_row(['', '', '', '', ''])
		receipt.add_row([format_str('BOLD', 'TOTAL'), '', '', '', format_str('BOLD', f'${"{:.2f}".format(cart_total_cost)}')])
		print(receipt)

def request_receipt():
	clear_console(system)
	print(receipt)

#
# Menu Item IDFs
#

def sandwichTable(type):
	options.clear_rows()
	if type == 'option':
		options.title = format_str('BOLD', 'SANDWICH OPTIONS')
		for index in range(len(sandwichs.names)):
			options.add_row([1, format_str('BOLD_UNDERLINE', sandwichs.names[index][0]) + sandwichs.names[index][1:], sandwichs.sizes, '$' + sandwichs.prices[index]])
		print(options)
		print(format_str('WARNING_BOLD_UNDERLINE', 'You can type the whole name or just the first letter!'))
	elif type == 'amount':
		options.title = format_str('BOLD', 'SANDWICH SIZES')
		for index in range(len(sandwichs.names)):
			options.add_row([format_str('BOLD_UNDERLINE', '>=1 && !== 0'), sandwichs.names[index], sandwichs.sizes, '$' + str(sandwichs.prices[index]) + 'ea'])	
		print(options)

def beverageTable(type):
	options.clear_rows()
	if type == 'option':
		options.title = format_str('BOLD', 'BEVERAGE OPTIONS')
		for index in range(len(beverages.sizes)):
			options.add_row([1, beverages.names, format_str('BOLD_UNDERLINE', beverages.sizes[index][0]) + beverages.sizes[index][1:], '$' + beverages.prices[index]])
		print(options)
	elif type == 'amount':
		options.title = format_str('BOLD', 'BEVERAGE AMOUNTS')
		for index in range(len(beverages.sizes)):
			options.add_row([format_str('BOLD_UNDERLINE', '>=1 && !== 0'), beverages.names, beverages.sizes[index], '$' + str(beverages.prices[index]) + 'ea'])	
		print(options)		

def friesTable(type):
	options.clear_rows()
	if type == 'option':
		options.title = format_str('BOLD', 'FRIES OPTIONS')
		for index in range(len(fries.sizes)):
			options.add_row([1, fries.names, format_str('BOLD_UNDERLINE', fries.sizes[index][0]) + fries.sizes[index][1:], '$' + fries.prices[index]])
		print(options)
	elif type == 'amount':
		options.title = format_str('BOLD', 'FRIES AMOUNTS')
		for index in range(len(fries.sizes)):
			options.add_row([format_str('BOLD_UNDERLINE', '>=1 && !== 0'), fries.names, fries.sizes[index], '$' + str(fries.prices[index]) + 'ea'])	
		print(options)	

def ketchupTable():
	options.clear_rows()
	options.title = format_str('BOLD', 'KETCHUP AMOUNTS')
	options.add_row([format_str('BOLD_UNDERLINE', '>=1 && !== 0'), ketchup.names, ketchup.sizes, '$' + str(ketchup.prices) + 'ea'])
	print(options)

#
# Menu Item Ordering
#

def sandwich_selection(stage):
	global sandwich_selected
	if stage == 'agreement':
		sandwich_agreement = input(f'Would you like a sandwich? ({format_str("BOLD_UNDERLINE", "Y")}es | {format_str("BOLD_UNDERLINE", "N")}o) ')
		if 'yes' in sandwich_agreement.lower().strip() or sandwich_agreement.lower().strip() == 'y':
			sandwich_selection('choose')
		elif 'no' in sandwich_agreement.lower().strip() or sandwich_agreement.lower().strip() == 'n':
			beverage_selection()
		else:
			error_handle('yes no', 'sandwich', sandwich_agreement)
			sandwich_selection('agreement')
	elif stage == 'choose':
		sandwichTable('option')
		sandwich_selected = input('What type of sandwich would you like? ')
		if sandwich_selected.lower().strip() == 'c' or 'chicken' in sandwich_selected.lower().strip():
			sandwich_selected = 'chicken'
		elif sandwich_selected.lower().strip() == 'b' or 'beef' in sandwich_selected.lower().strip():
			sandwich_selected = 'beef'
		elif sandwich_selected.lower().strip() == 't' or 'tofu' in sandwich_selected.lower().strip():
			sandwich_selected = 'tofu'
		else:
			error_handle('food selection', 'sandwich', sandwich_selected)
			sandwich_selection('choose')
		sandwich_selection('amount')
	elif stage == 'amount':
		sandwichTable('amount')
		sandwich_amount = input('How many sandwichs? ')
		isInt = bool(re.match(pattern, sandwich_amount))
		if isInt == True:
			if int(sandwich_amount) >= 1:
				addToCart(sandwich_amount, sandwichs.type, sandwich_selected, sandwichs.names, sandwichs.sizes, sandwichs.prices)
				beverage_selection('agreement')
			else:
				error_handle('food amount', 'sandwich', sandwich_amount)
				sandwich_selection('amount')				
		else:
			error_handle('food amount', 'sandwich', sandwich_amount)
			sandwich_selection('amount')

def beverage_selection(stage):
	global beverage_size_selected
	if stage == 'agreement':
		beverage_agreement = input(f'Would you like a beverage? ({format_str("BOLD_UNDERLINE", "Y")}es | {format_str("BOLD_UNDERLINE", "N")}o) ')
		if 'yes' in beverage_agreement.lower().strip() or beverage_agreement.lower().strip() == 'y':
			beverage_selection('choose')
		elif 'no' in beverage_agreement.lower().strip() or beverage_agreement.lower().strip() == 'n':
			fries_selection('agreement')
		else:
			error_handle('yes no', 'beverage', beverage_agreement)
			beverage_selection('agreement')
	elif stage == 'choose':
		beverageTable('option')
		beverage_size = input('What size of beverage? ')
		if beverage_size.lower().strip() == 's' or 'small' in beverage_size.lower().strip():
			beverage_size_selected = 'small'
		elif beverage_size.lower().strip() == 'm' or 'medium' in beverage_size.lower().strip():
			beverage_size_selected = 'medium'
		elif beverage_size.lower().strip() == 'l' or 'large' in beverage_size.lower().strip():
			beverage_size_selected = 'large'
		else:
			error_handle('food selection', 'beverage', beverage_size)
			beverage_selection('choose')
		beverage_selection('amount')
	elif stage == 'amount':
		beverageTable('amount')
		beverage_amount = input('How many beverages? ')
		isInt = bool(re.match(pattern, beverage_amount))
		if isInt == True:
			if int(beverage_amount) >= 1:
				addToCart(beverage_amount, beverages.type, beverage_size_selected, beverages.names, beverages.sizes, beverages.prices)
				fries_selection('agreement')
			else:
				error_handle('food amount', 'beverage', beverage_amount)
				beverage_selection('amount')				
		else:
			error_handle('food amount', 'beverage', beverage_amount)
			beverage_selection('amount')

def fries_selection(stage):
	global fries_size_selected
	if stage == 'agreement':
		fries_agreement = input(f'Would you like some fries? ({format_str("BOLD_UNDERLINE", "Y")}es | {format_str("BOLD_UNDERLINE", "N")}o) ')
		if 'yes' in fries_agreement.lower().strip() or fries_agreement.lower().strip() == 'y':
			fries_selection('choose')
		elif 'no' in fries_agreement.lower().strip() or fries_agreement.lower().strip() == 'n':
			ketchup_selection('agreement')
		else:
			error_handle('yes no', 'fries', fries_agreement)
			fries_selection('agreement')
	elif stage == 'choose':
		friesTable('option')
		fries_size = input('What size of fries? ')
		if fries_size.lower().strip() == 's' or 'small' in fries_size.lower().strip():
			fries_selection('upgrade')
		elif fries_size.lower().strip() == 'm' or 'medium' in fries_size.lower().strip():
			fries_size_selected = 'medium'
			fries_selection('amount')
		elif fries_size.lower().strip() == 'l' or 'large' in fries_size.lower().strip():
			fries_size_selected = 'large'
			fries_selection('amount')
		else:
			error_handle('food selection', 'fries', fries_size)
			fries_selection('choose')
	elif stage == 'upgrade':
		fries_upgrade = input('Would you like to mega-size your fries? ')
		if 'yes' in fries_upgrade.lower().strip() or fries_upgrade.lower().strip() == 'y':
			fries_size_selected = 'large'
		elif 'no' in fries_upgrade.lower().strip() or fries_upgrade.lower().strip() == 'n':
			fries_size_selected = 'small'
		else:
			error_handle('yes no', 'fries', fries_upgrade)
			fries_selection('upgrade')
		fries_selection('amount')
	elif stage == 'amount':
		friesTable('amount')
		fries_amount = input('How many fries? ')
		isInt = bool(re.match(pattern, fries_amount))
		if isInt == True:
			if int(fries_amount) >= 1:
				addToCart(fries_amount, fries.type, fries_size_selected, fries.names, fries.sizes, fries.prices)
				ketchup_selection('agreement')
			else:
				error_handle('food amount', 'fries', fries_amount)
				fries_selection('amount')				
		else:
			error_handle('food amount', 'fries', fries_amount)
			fries_selection('amount')

def ketchup_selection(stage):
	if stage == 'agreement':
		ketchup_agreement = input(f'Would you like some ketchup? ({format_str("BOLD_UNDERLINE", "Y")}es | {format_str("BOLD_UNDERLINE", "N")}o) ')
		if 'yes' in ketchup_agreement.lower().strip() or ketchup_agreement.lower().strip() == 'y':
			ketchup_selection('choose')
		elif 'no' in ketchup_agreement.lower().strip() or ketchup_agreement.lower().strip() == 'n':
			request_receipt()
		else:
			error_handle('yes no', 'ketchup', ketchup_agreement)
			ketchup_selection('agreement')
	elif stage == 'choose':
		ketchupTable()
		ketchup_amount = input('How many packets of ketchup? ')
		isInt = bool(re.match(pattern, ketchup_amount))
		if isInt == True:
			if int(ketchup_amount) >= 1:
				addToCart(ketchup_amount, ketchup.type, ketchup.names, ketchup.names, ketchup.sizes, ketchup.prices)
			else:
				error_handle('food amount', 'ketchup', ketchup_amount)
				ketchup_selection('choose')				
		else:
			error_handle('food amount', 'ketchup', ketchup_amount)
			ketchup_selection('choose')
		request_receipt()

#
# Start Program
#

sandwich_selection('agreement')