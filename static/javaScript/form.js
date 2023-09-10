// Funcion de tipo y subtipo
var tipoSelect = document.getElementById("tipo");
var subtipoSelect = document.getElementById("subtipo");
var tallaSelect = document.getElementById("talla");
var tallaZapatoHSelect = document.getElementById("talla-zapatoH");
var tallaZapatoMSelect = document.getElementById("talla-zapatoM");

var subtipoOptions = subtipoSelect.querySelectorAll("option");
var subtipoOriginalHTML = subtipoSelect.innerHTML;

// Mantener un registro del estado original del campo de Talla
var tallaOriginalHTML = tallaSelect.innerHTML;
var tallaZapatoHOriginalHTML = tallaZapatoHSelect.innerHTML;
var tallaZapatoMOriginalHTML = tallaZapatoMSelect.innerHTML;

// Inicialmente, ocultar los campos de tallas de zapatos
tallaZapatoHSelect.style.display = "none";
tallaZapatoMSelect.style.display = "none";

// Función para deshabilitar y seleccionar una opción en un elemento select
function disableAndSelectOption(selectElement, value) {
    selectElement.innerHTML = `<option value="${value}" selected>${value}</option>`;
    selectElement.disabled = true;
}

tipoSelect.addEventListener("change", function() {
    var tipoSeleccionado = tipoSelect.value;

    if (tipoSeleccionado === "sin-seleccionar") {
        // Si el tipo es "Sin seleccionar", ocultar y deshabilitar las tallas de zapatos
        tallaZapatoHSelect.style.display = "none";
        tallaZapatoMSelect.style.display = "none";
        disableAndSelectOption(tallaZapatoHSelect, "Sin seleccionar");
        disableAndSelectOption(tallaZapatoMSelect, "Sin seleccionar");
        return; // No se hace más procesamiento
    }

    subtipoSelect.innerHTML = subtipoOriginalHTML;
    subtipoOptions = subtipoSelect.querySelectorAll("option");

    subtipoOptions.forEach(function(option) {
        if (option.value !== "sin-seleccionar") {
            if (
                (tipoSeleccionado === "Hombre" && (option.value === "T-shirt" || option.value === "Camisa" || option.value === "Pantalon" || option.value === "Zapato" || option.value === "Deportivo")) ||
                (tipoSeleccionado === "Mujer" && (option.value === "Vestido" || option.value === "Blusa" || option.value === "Pantalon" || option.value === "Zapato" || option.value === "Deportivo"))
            ) {
                option.style.display = "block";
            } else if (tipoSeleccionado === "Accesorio" && (option.value === "Reloj" || option.value === "Cadenas" || option.value === "Brazaletes" || option.value === "Anillos" || option.value === "Otros")) {
                option.style.display = "block";
            } else {
                option.style.display = "none";
            }
        }
    });

    // Configurar el campo de Talla según el tipo seleccionado
    if (tipoSeleccionado === "Accesorio") {
        disableAndSelectOption(tallaSelect, "Todas las tallas");
        tallaZapatoHSelect.style.display = "none";
        tallaZapatoMSelect.style.display = "none";
    } else {
        tallaSelect.innerHTML = tallaOriginalHTML;
        tallaSelect.value = "sin-seleccionar";
        tallaSelect.disabled = false;
        tallaZapatoHSelect.innerHTML = tallaZapatoHOriginalHTML;
        tallaZapatoMSelect.innerHTML = tallaZapatoMOriginalHTML;
        tallaZapatoHSelect.style.display = "none";
        tallaZapatoMSelect.style.display = "none";
    }

    // Ocultar "Todas las tallas" cuando se selecciona "Hombre" o "Mujer"
    if (tipoSeleccionado === "Hombre" || tipoSeleccionado === "Mujer") {
        var todasLasTallasOption = tallaSelect.querySelector("option[value='Todas las tallas']");
        if (todasLasTallasOption) {
            todasLasTallasOption.style.display = "none";
        }
    } else {
        var todasLasTallasOption = tallaSelect.querySelector("option[value='Todas las tallas']");
        if (todasLasTallasOption) {
            todasLasTallasOption.style.display = "block";
        }
    }
});

subtipoSelect.addEventListener("change", function() {
    var subtipoSeleccionado = subtipoSelect.value;
    var tipoSeleccionado = tipoSelect.value;

    if (subtipoSeleccionado === "sin-seleccionar") {
        // Si el subtipo es "Sin seleccionar", ocultar y deshabilitar las tallas de zapatos
        tallaZapatoHSelect.style.display = "none";
        tallaZapatoMSelect.style.display = "none";
        disableAndSelectOption(tallaZapatoHSelect, "Sin seleccionar");
        disableAndSelectOption(tallaZapatoMSelect, "Sin seleccionar");
        return; // No se hace más procesamiento
    }

    // Si se selecciona el subtipo Zapatos y el tipo es Mujer, muestra talla-zapatoM y oculta las otras opciones.
    if (subtipoSeleccionado === "Zapatos" && tipoSeleccionado === "Mujer") {
        tallaSelect.style.display = "none";
        tallaZapatoHSelect.style.display = "none";
        tallaZapatoMSelect.style.display = "block";
    }
    // Si se selecciona el subtipo Zapatos y el tipo es Hombre, muestra talla-zapatoH y oculta las otras opciones.
    else if (subtipoSeleccionado === "Zapatos" && tipoSeleccionado === "Hombre") {
        tallaSelect.style.display = "none";
        tallaZapatoMSelect.style.display = "none";
        tallaZapatoHSelect.style.display = "block";
    }
    // En otros casos, muestra las tallas estándar y oculta las de zapatos.
    else {
        tallaSelect.style.display = "block";
        tallaZapatoMSelect.style.display = "none";
        tallaZapatoHSelect.style.display = "none";
    }

    // Habilitar el campo de Talla
    tallaSelect.disabled = false;
});

// Función para deshabilitar y seleccionar una opción en un elemento select
function disableAndSelectOption(selectElement, value) {
    selectElement.innerHTML = `<option value="${value}" selected>${value}</option>`;
    selectElement.disabled = true;
}