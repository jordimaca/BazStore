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
  var file = document.getElementById("subirUsuario").click();
}
function submitForm() {
  var formulario = document.getElementById("form");
  formulario.submit();
}
// FIN

// BOTON FILE SUBIR IMAGEN DE ARTICULO
function articuloImg() {
  var fileInput = document.getElementById("subirArticulo");
  var boton = document.getElementById("botonSubir");

  // Verifica si se ha seleccionado un archivo
  if (fileInput.files.length > 0) {
    boton.classList.remove("boton-rojo");
    boton.classList.add("boton-verde");
  } else {
    boton.classList.remove("boton-verde");
    boton.classList.add("boton-rojo");
  }

  // Abre el cuadro de diálogo de selección de archivo
  fileInput.click();
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