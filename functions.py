current_sandwich = ''

class Output_Check():
	def __init__(self, javascript_output, javascript_output_type):
		global cart
		self.chicken_typecases = ['c', 'chicken']
		self.beef_typecases = ['b', 'beef']
		self.tofu_typecases = ['t', 'tofu']
		if javascript_output_type == 'Sandwich Selection':
			self.js_output = str(javascript_output).lower().strip()
		else:
			self.js_output = javascript_output
		self.js_output_type = javascript_output_type
		cart = Cart()

	def check(self):
		global current_sandwich
		if self.js_output_type == 'Sandwich Selection':
			if self.js_output in self.chicken_typecases:
				self.current_sandwich = 'Chicken'
			if self.js_output in self.beef_typecases:
				self.current_sandwich = 'Beef'
			if self.js_output in self.tofu_typecases:
				self.current_sandwich = 'Tofu'
			if self.js_output_type == 'Sandwich Selection':
				self.python_output = f'How many {self.current_sandwich} sandwiches would you like?'
				current_sandwich = self.current_sandwich
				self.python_output_type = 'Sandwich Amount'
				return self.python_output, self.python_output_type
		elif self.js_output_type == 'Sandwich Amount':
			self.cart_sizes, self.cart_types, self.cart_names, self.cart_prices, self.cart_total = cart.add('Regular', 'Sandwich', current_sandwich, self.js_output)	
			self.python_output = f'Added: A {current_sandwich.lower()} sandwich to the cart!'
			self.python_output_type = 'Cart Addition'
			return self.python_output, self.python_output_type, self.cart_sizes, self.cart_types, self.cart_names, self.cart_prices, self.cart_total

#Cart().add('Sandwich', 'Tofu', 'Regular')

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
		self.cart_sizes.append(self.item_size)
		self.cart_types.append(self.item_type)
		self.cart_names.append(self.item_name)
		self.item_price = float(self.item_price) * float(self.item_quantity)
		self.cart_prices.append(self.item_price)
		self.cart_total = sum(self.cart_prices)
		return self.cart_sizes, self.cart_types, self.cart_names, self.cart_prices, self.cart_total