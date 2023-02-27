// Settings 
const typing_speed = 30; // Milliseconds

// Immutables
const sandwich_typecases = ['chicken', 'beef', 'tofu', 'c', 'b', 't'];
const sandwich_prices = [5.25, 6.25, 5.75] // Chicken, Beef, and Tofu
const drink_prices = [1.00, 1.75, 2.25] // Small, Medium, and Large
const fries_prices = [1.00, 1.50, 2.00] // Small, Medium, and Large
const size_typecases = ['small', 'medium', 'large', 's', 'm', 'l'];
var bot_typing_status = false;
var chat_count = 1;
var current_bot_message = ''
var current_person_message = '';
var flask_output = document.getElementById('flask-output').textContent;
var flask_output_type = document.getElementById('flask-output-type').textContent;
var flask_cart_prices = document.getElementById('flask-cart-prices').textContent;
var flask_cart_sizes = document.getElementById('flask-cart-sizes').textContent;
var flask_cart_types = document.getElementById('flask-cart-types').textContent;
var flask_cart_names = document.getElementById('flask-cart-names').textContent;
var flask_cart_total = document.getElementById('flask-cart-total').textContent;

// Elements
const chat = document.getElementById('chat');
const chat_wrapper = document.getElementById('chat-wrapper');
const cursor = document.getElementById("cursor");

const item_options = document.querySelector('.bot-options');
const food_options = document.querySelector('.item-option');
item_options.remove();
food_options.remove();

const bot_chat = document.querySelector('.bot-chat');
const human_chat = document.querySelector('.human-chat');
bot_chat.remove();
human_chat.remove();

const cart = document.querySelector('.shopping-cart');
cart.remove();

const form = document.getElementById('chat-form');
const form_parameters = document.getElementById('form-parameters');
const form_input = document.getElementById('form-input');
const submit_button = document.getElementById('form-submit');

// Functions
function input(msg) {
	let clone = bot_chat.cloneNode(true);
	clone_msg = clone.querySelector('.bot-msg[active]');
	clone_msg.textContent = '';
	clone.id = ''
	clone_msg.appendChild(cursor);
	chat_wrapper.appendChild(clone);
	console.log(clone_msg);
	type(".bot-msg[active]", msg, typing_speed, 0);
	current_bot_message = msg;
	flask_output_type = document.getElementById('flask-output-type').textContent;
	if (flask_output_type == 'Sandwich Selection') {
		form_parameters.textContent = '(C)hicken, (B)eef, or (T)ofu'
	}
	if (flask_output_type == 'Sandwich Amount') {
		form_parameters.textContent = '>=1 AND !==0'
	}
}

function add_chat(msg) {
	chat_count++;
	let clone = human_chat.cloneNode(true);
	clone.children[0].innerHTML = msg;
	clone.id = '';
	chat_wrapper.appendChild(clone);
	chat.scrollBy(0, 2000);
	cursor.remove()
	current_human_message = msg;
	sendVariables(current_human_message)
	fetchVariables()
}

function type(targetElement, textToType, speed, index) {
	element = document.querySelector(`${targetElement}`);
	let text = `${textToType}`;
	if (index < text.length) {
		cursor.removeAttribute('blinking', '');
		bot_typing_status = true;
		cursor.remove();
		element.innerHTML += text.charAt(index);  
		index++;
		element.appendChild(cursor);		  
		setTimeout(type, speed, `${targetElement}`, text, speed, index);
	} else {
		cursor.setAttribute('blinking', '');
		bot_typing_status = false;
		if (flask_output_type == 'Sandwich Selection') {
			add_all_item_options();
		}
		if (flask_output_type == 'Cart Addition' || flask_output_type == 'Show Cart') {
			show_cart();
		}
		element.removeAttribute('active');
		document.querySelector('.bot-msg-wrapper[active]').removeAttribute('active');
		document.querySelector('.bot-chat[active]').removeAttribute('active');
	}
}

function input_border(toggle) {
	if (toggle == true) {
		form_input.style.boxShadow = 'inset 0 0 0 2px red';
		form_input.style.color = 'red';
	} else {
		form_input.style.boxShadow = 'none';
		form_input.style.color = 'white';
	}
}

function add_item_option(cloneTo, item_id, item_title, item_size, item_type, item_name) {
	let new_item = food_options.cloneNode(true);
	new_item.id = '';
	new_item.querySelector('.item-option-title').textContent = item_title;
	if (item_type == 'Sandwich') {
		new_item.querySelector('.item-price').textContent = `$${sandwich_prices[item_id]}`;
	}
	new_item.querySelector('.item-size').textContent = item_size;
	new_item.querySelector('.item-type').textContent = item_type;
	new_item.querySelector('.item-name').textContent = item_name;
	cloneTo.appendChild(new_item);
}

function add_all_item_options() {
	if (current_bot_message == 'What type of sandwich would you like?') {
		let new_item_options = item_options.cloneNode(true);
		add_item_option(new_item_options, 0, 'Chicken Sandwich', 'Regular', 'Sandwich', 'Chicken');
		add_item_option(new_item_options, 1, 'Beef Sandwich', 'Regular', 'Sandwich', 'Beef');
		add_item_option(new_item_options, 2, 'Tofu Sandwich', 'Regular', 'Sandwich', 'Tofu');
		document.querySelector('.bot-msg-wrapper[active]').append(new_item_options);
	}	
	document.querySelector('.bot-chat').style.alignItems = 'flex-start';
}

function show_cart() {
	let new_cart = cart.cloneNode(true);
	flask_cart_prices = document.getElementById('flask-cart-prices');
	flask_cart_names = document.getElementById('flask-cart-names');
	flask_cart_types = document.getAnimations('flask-cart-types');
	flask_cart_sizes = document.getElementById('flask-cart-sizes');
	flask_cart_total = document.getElementById('flask-cart-total');
	let prices = ''
	let names = ''
	let sizes = ''
	if (flask_cart_names.length >= 2) {
		prices = flask_cart_prices.textContent;
		names = flask_cart_names.textContent;
		types = flask_cart_types.textContent;
		sizes = flask_cart_sizes.textContent;

		prices = prices.split(', ');
		names = names.split(', ');
		types = types.split(', ');
		sizes = sizes.split(', ');
	} else {
		prices = flask_cart_prices.textContent;
		names = flask_cart_names.textContent;
		sizes = flask_cart_sizes.textContent;
		total = flask_cart_total.textContent;

		new_cart.querySelector('.cart-item-name').textContent = `${names.charAt(0).toUpperCase() + names.slice(1)} Sandwich`;
		new_cart.querySelector('.cart-item-attr').textContent = `Size: ${sizes}`;
		new_cart.querySelector('.cart-item-price').textContent = `$${prices}`;
		new_cart.querySelector('.cart-discount').remove();
		new_cart.querySelector('.cart-total').textContent = `Total: $${total}`;
	}
	console.log(prices);
	document.querySelector('.bot-msg-wrapper[active]').append(new_cart);
	document.querySelector('.bot-chat[active]').style.alignItems = 'flex-start';
}

// Events 

form.addEventListener('submit', function(event) {
	event.preventDefault();
	if (bot_typing_status == false) {
		if (flask_output_type == 'Sandwich Selection') {
			if (!sandwich_typecases.includes(form_input.value.toLowerCase().trim())) {
				input_border(true);
			} else {
				input_border(false);
				add_chat(form_input.value);
				form_input.value = '';
			}
		} else if (flask_output_type == 'Sandwich Amount') {
			if (parseInt(form_input.value) !== 0 && parseInt(form_input.value) > 0) {
				input_border(false);
				add_chat(form_input.value);
				form_input.value = '';
			} else {
				input_border(true);
				console.log(form_input.value)
			}
		}
	}
});


form_input.addEventListener('input', function() {
	if (sandwich_typecases.includes(form_input.value.toLowerCase().trim())) {
		input_border(false);
	}
	if (form_input.value == '') {
		input_border(false);
	}
});

input(flask_output)

// Flask to JavaScript
function fetchVariables() {
    fetch('/data', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    })
	// Data Check
    .then(response => response.json())
	// Data Fetch
    .then(data => {
        document.getElementById('flask-output').textContent = data.flask_output;
		document.getElementById('flask-output-type').textContent = data.flask_output_type;
		document.getElementById('flask-cart-prices').textContent = data.flask_cart_prices;
		document.getElementById('flask-cart-sizes').textContent = data.flask_cart_sizes;
		document.getElementById('flask-cart-types').textContent = data.flask_cart_types;
		document.getElementById('flask-cart-names').textContent = data.flask_cart_names;
		document.getElementById('flask-cart-total').textContent =  data.flask_cart_total;
		input(data.flask_output);
    }).catch(error => {
    console.error('Error:', error);
});
}

// JavaScript to Flask

function sendVariables() {
    var javascript_output = current_human_message;
	var javascript_output_type = flask_output_type;
    fetch('/my-route', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            javascript_output: javascript_output,
			javascript_output_type: javascript_output_type
        })
    })
	// Data Check
    .then(response => response.json())
	// Data Fetch
    .then(data => {
        console.log(data.result);
    }).catch(error => {
    console.error('Error:', error);
});
}