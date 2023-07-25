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

    const empleado = document.querySelector('.btn-superiores');

    const pNombre = document.createElement('p');
    pNombre.textContent = nombreInput.value;

    const pPuesto = document.createElement('p');
    pPuesto.textContent = puestoInput.value;

    empleado.appendChild(pNombre);
    empleado.appendChild(pPuesto);
});