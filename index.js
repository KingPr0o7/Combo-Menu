function put_object(x) {
	console.log(x)
}

const submit_button = document.getElementById('submit');

submit_button.addEventListener('click', function(event) {
	event.preventDefault();
	alert('Hello World!')
});