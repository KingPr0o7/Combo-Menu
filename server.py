from flask import Flask, render_template, jsonify, request
from functions import Output_Check
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
	return render_template('index.html', flask_output=flask_output, flask_output_type=flask_output_type)

# Fetch JavaScript output and save to Flask
@app.route('/my-route', methods=['POST'])
def my_route():
	global javascript_output
	global javascript_output_type

	javascript_output = request.json['javascript_output']
	javascript_output_type = request.json['javascript_output_type']
	response_data = {'result': f'[POST | 200] Output: {javascript_output} & Output_Type: {javascript_output_type}'} # Verify Results
	if javascript_output_type == 'Sandwich Cart Addition' or javascript_output_type == 'Ketchup Cart Addition':
		send_data()
	return jsonify(response_data) # Verify Results

# Send input from Flask to Javascript 
@app.route('/data', methods=['POST'])
def send_data():
	print(javascript_output, javascript_output_type)
	output_checker = Output_Check(javascript_output, javascript_output_type)
	# Depending on type, have to change what's returned
	if javascript_output_type == 'Sandwich Agreement':
		flask_output, flask_output_type = output_checker.check()
		return jsonify({'flask_output': flask_output, 'flask_output_type': flask_output_type})
	elif javascript_output_type == 'Sandwich Selection':
		flask_output, flask_output_type = output_checker.check()
		return jsonify({'flask_output': flask_output, 'flask_output_type': flask_output_type})
	elif javascript_output_type == 'Sandwich Amount':
		flask_output, flask_output_type, cart_sizes, cart_types, cart_names, cart_prices, cart_total, item_quantity = output_checker.check() # Assignment of variables from functions.py
		return jsonify({'flask_output': flask_output, 'flask_output_type': flask_output_type, 'flask_cart_sizes': cart_sizes, 'flask_cart_types': cart_types, 'flask_cart_names': cart_names, 'flask_cart_prices': cart_prices, 'flask_cart_total': cart_total, 'flask_item_quantity': item_quantity})
	elif javascript_output_type == 'Sandwich Cart Addition':
		flask_output, flask_output_type = output_checker.check()
		return jsonify({'flask_output': flask_output, 'flask_output_type': flask_output_type})
	elif javascript_output_type == 'Drink Agreement':
		flask_output, flask_output_type = output_checker.check()
		return jsonify({'flask_output': flask_output, 'flask_output_type': flask_output_type})		
	elif javascript_output_type == 'Drink Size Selection':
		flask_output, flask_output_type = output_checker.check()
		return jsonify({'flask_output': flask_output, 'flask_output_type': flask_output_type})
	elif javascript_output_type == 'Drink Amount':
		flask_output, flask_output_type, cart_sizes, cart_types, cart_names, cart_prices, cart_total, item_quantity = output_checker.check() # Assignment of variables from functions.py
		return jsonify({'flask_output': flask_output, 'flask_output_type': flask_output_type, 'flask_cart_sizes': cart_sizes, 'flask_cart_types': cart_types, 'flask_cart_names': cart_names, 'flask_cart_prices': cart_prices, 'flask_cart_total': cart_total, 'flask_item_quantity': item_quantity})
	elif javascript_output_type == 'Drink Cart Addition':
		flask_output, flask_output_type = output_checker.check()
		return jsonify({'flask_output': flask_output, 'flask_output_type': flask_output_type})		
	elif javascript_output_type == 'Fries Agreement':
		flask_output, flask_output_type = output_checker.check()
		return jsonify({'flask_output': flask_output, 'flask_output_type': flask_output_type})		
	elif javascript_output_type == 'Fries Size Selection':
		flask_output, flask_output_type = output_checker.check()
		return jsonify({'flask_output': flask_output, 'flask_output_type': flask_output_type})		
	elif javascript_output_type == 'Fries Upgrade':
		flask_output, flask_output_type = output_checker.check()
		return jsonify({'flask_output': flask_output, 'flask_output_type': flask_output_type})		
	elif javascript_output_type == 'Fries Amount':
		flask_output, flask_output_type, cart_sizes, cart_types, cart_names, cart_prices, cart_total, item_quantity = output_checker.check() # Assignment of variables from functions.py
		return jsonify({'flask_output': flask_output, 'flask_output_type': flask_output_type, 'flask_cart_sizes': cart_sizes, 'flask_cart_types': cart_types, 'flask_cart_names': cart_names, 'flask_cart_prices': cart_prices, 'flask_cart_total': cart_total, 'flask_item_quantity': item_quantity})
	elif javascript_output_type == 'Fries Cart Addition':
		flask_output, flask_output_type = output_checker.check()
		return jsonify({'flask_output': flask_output, 'flask_output_type': flask_output_type})				
	elif javascript_output_type == 'Ketchup Agreement':
		flask_output, flask_output_type = output_checker.check()
		return jsonify({'flask_output': flask_output, 'flask_output_type': flask_output_type})		
	elif javascript_output_type == 'Ketchup Amount':
		flask_output, flask_output_type, cart_sizes, cart_types, cart_names, cart_prices, cart_total, item_quantity = output_checker.check() # Assignment of variables from functions.py
		return jsonify({'flask_output': flask_output, 'flask_output_type': flask_output_type, 'flask_cart_sizes': cart_sizes, 'flask_cart_types': cart_types, 'flask_cart_names': cart_names, 'flask_cart_prices': cart_prices, 'flask_cart_total': cart_total, 'flask_item_quantity': item_quantity})
	elif javascript_output_type == 'Ketchup Cart Addition':
		flask_output, flask_output_type = output_checker.check()
		return jsonify({'flask_output': flask_output, 'flask_output_type': flask_output_type})			
	elif javascript_output_type == 'Done!':
		flask_output, flask_output_type = output_checker.check()
		return jsonify({'flask_output': flask_output, 'flask_output_type': flask_output_type})				

if __name__ == '__main__':
    app.run(debug=True)
