from flask import Flask, render_template, jsonify, request
import jyserver.Flask as jsf

app = Flask(__name__)

@app.route('/')
def index():
    message = 'What type of sandwich would you like?'
    return render_template('index.html', message=message)

@app.route('/my-route', methods=['POST'])
def my_route():
	my_variable = request.json['myVariable']
	# Do something with my_variable here
	response_data = {'result': 'OK'}
	print(my_variable)
	return jsonify(response_data)

if __name__ == '__main__':
	app.run()