from flask import Flask, render_template, jsonify, request
from functions import Output_Check
import jyserver.Flask as jsf

# Startup
app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Global Variables
javascript_output = None
javascript_output_type = None

@app.route('/')
def index():
	flask_output = 'What type of sandwich would you like?'
	flask_output_type = 'Sandwich Selection'
	return render_template('index.html', flask_output=flask_output, flask_output_type=flask_output_type)

# JavaScript Fetch & Flask Status Report (If Received Vars)
@app.route('/my-route', methods=['POST'])
def my_route():
	global javascript_output
	global javascript_output_type

	javascript_output = request.json['javascript_output']
	javascript_output_type = request.json['javascript_output_type']
	response_data = {'result': f'[POST | 200] Output: {javascript_output} & Output_Type: {javascript_output_type}'}
	return jsonify(response_data)

@app.route('/data', methods=['POST'])
def send_data():
	output_checker = Output_Check(javascript_output, javascript_output_type)
	if javascript_output_type == 'Sandwich Selection':
		flask_output, flask_output_type = output_checker.check()
		return jsonify({'flask_output': flask_output, 'flask_output_type': flask_output_type})
	elif javascript_output_type == 'Sandwich Amount':
		flask_output, flask_output_type, cart_sizes, cart_types, cart_names, cart_prices, cart_total = output_checker.check()
		print(flask_output, flask_output_type)
		print(f'Cart Sizes: {cart_sizes}')
		print(f'Cart Types: {cart_types}')
		print(f'Cart Names: {cart_names}')
		print(f'Cart Prices: {cart_prices}')
		print(f'Cart Total: {cart_total}')
		return jsonify({'flask_output': flask_output, 'flask_output_type': flask_output_type, 'flask_cart_sizes': cart_sizes, 'flask_cart_types': cart_types, 'flask_cart_names': cart_names, 'flask_cart_prices': cart_prices, 'flask_cart_total': cart_total})


if __name__ == '__main__':
    app.run(debug=True)
