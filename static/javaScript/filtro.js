/* Ubicacion */
(function(){
    const ubicacionDropdown = document.getElementById('ubicacion');
    const cards = document.querySelectorAll('.card')
    
    ubicacionDropdown.addEventListener('change', function(){
      const ubicacionSeleccionada = ubicacionDropdown.value;
    
      cards.forEach(card => {
        const ubicacionCard = card.getAttribute('data-ubicacion');
        if (ubicacionSeleccionada === 'Todo el pais' || ubicacionCard === ubicacionSeleccionada){
            card.style.display = 'block';
            console.log(card);
        } else {
          card.style.display = 'none';
        }
      });
    });
  })();
  /* Ubicacion FIN */


  /* Talla */
  (function(){
    const tallaDropdown = document.getElementById('talla');
    const cards = document.querySelectorAll('.card')
    
    tallaDropdown.addEventListener('change', function(){
      const tallaSeleccionada = tallaDropdown.value;
    
      cards.forEach(card => {
        const tallaCard = card.getAttribute('data-talla');
        if (tallaSeleccionada === 'Todas las tallas' || tallaCard === tallaSeleccionada){
            card.style.display = 'block';
            console.log(card);
        } else {
          card.style.display = 'none';
        }
      });
    });
  })();
/* Talla FIN */


/* Precio */
function filterProducts(minPrice, maxPrice) {
    var products = Array.from(document.querySelectorAll(".card"));
    products.forEach(x => x.style.display = 'block')
    products.filter(x => {
        var priceElement = x.querySelector(".card-price");
        var price = parseFloat(priceElement.innerText.replace('$', ''));
        return price < minPrice || price > maxPrice;
    }).forEach(element => {
        element.style.display = 'none'
    });
}

var minInput = document.getElementById("min");
var maxInput = document.getElementById("max");

function filterByInputs() {
    filterProducts(parseFloat(minInput.value), parseFloat(maxInput.value));
}

minInput.addEventListener("keyup", filterByInputs);
maxInput.addEventListener("keyup", filterByInputs);
/* Precio FIN */


/* Condicion */
(function(){
    const condicionDropdown = document.getElementById('condicion');
    const cards = document.querySelectorAll('.card')
    
    condicionDropdown.addEventListener('change', function(){
      const condicionSeleccionada = condicionDropdown.value;
    
      cards.forEach(card => {
        const condicionCard = card.getAttribute('data-condicion');
        if (condicionSeleccionada === 'Nuevo y usado' || condicionCard === condicionSeleccionada){
            card.style.display = 'block';
            console.log(card);
        } else {
          card.style.display = 'none';
        }
      });
    });
  })();
/* Condicion FIN */