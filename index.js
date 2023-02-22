// Settings 
const typing_speed = 50;

// Immutables
const sandwich_typecases = ['chicken', 'beef', 'tofu', 'c', 'b', 't'];
const size_typecases = ['small', 'medium', 'large', 's', 'm', 'l'];
var bot_typing_status = false;
var chat_count = 1;

// Elements
const cursor = document.getElementById("cursor");
const form = document.getElementById('forum-content');
const old_element = document.getElementById('human-chat');
const submit_forum = document.getElementById('submit-input');
const submit_button = document.getElementById('submit');
const container_holder = document.getElementById('chat-container');
const container = document.getElementById('chat-content');
const sandwich_options = document.getElementById('sandwich-options');
old_element.remove();

// Functions
function input(msg) {
	let bot_msg = document.getElementById('bot-msg');
	bot_msg.textContent = '';
	bot_msg.appendChild(cursor);
	document.getElementById('bot-msg').appendChild(sandwich_options);
	type("bot-msg", msg, typing_speed, 0, true);
}

function add_chat(msg) {
	chat_count++;
	var clone = old_element.cloneNode(true);
	clone.children[0].innerHTML = msg;
	clone.classList.remove('starter-human-chat');
	container.appendChild(clone);
	container_holder.scrollBy(0, 2000);
	if (chat_count % 2 == 0) {
		document.getElementById('bot-msg').removeChild(cursor);
	}
}

function type(targetElement, textToType, speed, index, cursorMode) {
	let element = document.getElementById(`${targetElement}`);
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
		submit_forum.style.boxShadow = 'inset 0 0 0 2px red';
		submit_forum.style.color = 'red';
	} else {
		submit_forum.style.boxShadow = 'none';
		submit_forum.style.color = 'white';
	}
}

// Events 

form.addEventListener('submit', function(event) {
	event.preventDefault();
	if (bot_typing_status == false) {
		if (!sandwich_typecases.includes(submit_forum.value.toLowerCase())) {
			input_border(true);
		} else {
			input_border(false);
			add_chat(submit_forum.value);
			submit_forum.value = '';
		}
	}
});


submit_forum.addEventListener('input', function() {
	if (sandwich_typecases.includes(submit_forum.value.toLowerCase())) {
		input_border(false);
	}
	if (submit_forum.value == '') {
		input_border(false);
	}
});