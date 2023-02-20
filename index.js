const cursor = document.getElementById("cursor");
function input(msg) {
	let bot_msg = document.getElementById('bot-msg');
	bot_msg.textContent = '';
	bot_msg.appendChild(cursor);
	type("bot-msg", msg, 50, 0, true);
}

const submit_forum = document.getElementById('submit-input');
const submit_button = document.getElementById('submit');

submit_button.addEventListener('click', function(event) {
	event.preventDefault();
	add_chat(submit_forum.value)
	submit_forum.value = ''
});

function add_chat(msg) {
	var container_holder = document.getElementById('chat-container')
	var container = document.getElementById('chat-content')
	var old_element = document.getElementById('human-chat')
	var clone = old_element.cloneNode(true)
	clone.children[0].innerHTML = msg
	container.appendChild(clone);
	container_holder.scrollBy(0, 2000)
	document.getElementById('bot-msg').removeChild(cursor)
}

// "Real" Typing Characters
function type(targetElement, textToType, speed, index, cursorMode) {
	let element = document.getElementById(`${targetElement}`);
	let text = `${textToType}`;
	if (index < text.length) {
		cursor.removeAttribute('blinking', '')
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
	}
}