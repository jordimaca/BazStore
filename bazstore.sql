-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 10-09-2023 a las 06:07:04
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bazstore`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `articulo`
--

CREATE TABLE `articulo` (
  `id_articulo` int(11) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `nombre_articulo` varchar(100) NOT NULL,
  `imagen` varchar(255) NOT NULL,
  `precio` int(7) NOT NULL,
  `tipo` char(13) NOT NULL,
  `talla` varchar(5) NOT NULL,
  `ubicacion` char(80) NOT NULL,
  `condicion` char(15) NOT NULL,
  `descripcion` varchar(500) NOT NULL,
  `genero` char(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `articulo`
--

INSERT INTO `articulo` (`id_articulo`, `id_usuario`, `nombre_articulo`, `imagen`, `precio`, `tipo`, `talla`, `ubicacion`, `condicion`, `descripcion`, `genero`) VALUES
(2, 1, 'reloj', '2023151441_reloj7.png', 3000, 'zapatos', 'm', 'rd', 'nuevo', 'gdgjhjkhjkshjkfnjgjfngjnbkbhgjknbgg', 'accesor'),
(3, 1, 'Correa-cinturon ', '2023151604_cinturon.jpg', 2000, 'jeans', 'xl', 'rd', 'usado', 'hewhkjksjfjkfjskjsm,ajshkajk', 'hombre'),
(6, 1, 'Camisa-Tommy hilfiger', '2023152057_camisa5.jpg', 5000, 'camisa', 'l', 'stgo', 'nuevo', 'fdgfhzdhvbjkhkjgklxjkglmkflhmlg', 'hombre'),
(7, 1, 'Brazalete-Pulsera-Hombre', '2023152242_b6.jpg', 1000, 'tshirt', 'xl', 'sd', 'nuevo', '34284293723095830946809487', 'hombre'),
(8, 1, 'Cadena-Collar-Hombre', '2023152344_collarm1.jpg', 500, 'tshirt', 'l', 'sd', 'nuevo', 'fsjkhskfjsklgjdlkhl;h;kjjfjhdhfth', 'hombre'),
(9, 2, 'Blusa-Sueter', '2023170218_5b95725feecd19535877d35714443a1e.jpg', 800, 'Blusa', 'M', 'Todo el pais', 'Nuevo', 'Sueter de rallas negras con mangas cortas.', 'Mujer'),
(10, 2, 'Camisa-Mujer-Corta', '2023170737_33fc12c1fb151cedfcdb79a754d28dd2.jpg', 1500, 'Blusa', 'S', 'Santiago', 'Nuevo', 'Camisa corta de lino color beige ', 'Mujer'),
(11, 2, 'Blusa-Seda-Mujer', '2023172057_250c2fc8916d7f656eec5b8216b83e9e.jpg', 2000, 'Blusa', 'L', 'Todo el pais', 'Nuevo', 'Blusa blanca de ceda, hombros caídos. ', 'Mujer'),
(12, 2, 'Blusa-Camisa ', '2023172236_d1c7f6764cab65c40f925a63d94e733c.jpg', 1000, 'Blusa', 'XL', 'Puerto Plata', 'Nuevo', 'Camisa azul corta de rayas.', 'Mujer'),
(13, 2, 'Blusa-Tshirt', '2023172638_f93f447df322aaea67468e07e4de3833.jpg', 500, 'Blusa', 'XXL', 'Todo el pais', 'Usado', 'T-shirt corto de mujer, gris.', 'Mujer'),
(14, 2, 'T-shirt', '2023172750_87571385e4d0a6a98f522ccda822b9f2.jpg', 500, 'Blusa', 'M', 'Todo el pais', 'Usado', 'T-shirt de mujer básico, color crema, mangas cortas.  ', 'Mujer'),
(15, 2, 'T-shirt', '2023172858_0ea2eea1574553a61bef12bf53169605.jpg', 400, 'Blusa', 'XXL', 'Puerto Plata', 'Nuevo', 'T-shirt básico de mujer , color gris, mangas cortas.', 'Mujer'),
(16, 2, 'Blusa-Mujer', '2023173114_ea907eb5c8a9db2825f61af93e87ad83.jpg', 2500, 'Blusa', 'M', 'Todo el pais', 'Nuevo', 'Blusa blanca mujer, mangas largas. ', 'Mujer'),
(17, 2, 'Blusa-Camisa', '2023173224_d2f5e5c6db89c996a5133f9c2d25ae83.jpg', 1900, 'Blusa', 'XS', 'Santo Domingo', 'Usado', 'Camisa corta mujer, Nilo con botones', 'Mujer'),
(18, 2, 'Blusa-Blanca mujer', '2023173429_fcee23b7acc4b9aac7d13ab78be932f7.jpg', 750, 'Blusa', 'L', 'San Francisco', 'Nuevo', 'Blusa blanca de mujer, diseño fruncido, manga al costado.', 'Mujer'),
(19, 2, 'Blusa', '2023173610_923005f8b2e75e436c201db39d2666df.jpg', 600, 'Blusa', 'XXL', 'Todo el pais', 'Usado', 'Blusa crema de mujer mangas cortas', 'Mujer'),
(20, 2, 'T-shirt-Mujer blusa', '2023173746_7183a7ab6b0ae712afd8413238198a6c.jpg', 300, 'Blusa', 'S', 'Santiago', 'Usado', 'T-shirt de rayas de mujer mangas cortas básico.', 'Mujer');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id_usuario` int(11) NOT NULL,
  `nombre` varchar(25) NOT NULL,
  `email` varchar(320) NOT NULL,
  `celular` varchar(10) NOT NULL,
  `contraseña` varchar(60) NOT NULL,
  `imagen` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id_usuario`, `nombre`, `email`, `celular`, `contraseña`, `imagen`) VALUES
(1, 'admin', 'admin@admin.com', '8098000000', 'admin', 'user-icon.svg'),
(2, 'Boni Boni', 'boni@gmail.com', '8207946309', '12345678', 'static\\images\\user-icon.svg');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `articulo`
--
ALTER TABLE `articulo`
  ADD PRIMARY KEY (`id_articulo`),
  ADD KEY `id_usuario` (`id_usuario`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id_usuario`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `articulo`
--
ALTER TABLE `articulo`
  MODIFY `id_articulo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `articulo`
--
ALTER TABLE `articulo`
  ADD CONSTRAINT `articulo_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
