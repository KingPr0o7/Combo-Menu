# Global variables
current_sandwich = ''

# Checks JS outputs from server.py and returns outputs for JS.
class Output_Check():
	def __init__(self, javascript_output, javascript_output_type):
		global cart

		self.chicken_typecases = ['c', 'chicken']
		self.beef_typecases = ['b', 'beef']
		self.tofu_typecases = ['t', 'tofu']
		self.small_typecases = ['s', 'small']
		self.medium_typecases = ['m', 'medium']
		self.large_typecases = ['l', 'large']
		if javascript_output_type == 'Sandwich Selection' or javascript_output_type == 'Drink Size Selection':
			self.js_output = str(javascript_output).lower().strip()
		else:
			self.js_output = javascript_output
		self.js_output_type = javascript_output_type
		cart = Cart()

	def check(self):
		global current_sandwich
		global current_drink_size
		global current_fries_size

		# Depending on type, have to change what's returned
		if self.js_output_type == 'Sandwich Agreement':
			self.python_output = 'What type of sandwich would you like?'
			self.python_output_type = 'Sandwich Selection'
			return self.python_output, self.python_output_type			
		elif self.js_output_type == 'Sandwich Selection':
			if self.js_output in self.chicken_typecases:
				self.current_sandwich = 'chicken'
			if self.js_output in self.beef_typecases:
				self.current_sandwich = 'beef'
			if self.js_output in self.tofu_typecases:
				self.current_sandwich = 'tofu'
			self.python_output = f'How many {self.current_sandwich} sandwiches would you like?'
			current_sandwich = self.current_sandwich
			self.python_output_type = 'Sandwich Amount'
			return self.python_output, self.python_output_type
		elif self.js_output_type == 'Sandwich Amount':
			self.cart_sizes, self.cart_types, self.cart_names, self.cart_prices, self.cart_total, self.item_quantity = cart.add('Regular', 'Sandwich', current_sandwich, self.js_output)	
			self.python_output = quantity_fixer(self.item_quantity, current_sandwich.lower(), str(self.cart_types[0]).lower())
			self.python_output_type = 'Sandwich Cart Addition'
			return self.python_output, self.python_output_type, self.cart_sizes, self.cart_types, self.cart_names, self.cart_prices, self.cart_total, self.item_quantity
		elif self.js_output_type == 'Sandwich Cart Addition':
			self.python_output = 'Would you like a fountain drink?'
			self.python_output_type = 'Drink Agreement'
			return self.python_output, self.python_output_type
		elif self.js_output_type == 'Drink Agreement':
			self.python_output = 'What size of drink would you like?'
			self.python_output_type = 'Drink Size Selection'
			return self.python_output, self.python_output_type      
		elif self.js_output_type == 'Drink Size Selection':
			if self.js_output in self.small_typecases:
				self.drink_size = 'Small'
			if self.js_output in self.medium_typecases:
				self.drink_size = 'Medium'
			if self.js_output in self.large_typecases:
				self.drink_size = 'Large'
			current_drink_size = self.drink_size
			self.python_output = 'How many fountain drinks would you like?'
			self.python_output_type = 'Drink Amount'
			return self.python_output, self.python_output_type
		elif self.js_output_type == 'Drink Amount':
			self.cart_sizes, self.cart_types, self.cart_names, self.cart_prices, self.cart_total, self.item_quantity = cart.add(current_drink_size, 'Drink', 'Fountain', self.js_output)	
			self.python_output = quantity_fixer(self.item_quantity, 'fountain', 'drink')
			self.python_output_type = 'Drink Cart Addition'
			return self.python_output, self.python_output_type, self.cart_sizes, self.cart_types, self.cart_names, self.cart_prices, self.cart_total, self.item_quantity			
		elif self.js_output_type == 'Drink Cart Addition':
			self.python_output = 'Would you like some fries?'
			self.python_output_type = 'Fries Agreement'
			return self.python_output, self.python_output_type    	
		elif self.js_output_type == 'Fries Agreement':
			self.python_output = 'What size of fries would you like?'
			self.python_output_type = 'Fries Size Selection'
			return self.python_output, self.python_output_type     			
		elif self.js_output_type == 'Fries Size Selection':
			if self.js_output in self.small_typecases:
				self.fries_size = 'Small'
				self.python_output_type = 'Fries Upgrade'
				self.python_output = 'Would you like to mega-size your fries?'
			if self.js_output in self.medium_typecases:
				self.fries_size = 'Medium'
				self.python_output_type = 'Fries Amount'
				self.python_output = 'How many french fries would you like?'
			if self.js_output in self.large_typecases:
				self.fries_size = 'Large'
				self.python_output_type = 'Fries Amount'
				self.python_output = 'How many french fries would you like?'
			current_fries_size = self.fries_size		
			return self.python_output, self.python_output_type  
		elif self.js_output_type == 'Fries Upgrade':
			if self.js_output == 'y' or self.js_output == 'yes':
				current_fries_size = 'Large'
			self.python_output = 'How many french fries would you like?'	
			self.python_output_type = 'Fries Amount'	
			return self.python_output, self.python_output_type  	
		elif self.js_output_type == 'Fries Amount':
			self.cart_sizes, self.cart_types, self.cart_names, self.cart_prices, self.cart_total, self.item_quantity = cart.add(current_fries_size, 'Fries', 'French', self.js_output)	
			self.python_output = quantity_fixer(self.item_quantity, 'french', 'fries')
			self.python_output_type = 'Fries Cart Addition'
			return self.python_output, self.python_output_type, self.cart_sizes, self.cart_types, self.cart_names, self.cart_prices, self.cart_total, self.item_quantity					

def quantity_fixer(quantity, item, type):
	if int(quantity) <=1:
		if type == 'sandwich':
			return f'Okay! Added a {item} {type} to the cart!'
		elif type == 'drink':
			return f'Okay! Added a {item} {type} to the cart!'
		elif type == 'fries':
			return f'Okay! Added {item} {type} to the cart!'
	else:
		if type == 'sandwich':
			return f'Okay! Added {quantity} {item} {type}es to the cart!'
		elif type == 'drink':
			return f'Okay! Added {quantity} {item} {type}s to the cart!'
		elif type == 'fries':
			return f'Okay! Added {quantity} {item} {type} to the cart!'

# Stores and sends variables for the cart.
class Cart():
	def __init__(self):
		self.item_id = 0
		self.cart_total = 0
		self.cart_prices = []
		self.cart_sizes = []
		self.cart_types = []
		self.cart_names = []
		self.sandwich_prices = [5.25, 6.25, 5.75] # Chicken, Beef, and Tofu
		self.drink_prices = [1.00, 1.75, 2.25] # Small, Medium, and Large
		self.fries_prices = [1.00, 1.50, 2.00] # Small, Medium, and Large
		self.ketchup_price = 0.25

	def add(self, item_size, item_type, item_name, item_quantity):
		global current_sandwich

		self.item_size = item_size
		self.item_type = item_type
		self.item_name = item_name
		self.item_quantity = item_quantity
		if self.item_type == 'Sandwich':
			if self.item_name == 'chicken':
				self.item_id = 0
			if self.item_name == 'beef':
				self.item_id = 1
			if self.item_name == 'tofu':
				self.item_id = 2
			self.item_price = self.sandwich_prices[self.item_id]
		if self.item_type == 'Drink':
			if self.item_size == 'Small':
				self.item_id = 0
			if self.item_size == 'Medium':
				self.item_id = 1
			if self.item_size == 'Large':
				self.item_id = 2			
			self.item_price = self.drink_prices[self.item_id]	
			print(self.item_price)
		if self.item_type == 'Fries':
			if self.item_size == 'Small':
				self.item_id = 0
			if self.item_size == 'Medium':
				self.item_id = 1
			if self.item_size == 'Large':
				self.item_id = 2			
			self.item_price = self.fries_prices[self.item_id]	
			print(self.item_price)
		if int(self.item_quantity) >= 2:
			for i in range(int(self.item_quantity)):
				self.cart_sizes.append(self.item_size)
				self.cart_types.append(self.item_type)
				self.cart_names.append(self.item_name)
				self.cart_prices.append(self.item_price)
		else:
			self.cart_sizes.append(self.item_size)
			self.cart_types.append(self.item_type)
			self.cart_names.append(self.item_name)
			self.cart_prices.append(self.item_price)
		self.cart_total = sum(self.cart_prices)
		self.cart_total = '{:.2f}'.format(self.cart_total)
		return self.cart_sizes, self.cart_types, self.cart_names, self.cart_prices, self.cart_total, self.item_quantity