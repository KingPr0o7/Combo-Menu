from flask import Flask, render_template, jsonify, request
import jyserver.Flask as jsf

app = Flask(__name__)

# Flask to JavaScript

@app.route('/')
def index():
    python_output = 'What type of sandwich would you like?'
    return render_template('index.html', python_output=python_output)

# JavaScript Fetch & Flask Status Report (If Received Vars)

@app.route('/my-route', methods=['POST'])
def my_route():
	javascript_output = request.json['javascript_output']
	response_data = {'result': f'FLASK: JAVASCRIPT_VAR_FOUND [{javascript_output}] (200)'}
	print(javascript_output)
	return jsonify(response_data)

if __name__ == '__main__':
	app.run()