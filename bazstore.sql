-- phpMyAdmin SQL Dump
-- version 4.8.4
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 15-08-2023 a las 21:25:10
-- Versión del servidor: 10.1.37-MariaDB
-- Versión de PHP: 7.2.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
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
  `nombre_articulo` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  `imagen` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `precio` int(7) NOT NULL,
  `tipo` char(13) COLLATE utf8_spanish_ci NOT NULL,
  `talla` varchar(5) COLLATE utf8_spanish_ci NOT NULL,
  `ubicacion` char(80) COLLATE utf8_spanish_ci NOT NULL,
  `condicion` char(15) COLLATE utf8_spanish_ci NOT NULL,
  `descripcion` varchar(500) COLLATE utf8_spanish_ci NOT NULL,
  `genero` char(7) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `articulo`
--

INSERT INTO `articulo` (`id_articulo`, `id_usuario`, `nombre_articulo`, `imagen`, `precio`, `tipo`, `talla`, `ubicacion`, `condicion`, `descripcion`, `genero`) VALUES
(1, 1, 'articulo1', 'a4.jpg', 3213456, 'camisa', 'xxl', 'bna', 'nuevo-usado', 'wqiyugheygoi', 'hombre'),
(2, 1, 'reloj', '2023151441_reloj7.png', 3000, 'zapatos', 'm', 'rd', 'nuevo', 'gdgjhjkhjkshjkfnjgjfngjnbkbhgjknbgg', 'accesor'),
(3, 1, 'Correa-cinturon ', '2023151604_cinturon.jpg', 2000, 'jeans', 'xl', 'rd', 'usado', 'hewhkjksjfjkfjskjsm,ajshkajk', 'hombre'),
(4, 1, 'Reloj-Rolex-hombre', '2023151724_relojh1.jpg', 30000, 'tshirt', 'm', 'rd', 'nuevo', '32y48995850jhfnhkjgnvjkxfngklxgklxfmgbkflnbfklcnhkhjgfhkl', 'hombre'),
(5, 1, 'Zapatos-Dior-Hombre', '2023151851_zapatoh5.jpg', 10000, 'zapatos', '12', 'sd', 'nuevo', 'asdjkdjksfkdnklfsgmkldgklnhfgklhnklfghklhklgjklllllllllllllllllll', 'hombre'),
(6, 1, 'Camisa-Tommy hilfiger', '2023152057_camisa5.jpg', 5000, 'camisa', 'l', 'stgo', 'nuevo', 'fdgfhzdhvbjkhkjgklxjkglmkflhmlg', 'hombre'),
(7, 1, 'Brazalete-Pulsera-Hombre', '2023152242_b6.jpg', 1000, 'tshirt', 'xl', 'sd', 'nuevo', '34284293723095830946809487', 'hombre'),
(8, 1, 'Cadena-Collar-Hombre', '2023152344_collarm1.jpg', 500, 'tshirt', 'l', 'sd', 'nuevo', 'fsjkhskfjsklgjdlkhl;h;kjjfjhdhfth', 'hombre');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id_usuario` int(11) NOT NULL,
  `nombre` varchar(25) COLLATE utf8_spanish_ci NOT NULL,
  `email` varchar(320) COLLATE utf8_spanish_ci NOT NULL,
  `celular` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `contraseña` varchar(60) COLLATE utf8_spanish_ci NOT NULL,
  `imagen` varchar(255) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id_usuario`, `nombre`, `email`, `celular`, `contraseña`, `imagen`) VALUES
(1, 'admin', 'admin@admin.com', '8098000000', 'admin', '<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"24\" height=\"24\" viewBox=\"0 0 24 24\"><path d=\"M12 2C6.579 2 2 6.579 2 12s4.579 10 10 10 10-4.579 10-10S17.421 2 12 2zm0 5c1.727 0 3 1.272 3 3s-1.273 3-3 3c-1.726 0-3-1.272-3-3s1.274-3 3-3zm-5.106 9.772c.897-1.');

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
  MODIFY `id_articulo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

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
