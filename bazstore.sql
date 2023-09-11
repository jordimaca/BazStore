-- phpMyAdmin SQL Dump
-- version 4.8.4
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 11-09-2023 a las 23:37:51
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
  `talla` varchar(7) COLLATE utf8_spanish_ci NOT NULL,
  `ubicacion` char(80) COLLATE utf8_spanish_ci NOT NULL,
  `condicion` char(15) COLLATE utf8_spanish_ci NOT NULL,
  `descripcion` varchar(500) COLLATE utf8_spanish_ci NOT NULL,
  `genero` char(10) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `articulo`
--

INSERT INTO `articulo` (`id_articulo`, `id_usuario`, `nombre_articulo`, `imagen`, `precio`, `tipo`, `talla`, `ubicacion`, `condicion`, `descripcion`, `genero`) VALUES
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
(20, 2, 'T-shirt-Mujer blusa', '2023173746_7183a7ab6b0ae712afd8413238198a6c.jpg', 300, 'Blusa', 'S', 'Santiago', 'Usado', 'T-shirt de rayas de mujer mangas cortas básico.', 'Mujer'),
(22, 3, 'Short Corto Deportivo', '2023133950_2c2d9a314873a5973d95d362f8ebbb5a.jpg', 700, 'Deportivo', 'L', 'Santo Domingo', 'Nuevo', '', 'Mujer'),
(23, 3, 'Set Deportivo de mujer', '2023134050_7cc54c42343dd060cb2b9849c7b0b3e8.jpg', 900, 'Deportivo', 'S', 'Santiago', 'Usado', '', 'Mujer'),
(24, 3, 'Leggins largo ', '2023134149_09eb8f5d033aa435e48f2ca3923fbffe.jpg', 1300, 'Deportivo', 'S', 'Todo el pais', 'Nuevo', '', 'Mujer'),
(25, 3, 'Top Adidas Deportivo', '2023134303_3637f499b077e8b1c4fef76b51f149b7.jpg', 1500, 'Deportivo', 'L', 'Puerto Plata', 'Nuevo', '', 'Mujer'),
(26, 3, 'Top de tirantes deportivo', '2023134350_933abd792ffe26138427d0939acaa1e6.jpg', 600, 'Deportivo', 'S', 'Todo el pais', 'Nuevo', '', 'Mujer'),
(27, 3, 'Leggins ', '2023134420_5180748e1252c55671424b41c9cfd806.jpg', 2000, 'Deportivo', 'XL', 'Santo Domingo', 'Nuevo', '', 'Mujer'),
(28, 3, 'Top Adidas Deportivo', '2023134506_58045fe59693a367131288b71dde7cf8.jpg', 1600, 'Deportivo', 'S', 'Todo el pais', 'Nuevo', '', 'Mujer'),
(29, 3, 'Overoles Deportivos', '2023134614_2043a614aa12ac3bf9289e2495810cba.jpg', 1500, 'Deportivo', 'S', 'Todo el pais', 'Nuevo', '', 'Mujer'),
(30, 3, 'Leggins Deportivo Mujer', '2023134713_6250980db17acf2d9348f32d7810a95e.jpg', 1900, 'Deportivo', 'S', 'San Francisco', 'Nuevo', '', 'Mujer'),
(31, 3, 'Vestido Para Fiesta', '2023134844_2e482491f0c03228e900eef7e26e50cb.jpg', 4000, 'Vestido', 'XL', 'Todo el pais', 'Nuevo', '', 'Mujer'),
(32, 3, 'Vestido Negro Corto de mujer', '2023134920_6494c9150d485e496795d667a5843ec0.jpg', 3700, 'Vestido', 'S', 'Todo el pais', 'Nuevo', '', 'Mujer'),
(33, 3, 'Vestido Casual de mujer', '2023135000_c9f4018b43b6acc65f8f4318e2249f42.jpg', 3400, 'Vestido', 'XL', 'Puerto Plata', 'Nuevo', '', 'Mujer'),
(34, 3, 'Vestido Mangas Largas Corto de mujer', '2023135036_32d36790d2dfc15a2b14c6ec6cf755bc.jpg', 4300, 'Vestido', 'XL', 'Barahona', 'Nuevo', '', 'Mujer'),
(35, 3, 'Vestido Largo Casual', '2023135137_72b0dcc30abd0dda623ed97a4d36b726.jpg', 2550, 'Vestido', 'XS', 'Todo el pais', 'Usado', '', 'Mujer'),
(36, 3, 'Vestido Azul Largo Para Fiestas', '2023135219_2f6b076e6de9f42fe788e73d5e7cb5fd.jpg', 6000, 'Vestido', 'S', 'Puerto Plata', 'Nuevo', '', 'Mujer'),
(37, 3, 'Camisa Blanca', '2023135350_01ffdf865912bbc4f1a22de46cc5d3b2.jpg', 2999, 'Camisa', 'M', 'Todo el pais', 'Nuevo', '', 'Hombre'),
(38, 3, 'Camisa Mangas Cortas Hombre', '2023135458_d2c8265c117a0816672d5d2b8cd024ae.jpg', 3000, 'Camisa', 'L', 'Barahona', 'Nuevo', '', 'Hombre'),
(39, 3, 'Camisa Azul Mangas Cortas', '2023135626_ea4ef765dbc7520f1c0de69e2ad9c2a4.jpg', 3200, 'Camisa', 'L', 'Todo el pais', 'Usado', '', 'Hombre'),
(40, 3, 'T-shirt básico Hombre', '2023135722_4cbab58feea7a3a82a66f37d9f182a7b.jpg', 1000, 'T-shirt', 'XXL', 'Todo el pais', 'Usado', '', 'Hombre'),
(41, 3, 'T-shirt ', '2023135801_37f17769e427c88083c93f4d52f12020.jpg', 2400, 'T-shirt', 'M', 'Barahona', 'Nuevo', '', 'Hombre'),
(42, 3, 'T-shirt de hombre', '2023135833_5aa6245c325fdac58aaa30ed9e931582.jpg', 2000, 'T-shirt', 'XL', 'Todo el pais', 'Usado', '', 'Hombre'),
(44, 3, 'T-shirt Mangas Largas- Sueter', '2023140047_b779255f84b943bd250f8ceffa4f224a.jpg', 5000, 'T-shirt', 'XL', 'Todo el pais', 'Nuevo', '', 'Hombre'),
(46, 4, 'Short deportivo', '2023140614_334d3d4ac99a98dc1f803476ed61ccaf.jpg', 400, 'Deportivo', 'M', 'Santo Domingo', 'Usado', '', 'Hombre'),
(47, 4, 'T-shirt deportivo', '2023140702_3ad99e2d2d68c67c3004f1c8deddc33e.jpg', 1000, 'Deportivo', 'M', 'Santiago', 'Usado', '', 'Hombre'),
(48, 4, 'Sportswear Nike', '2023140841_44df8716ef0401b919712070a90eb342.jpg', 3000, 'Deportivo', 'XL', 'Todo el pais', 'Nuevo', '', 'Hombre'),
(49, 4, 'Set Deportivo de Hombre', '2023140930_8e0166b8e0a7af0e4ab2af635e3f2946.jpg', 5000, 'Deportivo', 'L', 'San Francisco', 'Nuevo', '', 'Hombre'),
(50, 4, 'T-shirt Deportivo', '2023141027_ff41e7d51286858f74aca79d8bb1d15e.jpg', 1400, 'Deportivo', 'M', 'Santiago', 'Usado', '', 'Hombre'),
(51, 4, 'Jeans cargo bolsillo', '2023141234_001a637e9197e576fba9e3b6d27a0cd1.jpg', 3000, 'Pantalon', 'L', 'Todo el pais', 'Nuevo', '', 'Hombre'),
(52, 4, 'Jean Azul Claro ', '2023141335_2595f49c4e8be9d4f09e2d2927892b0c.jpg', 3600, 'Pantalon', 'M', 'San Francisco', 'Nuevo', '', 'Hombre'),
(53, 4, 'Jean Negro de Hombre', '2023141403_36d58a5975226ba61cb094190b7ca6dd.jpg', 3000, 'Pantalon', 'S', 'Todo el pais', 'Nuevo', '', 'Hombre'),
(54, 4, 'Jean Hombre Azul', '2023141518_8336f2e4059b6e17c67753f9e97f23b8.jpg', 3400, 'Pantalon', 'S', 'Santiago', 'Nuevo', '', 'Hombre'),
(55, 4, 'pantalones Cargo de mezclilla para hombre', '2023141651_9b7d50a8741f0962b2ec58c27c2692f8.jpg', 1200, 'Pantalon', 'XS', 'Barahona', 'Usado', '', 'Hombre'),
(56, 4, 'Jean Negro de Hombre', '2023141747_97152b14dca6a17d97d4ddde72fed822.jpg', 1300, 'Pantalon', 'XS', 'Todo el pais', 'Usado', '', 'Hombre'),
(57, 4, 'Short Jean de mujer', '2023141916_46552b22b9390258f70cd9e196edc64c.jpg', 3000, 'Pantalon', 'M', 'San Francisco', 'Nuevo', '', 'Mujer'),
(58, 4, 'Jean Azul Claro de Mujer', '2023142021_74d7526d9f7926e2ba5eeb840aaba824.jpg', 4995, 'Pantalon', 'XXL', 'Santo Domingo', 'Nuevo', '', 'Mujer'),
(59, 4, 'Jean Negro de Mujer', '2023142104_11decdd5a5ce08a6de260f37404fe7b0.jpg', 2000, 'Pantalon', 'L', 'Barahona', 'Usado', '', 'Mujer'),
(60, 4, 'Jean Acampanado de Mujer', '2023142148_19cfdb372810240bb989bd2fecc7760b.jpg', 3570, 'Pantalon', 'XS', 'Santiago', 'Nuevo', '', 'Mujer'),
(61, 5, 'Nike Air Max 96', '2023142901_012d138b6cccef88c37e33b3b04168c9.jpg', 10000, 'Zapato', 'M', 'Todo el pais', 'Nuevo', '', 'Hombre'),
(62, 5, 'Zapatos de Hombre', '2023144024_676d07fee45580f1168729f56fa49317.jpg', 7800, 'Zapato', '10.5 H', 'Santo Domingo', 'Nuevo', '', 'Hombre'),
(63, 5, 'Adidas Yeezy Boost 350 V2 – Mono Ice', '2023144143_368571cca7d20996404da6f9222d474d.jpg', 6000, 'Zapato', '13 H', 'San Francisco', 'Usado', '', 'Hombre'),
(64, 5, 'Nike M2K Tekno W', '2023144310_5ec977a097f1dafffe00a5bbff3714de.jpg', 7000, 'Zapato', '8 H', 'Santiago', 'Usado', '', 'Hombre'),
(65, 5, 'Adidas Forum Low', '2023144639_d0cfe7a7882f8e68b34edf0b44c45822.jpg', 8000, 'Zapato', '11 H', 'San Francisco', 'Nuevo', '', 'Hombre'),
(66, 5, 'Women\'s Aveline 100 High Heel Sandals', '2023144827_4bd09c72cce33cabb9695ac71f43b0c7.jpg', 7000, 'Zapato', '7 M', 'Santiago', 'Nuevo', '', 'Mujer'),
(67, 5, 'Sandalias Negras de mujer', '2023144953_6d3064e253bf607ebfb392ed39ebf856.jpg', 700, 'Zapato', '5.5 M', 'Barahona', 'Usado', '', 'Mujer'),
(68, 5, 'New Balance 500 Uk', '2023145120_2377b322e9b9175e068766bbe1f3d6e5.jpg', 34500, 'Zapato', '8.5 M', 'Santo Domingo', 'Nuevo', '', 'Mujer'),
(70, 8, 'Cushion Cut Diamond Ring', '2023161737_098bd6ff25ed78efb97a5c8b9ac0ed43.jpg', 77000, 'Anillos', 'Todas l', 'Barahona', 'Usado', 'Anillo de compromiso, de Oro 14k con zirconias, ncluye gratis: Grabado, estuche, medidas, una limpieza y garantía en el metal.', 'Accesorio'),
(71, 8, 'LOVE WEDDING BAND', '2023162012_141e1017aa9c3af990eedec456437065.jpg', 83000, 'Anillos', 'Todas l', 'Todo el pais', 'Nuevo', 'Alianza Love, oro amarillo 750/1000. Ancho: 3,6 mm (para talla 52).\r\n\r\nTenga en cuenta que el peso en quilates, la cantidad de piedras y las dimensiones del producto variarán según el tamaño de la creación solicitada. Por favor contáctenos para más información.', 'Accesorio'),
(72, 8, 'Anillos de Acero Inoxidable', '2023162247_bc7771f6afe2406ccbdf05003fa7c563.jpg', 700, 'Anillos', 'Todas l', 'Santiago', 'Usado', 'Anillos de Acero Inoxidable en Oro 14K Sortija de Hombre Joyería Para Hombre. El anillo de sello negro clásico es la pieza perfecta para usar solo o en capas con otros anillos.', 'Accesorio'),
(73, 8, 'Anillos de circón cuadrados', '2023162458_dd3d96b89c26f5c89ec57d529ce7a2fc.jpg', 1000, 'Anillos', 'Todas l', 'Puerto Plata', 'Usado', 'Anillos de circón cuadrados de color negro, blanco, rosa, verde, para mujer, anillo de oro ancho de lujo.', 'Accesorio'),
(74, 8, 'Anillo grabado Anillo personalizado', '2023162814_e3a538e5596562cc1658c01fe4f80619.jpg', 24000, 'Anillos', 'Todas l', 'San Francisco', 'Nuevo', 'Año Fecha Número Anillo grabado Anillo personalizado Anillo inicial Regalo.', 'Accesorio'),
(75, 8, 'Anillo David Yurman Black Titanium', '2023162935_6864e897923855e8e1f4515af187deeb.jpg', 2000, 'Anillos', 'Todas l', 'Barahona', 'Usado', 'David Yurman Black Titanium & Sterling Silver Pave Roman Signet Ring with Sapphires - Blue/Black.', 'Accesorio'),
(77, 8, 'Reloj Rosefield para mujer', '2023163408_813291c81dfe15e2b820378161cf6379.jpg', 23000, 'Reloj', 'Todas l', 'Puerto Plata', 'Usado', '', 'Accesorio'),
(78, 8, 'Rolex – Datejust 41 – Oystersteel & White Gold – Jubilee – Black Dial', '2023163626_804dd844cc8955ea6e0a273a63cc9438.jpg', 19280, 'Reloj', 'Todas l', 'Todo el pais', 'Usado', 'El Oyster Perpetual Datejust de Rolex es un reloj clásico verdaderamente icónico. Creado en 1945, el Datejust fue el primer reloj de pulsera con cronómetro automático que mostraba la fecha en una ventana situada a las 3 en punto de la esfera, de ahí su nombre.', 'Accesorio'),
(79, 8, 'Rolex Datejust 31 278273 Silver Diamond Jubilee', '2023163851_8a43ab7765a4082d30245c6742ec84ab.jpg', 1077618, 'Reloj', 'Todas l', 'Todo el pais', 'Nuevo', 'El Oyster Perpetual Lady-Datejust de Rolex es un clásico entre los guardatiempos femeninos, una de esas joyas que trasciende épocas y modas. Lleva siéndolo desde su presentación en 1957, en un momento en el que las mujeres estaban cambiando.', 'Accesorio'),
(80, 8, 'Cartier Reloj Tank Louis Cartier', '2023164037_6d3ad6a35062533505e44a0389a3e024.jpg', 77000, 'Reloj', 'Todas l', 'Todo el pais', 'Nuevo', 'El nombre Cartier por sí solo es bien estimado, pero el gran respeto de la casa francesa se ve validado por la impresionante mano de obra de sus finos relojes. Fabricada en Suiza, esta edición \'Tank\' sigue el modelo del que usó el propio Sr. Louis Cartier y presenta asas redondeadas inspiradas en su aprecio por el estilo Art Déco. La caja de oro de 18 quilates alberga un preciso movimiento de cuarzo y complementa magníficamente la corona de zafiro y la correa de aligátor marrón.', 'Accesorio'),
(81, 8, 'Rolex Datejust', '2023164612_d8b2768b9a52ac8ee4cfd5d8681ee469.jpg', 1020901, 'Reloj', 'Todas l', 'San Francisco', 'Nuevo', 'La década de 1930 fue un período en el que los espectaculares avances en el rendimiento de las aeronaves ampliaron constantemente la capacidad de la humanidad para conquistar los cielos y llevaron a la introducción de vuelos de larga distancia. Varios pilotos establecieron récords con un Oyster. Otros utilizaron un reloj Rolex como cronómetro de a bordo.', 'Accesorio'),
(82, 8, 'RELOJES ROLEX LADY‑DATEJUST', '2023165017_a74f9e33feca8667044c01a6aa0a5890.jpg', 397017, 'Reloj', 'Todas l', 'Santo Domingo', 'Nuevo', 'Este Oyster Perpetual Lady‑Datejust en acero Oystersteel presenta una esfera rosa y un brazalete Oyster. Un reloj clásico para mujer». Así describen algunos a nuestro Oyster Perpetual Lady-Datejust. Y puede que tengan razón. Desde comienzos del siglo XX, Rolex ha diseñado y fabricado relojes adecuados para todas las muñecas femeninas, con el mismo estándar de excelencia que todos los modelos que han forjado su leyenda. Si «clásico» significa buscar siempre llegar a lo más alto.', 'Accesorio'),
(83, 8, 'Pulcera Luxury Famous Brand Jewelry Rose', '2023170908_ba2bfbf847ebebd99318dc70e858bb23.jpg', 3000, 'Brazaletes', 'Todas l', 'Santiago', 'Usado', 'Luxury Famous Brand Jewelry Rose Gold Stainless Steel Roman Numerals Bracelets Bangles Female Charm Bracelets For Women.', 'Accesorio'),
(84, 8, 'Brazalete de Hombre', '2023171006_132e9bfb03a663e2d01d944aed8ff001.jpg', 1000, 'Brazaletes', 'Todas l', 'San Francisco', 'Usado', '', 'Accesorio'),
(85, 8, 'PULSERAS PANTHÈRE DE CARTIER', '2023171254_4c2d76480462ed4f1746367569e08b4c.jpg', 28840, 'Brazaletes', 'Todas l', 'Todo el pais', 'Nuevo', 'La Panthère de Cartier, indomable y magnética, imprime su carácter y su fuerza en las pulseras de la Maison.', 'Accesorio'),
(86, 8, 'Estilo Clásico Color Sólido Acero Titanio Enchapado Brazalete', '2023171504_8924e222e058af1754a86ff17bc49bbf.jpg', 1500, 'Brazaletes', 'Todas l', 'Barahona', 'Usado', '', 'Accesorio'),
(87, 8, 'Pulseras de cuero Homme de cuero ', '2023171624_0b8f32892db6406e5d1157681b13247a.jpg', 1700, 'Brazaletes', 'Todas l', 'San Francisco', 'Usado', 'Pulseras de cuero Homme de cuero de puntada para hombres Joyería hecha a mano de acero inoxidable\r\n', 'Accesorio'),
(88, 8, 'Pulsera tennis clásica de 2-20 quilates oro blanco 14K', '2023171736_c96acc89b365c7f5ad79b3834c3f23d2.jpg', 6400, 'Brazaletes', 'Todas l', 'Santo Domingo', 'Nuevo', 'Pulsera tennis clásica de 2-20 quilates oro blanco 14K Colección Value, oro blanco, #4 74 TENNIS BRACELET K-L I1-I2 var 426', 'Accesorio'),
(89, 8, 'Collar moderno de doble capa chapado en oro de 18 quilates', '2023171900_98546b50937330f6749d6319288c3240.jpg', 1200, 'Cadenas', 'Todas l', 'Barahona', 'Usado', 'Collar moderno de doble capa chapado en oro de 18 quilates para mujer, colgante de ónix cuadrado negro, gargantilla de nácar, regalo de joyería de dama de honor para ella.\r\n', 'Accesorio'),
(90, 8, 'Collar de cruz de plata', '2023172005_cd230f1fc8a9b2263462e80e88d429f2.jpg', 2000, 'Cadenas', 'Todas l', 'Todo el pais', 'Nuevo', 'Alexandreasjewels Pequeño y delicado collar de cruz de plata de ley, regalo de bautismo, cinturón de confirmación, collar de regalo de primera comunión, 18 pulgadas, Metal.', 'Accesorio'),
(91, 8, 'Collar de cadena de acero', '2023172104_9031b22bd7646234e4fa771ceef6cab9.jpg', 1000, 'Cadenas', 'Todas l', 'Santo Domingo', 'Usado', 'FOSIR Collar de cadena de acero inoxidable chapado en oro de 18 quilates para hombres y mujeres, 0.098 in, 0.118 in, 0.157 in, 0.197.', 'Accesorio'),
(92, 8, '18K Gold Vermeil Figaro Link Chain Sterling Silver Mens', '2023172159_86312858c32b2444ab6934661634c9fa.jpg', 30000, 'Cadenas', 'Todas l', 'Barahona', 'Nuevo', '', 'Accesorio'),
(93, 2, 'Nike H86 Metal Swoosh Cap', '2023172420_3c475da1bd8f989182b950a13d4bbb61.jpg', 2500, 'Otros', 'Todas l', 'Santiago', 'Usado', 'En estos momentos Nike Gorra H86 Metal Swoosh está al mejor precio y es perfecta para tus actividades. En traininn puedes encontrar otros productos que se complementan con nuestro catálogo de Ropa infantil y especialmente con nuestra categoría de Gorros. Disponemos de una variedad de Headwear que se adaptan a tus necesidades y te inspiran a hacer más deporte en tu rutina diaria.', 'Accesorio'),
(94, 2, 'Bolso de mano para fiesta', '2023172514_72af120154f77d3d97aa761bfd2e8081.jpg', 1000, 'Otros', 'Todas l', 'Todo el pais', 'Usado', 'Bolso de mano para fiesta de noche para mujer con cuero único y elegante bolso femenino bolso de mano para fiesta de boda ', 'Accesorio'),
(95, 2, 'Cinturon Buckle Reversible Belt, 32Mm', '2023172712_078c50624ee63fc1140effc62a438486.jpg', 7800, 'Otros', 'Todas l', 'Santo Domingo', 'Nuevo', 'Este cinturón está confeccionado con piel suave curtida y reverso con piel granulada texturizada para crear dos estilos en uno. Está acabado con nuestra hebilla distintiva para darle un estilo tradicional.', 'Accesorio'),
(96, 2, 'Monedero  plegable de piel sintética para hombre', '2023172808_87a5cee332d593b66b316fb33df846d0.jpg', 5000, 'Otros', 'Todas l', 'Todo el pais', 'Nuevo', '', 'Accesorio'),
(97, 2, 'Cartera Women\'s Black Velvet Pattina Bag With Gold Chain', '2023173012_679cebe873fd0b8992193e25921c473c.jpg', 70000, 'Otros', 'Todas l', 'Todo el pais', 'Nuevo', 'La última vez que compartimos el bolso Prada Velvet Tote, recibimos excelentes respuestas. Así que hoy nos encontramos con la versión Shoulder Bag y solo necesitábamos compartirla.\r\n\r\nLos estilos minimalistas siempre son bienvenidos, combinan más fácilmente con tu atuendo y te ahorran tiempo pensando qué pieza es mejor.\r\n\r\nPero lo minimalista es una cosa y lo bello es otra. Podemos decir que este bolso bandolera es precioso al igual que el material. ', 'Accesorio'),
(98, 2, 'Cinturón Para mujer ', '2023173105_78e26146456e356947e84742d2e89a8c.jpg', 3000, 'Otros', 'Todas l', 'Barahona', 'Nuevo', '', 'Accesorio'),
(99, 2, 'Hombres Gorra de béisbol con bordado de letra', '2023173214_f478c30a54f99c4ccbaa1bfda9795666.jpg', 500, 'Otros', 'Todas l', 'Santiago', 'Usado', '', 'Accesorio'),
(100, 2, 'Cartera MILAN BAG', '2023173516_b6ca8d0e05a67d1f68ad0a65e979dc74.jpg', 150000, 'Otros', 'Todas l', 'Todo el pais', 'Nuevo', 'HERMES KELLY 28 SELLIER CRAIE EPSOM GOLD HARDWARE.', 'Accesorio'),
(101, 2, 'Dior Bolso Saddle Soft Dior', '2023173644_378bbd3694e1455ae276a3a9e23da50a.jpg', 23000, 'Otros', 'Todas l', 'Todo el pais', 'Usado', 'Dior Bolso Saddle Soft Dior Oblique en Jacquard Beige y Negro - Hombre.', 'Accesorio');

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
(2, 'Boni Boni', 'boni@gmail.com', '8207946309', '12345678', '2023132906_fba75b00afed4a9f8bd2512aced5cfba.jpg'),
(3, 'Tryless', 'tryless@gmail.com', '8298456908', '12345678', '2023133810_8f3ed90386f52f519fd4587c06982757.jpg'),
(4, 'SarahClothes', 'sarahclothes@gmail.com', '8298352105', '12345678', '2023140403_c848a192e2e0880f6adf3224ddcba6bf.jpg'),
(5, 'La Casa Del Zapato', 'lacasadelzapato@gmail.com', '8296782334', '12345678', '2023142628_df1bcc26c2378a5611591b7f12349e84.jpg'),
(6, 'jordi', 'jordi@gmail.com', '1918210930', '12345678', 'user-icon.svg'),
(7, 'Jolmav', 'alcaberry@gmail.com', '8093031701', '12345678', 'user-icon.svg'),
(8, 'Encantos', 'encantos@gmal.com', '8298716807', '12345678', '2023155644_1eff8f34b96b5121806da84cccd57b12.jpg');

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
  MODIFY `id_articulo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=102;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

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
