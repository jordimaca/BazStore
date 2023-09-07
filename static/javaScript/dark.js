// MODO OSCURO ACTIVO
document.addEventListener("DOMContentLoaded", function() {
    var darkActivado = localStorage.getItem("darkMode") === "activado";

    var itemBody = document.body;
    itemBody.classList.toggle("dark-body", darkActivado);

    var itemPerfil = document.getElementsByClassName("perfil-contenedor");
    for (var i = 0; i < itemPerfil.length; i++) {
        itemPerfil[i].classList.toggle("dark-perfil-contenedor", darkActivado);
        }

    var itemTop = document.getElementsByClassName("topline");
    for (var i = 0; i < itemTop.length; i++) {
        itemTop[i].classList.toggle("dark-topline", darkActivado);
        }

    /* Menu */
    var itemMenu = document.getElementsByClassName("menu-contenedor");
    for (var i = 0; i < itemMenu.length; i++) {
        itemMenu[i].classList.toggle("dark-menu-contenedor", darkActivado);
        }
    var itemBtnMenu = document.getElementsByClassName("btn-menu");
    for (var i = 0; i < itemBtnMenu.length; i++) {
        itemBtnMenu[i].classList.toggle("btn-dark-menu", darkActivado);
        }
    var itemActive = document.getElementsByClassName("active");
    for (var i = 0; i < itemActive.length; i++) {
        itemActive[i].classList.toggle("dark-active", darkActivado);
        }
    var itemBtnCuenta = document.getElementsByClassName("btn-cuenta");
    for (var i = 0; i < itemBtnCuenta.length; i++) {
        itemBtnCuenta[i].classList.toggle("btn-dark-cuenta", darkActivado);
        }
    var itemBtnDark = document.getElementsByClassName("btn-dark");
    for (var i = 0; i < itemBtnDark.length; i++) {
        itemBtnDark[i].classList.toggle("btn-dark-dark", darkActivado);
        }
    var itemBtnContent = document.getElementsByClassName("btn-content");
    for (var i = 0; i < itemBtnContent.length; i++) {
        itemBtnContent[i].classList.toggle("btn-dark-content", darkActivado);
        }
    /* Menu FIN */

    /* Buscador */
    var searchTerm = document.getElementsByClassName("searchTerm");
    for (var i = 0; i < searchTerm.length; i++) {
        searchTerm[i].classList.toggle("dark-searchTerm", darkActivado);
        }
    var searchButton = document.getElementsByClassName("searchButton");
    for (var i = 0; i < searchButton.length; i++) {
        searchButton[i].classList.toggle("dark-searchButton", darkActivado);
        }
    /* Buscardo FIN */

    /* Buscador perfil */
    var searchTermPerfil = document.getElementsByClassName("searchTerm-perfil");
    for (var i = 0; i < searchTermPerfil.length; i++) {
        searchTermPerfil[i].classList.toggle("dark-searchTerm-perfil", darkActivado);
        }
    var searchButtonPerfil = document.getElementsByClassName("searchButton-perfil");
    for (var i = 0; i < searchButtonPerfil.length; i++) {
        searchButtonPerfil[i].classList.toggle("dark-searchButton-perfil", darkActivado);
        }
    /* Buscardo perfil FIN */

    /* Filtro */
    var itemFiltro = document.getElementsByClassName("contenedor-filtro");
    for (var i = 0; i < itemFiltro.length; i++) {
        itemFiltro[i].classList.toggle("dark-contenedor-filtro", darkActivado);
        }
    /* Filtro Fin */

    /* Perfil */
    var itemBtn = document.getElementsByClassName("btn");
    for (var i = 0; i < itemBtn.length; i++) {
        itemBtn[i].classList.toggle("dark-btn", darkActivado);
        }
    /* Perfil FIN */

    /* Modal */
    var itemConModal = document.getElementsByClassName("contenedor-modal");
    for (var i = 0; i < itemConModal.length; i++) {
        itemConModal[i].classList.toggle("dark-contenedor-modal", darkActivado);
        }
    /* Modal FIN */

    /* Card */
    var itemCard = document.getElementsByClassName("card");
    for (var i = 0; i < itemCard.length; i++) {
        itemCard[i].classList.toggle("dark-card", darkActivado);
        }
    
    var itemCardTitle = document.getElementsByClassName("card-title");
    for (var i = 0; i < itemCardTitle.length; i++) {
        itemCardTitle[i].classList.toggle("dark-card-title", darkActivado);
        }
    /* Card FIN */
    
    /* Articulo */
    var itemConTitle = document.getElementsByClassName("contenedor-titulo");
    for (var i = 0; i < itemConTitle.length; i++) {
        itemConTitle[i].classList.toggle("dark-contenedor-titulo", darkActivado);
        }
    var itemConInfo = document.getElementsByClassName("contenedor-informacion");
    for (var i = 0; i < itemConInfo.length; i++) {
        itemConInfo[i].classList.toggle("dark-contenedor-informacion", darkActivado);
        }
    var itemConDes = document.getElementsByClassName("contenedor-descripcion");
    for (var i = 0; i < itemConDes.length; i++) {
        itemConDes[i].classList.toggle("dark-contenedor-descripcion", darkActivado);
        }
    var itemConVend = document.getElementsByClassName("contenedor-vendedor");
    for (var i = 0; i < itemConVend.length; i++) {
        itemConVend[i].classList.toggle("dark-contenedor-vendedor", darkActivado);
        }
    /* Articulo FIN */

    /* Login */
    var itemContenedor = document.getElementsByClassName("contenedor-cuadrado");
    for (var i = 0; i < itemContenedor.length; i++) {
        itemContenedor[i].classList.toggle("dark-contenedor-cuadrado", darkActivado);
        }
    var itemBtnUp = document.getElementsByClassName("btn-up");
    for (var i = 0; i < itemBtnUp.length; i++) {
        itemBtnUp[i].classList.toggle("dark-btn-up", darkActivado);
        }
    var itemContenedorBtn = document.getElementsByClassName("contenedor-botones");
    for (var i = 0; i < itemContenedorBtn.length; i++) {
        itemContenedorBtn[i].classList.toggle("dark-contenedor-botones", darkActivado);
        }
    var itemRegisterForm = document.getElementsByClassName("register-form");
    for (var i = 0; i < itemRegisterForm.length; i++) {
        itemRegisterForm[i].classList.toggle("dark-register-form", darkActivado);
        }
    /* Login FIN */

    /* Footer */
    var itemFooter = document.getElementsByClassName("footer");
    for (var i = 0; i < itemFooter.length; i++) {
        itemFooter[i].classList.toggle("dark-footer", darkActivado);
        }
    /* Footer FIN */

    /* Boton dark */
    var itemSun = document.getElementsByClassName("sun");
    for (var i = 0; i < itemSun.length; i++) {
        itemSun[i].classList.toggle("sun-oculto", darkActivado);
        }
    var itemMoon = document.getElementsByClassName("moon-oculto");
    for (var i = 0; i < itemMoon.length; i++) {
        itemMoon[i].classList.toggle("fa-moon", darkActivado);
        }
    /* Boton dark FIN */

});


// MODO OSCURO INACTIVO
function dark() {

    var darkActivado = localStorage.getItem("darkMode") === "activado";

    var itemBody = document.body;
    itemBody.classList.toggle("dark-body", !darkActivado);

    var itemPerfil = document.getElementsByClassName("perfil-contenedor");
    for (var i = 0; i < itemPerfil.length; i++) {
        itemPerfil[i].classList.toggle("dark-perfil-contenedor", !darkActivado);
        }

    var itemTop = document.getElementsByClassName("topline");
    for (var i = 0; i < itemTop.length; i++) {
        itemTop[i].classList.toggle("dark-topline", !darkActivado);
        }

    /* Menu */
    var itemMenu = document.getElementsByClassName("menu-contenedor");
    for (var i = 0; i < itemMenu.length; i++) {
        itemMenu[i].classList.toggle("dark-menu-contenedor", !darkActivado);
        }
    var itemBtnMenu = document.getElementsByClassName("btn-menu");
    for (var i = 0; i < itemBtnMenu.length; i++) {
        itemBtnMenu[i].classList.toggle("btn-dark-menu", !darkActivado);
        }
    var itemActive = document.getElementsByClassName("active");
    for (var i = 0; i < itemActive.length; i++) {
        itemActive[i].classList.toggle("dark-active", !darkActivado);
        }
    var itemBtnCuenta = document.getElementsByClassName("btn-cuenta");
    for (var i = 0; i < itemBtnCuenta.length; i++) {
        itemBtnCuenta[i].classList.toggle("btn-dark-cuenta", !darkActivado);
        }
    var itemBtnDark = document.getElementsByClassName("btn-dark");
    for (var i = 0; i < itemBtnDark.length; i++) {
        itemBtnDark[i].classList.toggle("btn-dark-dark", !darkActivado);
        }
    var itemBtnContent = document.getElementsByClassName("btn-content");
    for (var i = 0; i < itemBtnContent.length; i++) {
        itemBtnContent[i].classList.toggle("btn-dark-content", !darkActivado);
        }
    /* Menu FIN */
    
    /* Buscador */
    var searchTerm = document.getElementsByClassName("searchTerm");
    for (var i = 0; i < searchTerm.length; i++) {
        searchTerm[i].classList.toggle("dark-searchTerm", !darkActivado);
        }
    var searchButton = document.getElementsByClassName("searchButton");
    for (var i = 0; i < searchButton.length; i++) {
        searchButton[i].classList.toggle("dark-searchButton", !darkActivado);
        }
    /* Buscardo FIN */

    /* Buscador perfil */
    var searchTermPerfil = document.getElementsByClassName("searchTerm-perfil");
    for (var i = 0; i < searchTermPerfil.length; i++) {
        searchTermPerfil[i].classList.toggle("dark-searchTerm-perfil", !darkActivado);
        }
    var searchButtonPerfil = document.getElementsByClassName("searchButton-perfil");
    for (var i = 0; i < searchButtonPerfil.length; i++) {
        searchButtonPerfil[i].classList.toggle("dark-searchButton-perfil", !darkActivado);
        }
    /* Buscardo perfil FIN */

    /* Filtro */
    var itemFiltro = document.getElementsByClassName("contenedor-filtro");
    for (var i = 0; i < itemFiltro.length; i++) {
        itemFiltro[i].classList.toggle("dark-contenedor-filtro", !darkActivado);
        }
    /* Filtro Fin */

    /* Perfil */
    var itemBtn = document.getElementsByClassName("btn");
    for (var i = 0; i < itemBtn.length; i++) {
        itemBtn[i].classList.toggle("dark-btn", !darkActivado);
        }
    /* Perfil FIN */
    
    /* Modal */
    var itemConModal = document.getElementsByClassName("contenedor-modal");
    for (var i = 0; i < itemConModal.length; i++) {
        itemConModal[i].classList.toggle("dark-contenedor-modal", !darkActivado);
        }
    /* Modal FIN */

    /* Card */
    var itemCard = document.getElementsByClassName("card");
    for (var i = 0; i < itemCard.length; i++) {
        itemCard[i].classList.toggle("dark-card", !darkActivado);
        }
    
    var itemCardTitle = document.getElementsByClassName("card-title");
    for (var i = 0; i < itemCardTitle.length; i++) {
        itemCardTitle[i].classList.toggle("dark-card-title", !darkActivado);
        }
    /* Card FIN */

    /* Articulo */ 
    var itemConTitle = document.getElementsByClassName("contenedor-titulo");
    for (var i = 0; i < itemConTitle.length; i++) {
        itemConTitle[i].classList.toggle("dark-contenedor-titulo", !darkActivado);
        }
    var itemConInfo = document.getElementsByClassName("contenedor-informacion");
    for (var i = 0; i < itemConInfo.length; i++) {
        itemConInfo[i].classList.toggle("dark-contenedor-informacion", !darkActivado);
        }
    var itemConDes = document.getElementsByClassName("contenedor-descripcion");
    for (var i = 0; i < itemConDes.length; i++) {
        itemConDes[i].classList.toggle("dark-contenedor-descripcion", !darkActivado);
        }
    var itemConVend = document.getElementsByClassName("contenedor-vendedor");
    for (var i = 0; i < itemConVend.length; i++) {
        itemConVend[i].classList.toggle("dark-contenedor-vendedor", !darkActivado);
        }
    /* Articulo FIN */

    /* Login */
    var itemContenedor = document.getElementsByClassName("contenedor-cuadrado");
    for (var i = 0; i < itemContenedor.length; i++) {
        itemContenedor[i].classList.toggle("dark-contenedor-cuadrado", !darkActivado);
        }
    var itemBtnUp = document.getElementsByClassName("btn-up");
    for (var i = 0; i < itemBtnUp.length; i++) {
        itemBtnUp[i].classList.toggle("dark-btn-up", !darkActivado);
        }
    var itemContenedorBtn = document.getElementsByClassName("contenedor-botones");
    for (var i = 0; i < itemContenedorBtn.length; i++) {
        itemContenedorBtn[i].classList.toggle("dark-contenedor-botones", !darkActivado);
        }
    var itemRegisterForm = document.getElementsByClassName("register-form");
    for (var i = 0; i < itemRegisterForm.length; i++) {
        itemRegisterForm[i].classList.toggle("dark-register-form", !darkActivado);
        }
    /* Login FIN */

    /* Footer */
    var itemFooter = document.getElementsByClassName("footer");
    for (var i = 0; i < itemFooter.length; i++) {
        itemFooter[i].classList.toggle("dark-footer", !darkActivado);
        }
    /* Footer FIN */
    
    /* Boton dark */
    var itemSun = document.getElementsByClassName("sun");
    for (var i = 0; i < itemSun.length; i++) {
        itemSun[i].classList.toggle("sun-oculto", !darkActivado);
        }
    var itemMoon = document.getElementsByClassName("moon-oculto");
    for (var i = 0; i < itemMoon.length; i++) {
        itemMoon[i].classList.toggle("fa-moon", !darkActivado);
        }
    /* Boton dark FIN */

    localStorage.setItem("darkMode", darkActivado ? "desactivado" : "activado");
}

/* var itemUbicacion = document.getElementById("ubicacion");
    itemUbicacion.toggle("dark-id");

    var itemTalla = document.getElementById("talla");
    itemTalla.classList.toggle("dark-id");

    var itemCondicion = document.getElementById("condicion");
    itemCondicion.classList.toggle("dark-id"); */
   