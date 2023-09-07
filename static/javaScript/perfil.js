// Boton modal
const btnLanzarModal = document.querySelector('#lanzar-modal');
const btnOcultarModal = document.querySelector('#ocultar-modal');

const contModal = document.querySelector('.contenedor-modal');

const nombreInput = document.querySelector('#nombre');
const puestoInput = document.querySelector('#puesto');

btnLanzarModal.addEventListener('click', (e) => {
    e.preventDefault();
    contModal.classList.add('mostrar');
});

btnOcultarModal.addEventListener('click', (e) => {
    e.preventDefault();
    contModal.classList.remove('mostrar');

    const usuario = document.querySelector('.btn-superiores');

    const pNombre = document.createElement('p');
    pNombre.textContent = nombreInput.value;

    const pPuesto = document.createElement('p');
    pPuesto.textContent = puestoInput.value;

    usuario.appendChild(pNombre);
    usuario.appendChild(pPuesto);
});
// FIN


// BOTON FILE SUBIR IMAGEN DE PERFIL
function usuarioImg() {
  var file = document.getElementById("subir").click();
}
// FIN


// Boton eliminar en perfil.html
function eliminar() {
  var x = document.getElementsByClassName("btn-eliminar");
  for( let i = 0; i < x.length; i++){
    if (x[i].style.display === "none") {
      x[i].style.display = "block";
    } else {
      x[i].style.display = "none";
    }
  }
}
// FIN

/* function Toggle1() {
  var x = document.getElementsByClassName("dropdown-contenido");
  if (x.style.display === "none") {
      x.style.display = "block";
    } else {
      x.style.display = "none";
    }
} */

//Buscador de perfil
document.addEventListener("DOMContentLoaded", function () {
  const searchForm = document.querySelector(".search-perfil");
  const searchInput = document.querySelector(".searchTerm-perfil");
  const cards = document.querySelectorAll(".card");

  searchForm.addEventListener("submit", function (event) {
      event.preventDefault(); // Evita el envío predeterminado del formulario

      const searchTerm = searchInput.value.toLowerCase();

      // Itera a través de las cartas y muestra u oculta según el término de búsqueda
      cards.forEach(function (card) {
          const nombre = card.getAttribute("data-nombre").toLowerCase();
          const ubicacion = card.getAttribute("data-ubicacion").toLowerCase();
          const talla = card.getAttribute("data-talla").toLowerCase();
          const condicion = card.getAttribute("data-condicion").toLowerCase();

          if (
              nombre.includes(searchTerm) ||
              ubicacion.includes(searchTerm) ||
              talla.includes(searchTerm) ||
              condicion.includes(searchTerm)
          ) {
              card.style.display = "block";
          } else {
              card.style.display = "none";
          }
      });
  });
});
// FIN