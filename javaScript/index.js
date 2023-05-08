const inputQuantity = document.querySelector('.input-quantity');
const btnIncrement = document.querySelector('#increment');
const btnDecrement = document.querySelector('#decrement');

let valueByDefault = parseInt(inputQuantity.value);

// Funciones Click

btnIncrement.addEventListener('click', () => {
	valueByDefault += 1;
	inputQuantity.value = valueByDefault;
});

btnDecrement.addEventListener('click', () => {
	if (valueByDefault === 1) {
		return;
	}
	valueByDefault -= 1;
	inputQuantity.value = valueByDefault;
});

// Toggle
// Constantes Toggle Titles
const toggleDescription = document.querySelector(
	'.title-description'
);
const toggleAdditionalInformation = document.querySelector(
	'.title-additional-information'
);
const toggleReviews = document.querySelector('.title-reviews');

// Constantes Contenido Texto
const contentDescription = document.querySelector(
	'.text-description'
);
const contentAdditionalInformation = document.querySelector(
	'.text-additional-information'
);
const contentReviews = document.querySelector('.text-reviews');

// Funciones Toggle
toggleDescription.addEventListener('click', () => {
	contentDescription.classList.toggle('hidden');
});

toggleAdditionalInformation.addEventListener('click', () => {
	contentAdditionalInformation.classList.toggle('hidden');
});

toggleReviews.addEventListener('click', () => {
	contentReviews.classList.toggle('hidden');
});





function filterProducts(minPrice, maxPrice) {
    var products = Array.from(document.querySelectorAll(".card"));
    products.forEach(x => x.style.opacity = '1')
    products.filter(x => {
        var priceElement = x.querySelector(".price");
        var price = parseFloat(priceElement.innerText.replace('$', ''));
        return price < minPrice || price > maxPrice;
    }).forEach(element => {
        element.style.opacity = '0.3'
    });
}

var minInput = document.getElementById("min");
var maxInput = document.getElementById("max");

function filterByInputs() {
    filterProducts(parseFloat(minInput.value), parseFloat(maxInput.value));
}

minInput.addEventListener("keyup", filterByInputs);
maxInput.addEventListener("keyup", filterByInputs);