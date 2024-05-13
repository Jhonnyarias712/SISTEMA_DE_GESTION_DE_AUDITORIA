-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 12-05-2024 a las 22:43:21
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `sga`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `formulario`
--

CREATE TABLE `formulario` (
  `FK_ID_PLANTILLA` int(11) NOT NULL,
  `ACTIVIDAD` varchar(1200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `plantilla`
--

CREATE TABLE `plantilla` (
  `ID_PLANTILLA` int(11) NOT NULL,
  `NOMBRE_PLANTILLA` varchar(100) DEFAULT NULL,
  `TEMA` varchar(100) DEFAULT NULL,
  `OWNER` varchar(120) DEFAULT NULL,
  `DESCRIPTION` varchar(1000) DEFAULT NULL,
  `CREATED_DATE` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users`
--

CREATE TABLE `users` (
  `ID_USER` int(11) NOT NULL,
  `USER` varchar(50) NOT NULL,
  `PASSWORD` varchar(50) NOT NULL,
  `FULL_NAME` varchar(120) NOT NULL,
  `USER_TYPE` varchar(40) NOT NULL,
  `CREATED_DATE` datetime NOT NULL,
  `UPDATE_DATE` datetime DEFAULT NULL,
  `STATUS` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `users`
--

INSERT INTO `users` (`ID_USER`, `USER`, `PASSWORD`, `FULL_NAME`, `USER_TYPE`, `CREATED_DATE`, `UPDATE_DATE`, `STATUS`) VALUES
(1, 'JHONNY', 'JHONNY123', 'Jhonny Arias', 'ADMIN', '2024-05-11 00:00:00', '2024-05-11 00:00:00', 'A'),
(2, 'Jhonny', 'jhonny123', 'Jhonny Arias', 'AUDITOR', '2024-05-11 00:00:00', '2024-05-11 00:00:00', 'A');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `formulario`
--
ALTER TABLE `formulario`
  ADD PRIMARY KEY (`FK_ID_PLANTILLA`);

--
-- Indices de la tabla `plantilla`
--
ALTER TABLE `plantilla`
  ADD PRIMARY KEY (`ID_PLANTILLA`),
  ADD KEY `OWNER` (`OWNER`);

--
-- Indices de la tabla `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`ID_USER`),
  ADD KEY `FULL_NAME` (`FULL_NAME`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `formulario`
--
ALTER TABLE `formulario`
  MODIFY `FK_ID_PLANTILLA` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `plantilla`
--
ALTER TABLE `plantilla`
  MODIFY `ID_PLANTILLA` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `users`
--
ALTER TABLE `users`
  MODIFY `ID_USER` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `formulario`
--
ALTER TABLE `formulario`
  ADD CONSTRAINT `formulario_ibfk_1` FOREIGN KEY (`FK_ID_PLANTILLA`) REFERENCES `plantilla` (`ID_PLANTILLA`);

--
-- Filtros para la tabla `plantilla`
--
ALTER TABLE `plantilla`
  ADD CONSTRAINT `plantilla_ibfk_1` FOREIGN KEY (`OWNER`) REFERENCES `users` (`FULL_NAME`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
