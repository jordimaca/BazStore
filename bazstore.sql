-- phpMyAdmin SQL Dump
-- version 4.8.4
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 30-06-2023 a las 23:35:36
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
  `imagen` mediumblob NOT NULL,
  `precio` int(7) NOT NULL,
  `tipo` char(13) COLLATE utf8_spanish_ci NOT NULL,
  `talla` varchar(5) COLLATE utf8_spanish_ci NOT NULL,
  `ubicacion` char(80) COLLATE utf8_spanish_ci NOT NULL,
  `condicion` char(15) COLLATE utf8_spanish_ci NOT NULL,
  `descripcion` varchar(65) COLLATE utf8_spanish_ci NOT NULL,
  `genero` char(7) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

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
  `imagen` mediumblob NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id_usuario`, `nombre`, `email`, `celular`, `contraseña`, `imagen`) VALUES
(1, 'admin', 'admin@admin.com', '8098000000', 'admin', 0x3c73766720786d6c6e733d22687474703a2f2f7777772e77332e6f72672f323030302f737667222077696474683d22323422206865696768743d223234222076696577426f783d22302030203234203234223e3c7061746820643d224d3132203243362e3537392032203220362e353739203220313273342e3537392031302031302031302031302d342e3537392031302d31305331372e343231203220313220327a6d30203563312e3732372030203320312e32373220332033732d312e32373320332d332033632d312e37323620302d332d312e3237322d332d3373312e3237342d3320332d337a6d2d352e31303620392e373732632e3839372d312e333220322e3339332d322e3220342e3130362d322e32683263312e373134203020332e3230392e383820342e31303620322e324331352e3832382031382e31342031342e303135203139203132203139732d332e3832382d2e38362d352e3130362d322e3232387a222f3e3c2f7376673e);

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
