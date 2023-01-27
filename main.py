# Imports
import os
from datetime import date
from prettytable import PrettyTable
from prettytable import DOUBLE_BORDER

# Combo Menu Configuration
cart_items = []
cart_item_prices = []
cart_total_cost = 0

# Libary Setups
receipt = PrettyTable()
today = date.today()
receipt.set_style(DOUBLE_BORDER)
receipt.title = f'RECEIPT | {today.month}/{today.day}/{today.year}'
receipt.field_names = ['TYPE', 'NAME', 'SIZE', 'PRICE']


# Global Functions
def clear_console():
  os.system('cls')
  os.system('clear')

def underline(text):
    # Underline start: \033[4m
    # Underline end: \033[0m
    return f'\033[4m{text}\033[0m'


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
          str(item_type).upper(),
          str(items_list),
          str(items_sizes[index]), '$' + str(item_price)
        ])
        receipt.add_row(['', '', '', ''])
        receipt.ad(['TOTAL', '', '', '$' + "{:.2f}".format(cart_total_cost)])
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
        receipt.add_row([
          str(item_type).upper(),
          str(item),
          str(items_sizes), '$' + str(item_price)
        ])
        receipt.add_row(['', '', '', ''])
        receipt.add_row(['TOTAL', '', '', '$' + "{:.2f}".format(cart_total_cost)])
        print(receipt)


# Sandwitch Configuration
class sandwitchs:
  type = 'Sandwitch'
  names = ['Chicken', 'Beef', 'Tofu']
  sizes = 'Regular'
  prices = ['5.25', '6.25', '5.75']


# Beverage Configuration
class beverages:
  type = 'Beverage'
  names = 'Fountain'
  sizes = ['Small', 'Medium', 'Large']
  prices = ['1.00', '1.75', '2.25']


# Fries Configuration
class fries:
  type = 'Side'
  names = 'Fries'
  sizes = ['Small', 'Medium', 'Large']
  prices = ['1.00', '1.50', '2.00']


# Sandwitch Selection
def sandwitch_selection():
    print(f'Options: \n- {underline("Y")}es\n- {underline("N")}o')
    sandwitch_agreement = input('Would you like a sandwitch? ')
    if 'yes' in sandwitch_agreement.lower() or sandwitch_agreement.lower() == 'y':
        print(f'Options: \n- {underline("C")}hicken\n- {underline("B")}eef\n- {underline("T")}ofu')
        sandwitch_selected = input('What type of sandwitch would you like? ')
        if 'c' in sandwitch_selected.lower() or 'chicken' in sandwitch_selected.lower():
            sandwitch_selected = 'chicken'
        elif 'b' in sandwitch_selected.lower() or 'beef' in sandwitch_selected.lower():
            sandwitch_selected = 'beef'
        elif 't' in sandwitch_selected.lower() or 'tofu' in sandwitch_selected.lower():
            sandwitch_selected = 'tofu'
        else:
            print('ERROR')
        addToCart(sandwitchs.type, sandwitch_selected, sandwitchs.names, sandwitchs.sizes, sandwitchs.prices)
    elif 'no' in sandwitch_agreement.lower() or sandwitch_agreement.lower() == 'n':
            beverage_selection()
    else:
        print('ERROR')


# Drink Selection
def beverage_selection():
    print(f'Options: \n- {underline("Y")}es\n- {underline("N")}o')
    beverage_agreement = input('Whould you like a beverage? ')
    if 'yes' in beverage_agreement.lower() or beverage_agreement.lower() == 'y':
        beverage_size = input('What size of beverage? ')
        addToCart(beverages.type, beverage_size, beverages.names, beverages.sizes, beverages.prices)
    elif 'no' in beverage_agreement.lower() or beverage_agreement.lower() == 'n':
        print('hello')


sandwitch_selection()
beverage_selection()
# Fries Selection
#fries_agreement = input('Would you like fries? ')
#if (fries_agreement.lower() in ['yes','y']):
#    fries_size = input('What size of fries? ')
#    if fries_size.lower() == 'small':
#        fries_upgrade = input('Would you like to mega-size your fries? ')
#        if fries_upgrade.lower() in ['yes','y']:
#add cart
#        if fries_upgrade.lower() in ['no','n']:
#add cart
#    else:
#add cart

# Ketchup Selection
#ketchup_ask = input('How many ketchup packets do you want? ')
#if int(ketchup_ask) > 0:
#    ketchup_amount = ketchup_ask
#    print('You got: ' + ketchup_amount + ' packets!')
