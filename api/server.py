from flask import Flask, render_template, jsonify, request
from functions import Output_Check, clear_item_types
import jyserver.Flask as jsf

# App creation
app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Global variables
javascript_output = None
javascript_output_type = None

# Startup (First output to JavaScript)
@app.route('/')
def index():
	flask_output = 'Would you like a sandwich?'
	flask_output_type = 'Sandwich Agreement'
	clear_item_types()
	return render_template('index.html', flask_output=flask_output, flask_output_type=flask_output_type)

# Fetch JavaScript output and save to Flask
@app.route('/my-route', methods=['POST'])
def my_route():
	global javascript_output
	global javascript_output_type

	javascript_output = request.json['javascript_output']
	javascript_output_type = request.json['javascript_output_type']
	response_data = {'result': f'[POST | 200] Output: {javascript_output} & Output_Type: {javascript_output_type}'} # Verify Results
	if javascript_output_type == 'Sandwich Cart Addition' or javascript_output_type == 'Drink Cart Addition' or javascript_output_type == 'Fries Cart Addition' or javascript_output_type == 'Ketchup Cart Addition':
		send_data()
	return jsonify(response_data) # Verify Results

# Send input from Flask to Javascript 
@app.route('/data', methods=['POST'])
def send_data():
	output_checker = Output_Check(javascript_output, javascript_output_type)
	print(javascript_output, javascript_output_type)
	# Depending on type, have to change what's returned
	statement_returns = ['Sandwich Agreement', 'Sandwich Selection', 'Sandwich Cart Addition', 'Drink Agreement', 'Drink Size Selection', 'Drink Cart Addition', 'Fries Agreement', 'Fries Size Selection', 'Fries Upgrade', 'Fries Cart Addition', 'Ketchup Agreement', 'Ketchup Cart Addition', 'Done!']
	cart_returns = ['Sandwich Amount', 'Drink Amount', 'Fries Amount', 'Ketchup Amount']
	if javascript_output_type in statement_returns:
		flask_output, flask_output_type = output_checker.check()
		return jsonify({'flask_output': flask_output, 'flask_output_type': flask_output_type})	
	elif javascript_output_type in cart_returns:
		flask_output, flask_output_type, cart_sizes, cart_types, cart_names, cart_prices, cart_total, item_quantity, coupon_eligibility = output_checker.check() # Assignment of variables from functions.py
		return jsonify({'flask_output': flask_output, 'flask_output_type': flask_output_type, 'flask_cart_sizes': cart_sizes, 'flask_cart_types': cart_types, 'flask_cart_names': cart_names, 'flask_cart_prices': cart_prices, 'flask_cart_total': cart_total, 'flask_item_quantity': item_quantity, 'flask_coupon_eligibility': coupon_eligibility})		

if __name__ == '__main__':
    app.run()
