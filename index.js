// Settings 
const typing_speed = 30; // Milliseconds

// Immutables
const sandwich_typecases = ['chicken', 'beef', 'tofu', 'c', 'b', 't'];
const size_typecases = ['small', 'medium', 'large', 's', 'm', 'l'];
var bot_typing_status = false;
var chat_count = 1;

// Elements
const chat = document.getElementById('chat');
const chat_wrapper = document.getElementById('chat-wrapper');

const cursor = document.getElementById("cursor");

const bot_chat = document.querySelector('.bot-msg');
const human_chat = document.querySelector('.human-chat');
human_chat.remove();

const form = document.getElementById('chat-form');
const form_input = document.getElementById('form-input');
const submit_button = document.getElementById('form-submit');

// Functions
function input(msg) {
	let bot_msg = document.querySelector('.bot-msg');
	bot_msg.textContent = '';
	bot_msg.appendChild(cursor);
	type(".bot-msg", msg, typing_speed, 0, true);
}

function add_chat(msg) {
	chat_count++;
	let clone = human_chat.cloneNode(true);
	clone.children[0].innerHTML = msg;
	clone.id = '';
	chat_wrapper.appendChild(clone);
	chat.scrollBy(0, 2000);
	if (chat_count % 2 == 0) {
		bot_chat.removeChild(cursor);
	}
}

function type(targetElement, textToType, speed, index, cursorMode) {
	let element = document.querySelector(`${targetElement}`);
	let text = `${textToType}`;
	if (index < text.length) {
		cursor.removeAttribute('blinking', '');
		bot_typing_status = true;
		if (cursorMode == true) {
			element.removeChild(cursor);
			element.innerHTML += text.charAt(index);  
			index++;
			element.appendChild(cursor);		  
		} else {
			element.innerHTML += text.charAt(index);  
			index++;			
		}
		setTimeout(type, speed, `${targetElement}`, text, speed, index, cursorMode);
	} else {
		cursor.setAttribute('blinking', '');
		bot_typing_status = false;
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

// Events 

form.addEventListener('submit', function(event) {
	event.preventDefault();
	if (bot_typing_status == false) {
		if (!sandwich_typecases.includes(form_input.value.toLowerCase())) {
			input_border(true);
		} else {
			input_border(false);
			add_chat(form_input.value);
			form_input.value = '';
		}
	}
});


form_input.addEventListener('input', function() {
	if (sandwich_typecases.includes(form_input.value.toLowerCase())) {
		input_border(false);
	}
	if (form_input.value == '') {
		input_border(false);
	}
});