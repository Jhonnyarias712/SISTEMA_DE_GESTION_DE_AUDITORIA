-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 20-05-2024 a las 05:31:31
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
-- Estructura de tabla para la tabla `agendaauditorias`
--

CREATE TABLE `agendaauditorias` (
  `id_agenda` int(11) NOT NULL,
  `nombre_entidad` varchar(255) DEFAULT NULL,
  `tipo_entidad` varchar(100) DEFAULT NULL,
  `sector_industria` varchar(100) DEFAULT NULL,
  `direccion` varchar(255) DEFAULT NULL,
  `contacto_entidad_email` varchar(255) DEFAULT NULL,
  `fecha_inicio` datetime DEFAULT NULL,
  `fecha_fin` datetime DEFAULT NULL,
  `duracion_dia` int(11) DEFAULT NULL,
  `area_departamento` varchar(255) DEFAULT NULL,
  `auditor` varchar(120) DEFAULT NULL,
  `fk_plantilla_id` int(11) DEFAULT NULL,
  `objetivo` varchar(1000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auditoria`
--

CREATE TABLE `auditoria` (
  `id_auditar` int(11) NOT NULL,
  `agenda_auditorias_id` int(11) DEFAULT NULL,
  `fecha_inicio_auditoria` datetime DEFAULT NULL,
  `fecha_fin_auditoria` datetime DEFAULT NULL,
  `fecha_inicio_plazo` datetime DEFAULT NULL,
  `estado_auditoria` varchar(10) DEFAULT NULL,
  `observacion` text DEFAULT NULL,
  `fecha_fin_plazo` datetime DEFAULT NULL,
  `fecha_cierre_auditoria` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `evaluacionactividad`
--

CREATE TABLE `evaluacionactividad` (
  `id` int(11) NOT NULL,
  `id_actividad` int(11) DEFAULT NULL,
  `auditoria_id` int(11) DEFAULT NULL,
  `respuesta` varchar(10) DEFAULT NULL,
  `observaciones` varchar(1000) DEFAULT NULL,
  `plazo_ini_observacion` datetime DEFAULT NULL,
  `plazo_fin_observacion` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `formulario`
--

CREATE TABLE `formulario` (
  `id_actividad` int(11) NOT NULL,
  `FK_ID_PLANTILLA` int(11) DEFAULT NULL,
  `ACTIVIDAD` varchar(1200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `formulario`
--

INSERT INTO `formulario` (`id_actividad`, `FK_ID_PLANTILLA`, `ACTIVIDAD`) VALUES
(1, 1, '- ¿La empresa tiene políticas y procedimientos claros para garantizar la integridad financiera?'),
(2, 1, '- ¿Están documentadas y comunicadas estas políticas y procedimientos a todo el personal relevante?');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `historialauditoria`
--

CREATE TABLE `historialauditoria` (
  `id_historial` int(11) NOT NULL,
  `auditoria_id` int(11) DEFAULT NULL,
  `fecha_inicio_auditoria` datetime DEFAULT NULL,
  `fecha_fin_auditoria` datetime DEFAULT NULL,
  `estado_auditoria` enum('APROBADA','REPROBADA','PENDIENTE','CANCELADA') DEFAULT NULL,
  `observaciones` text DEFAULT NULL,
  `auditor_id` int(11) DEFAULT NULL,
  `fk_plantilla_id` int(11) DEFAULT NULL,
  `documentos_adjuntos` varchar(255) DEFAULT NULL,
  `fecha_creacion` datetime DEFAULT NULL,
  `fecha_actualizacion` datetime DEFAULT NULL
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

--
-- Volcado de datos para la tabla `plantilla`
--

INSERT INTO `plantilla` (`ID_PLANTILLA`, `NOMBRE_PLANTILLA`, `TEMA`, `OWNER`, `DESCRIPTION`, `CREATED_DATE`) VALUES
(1, 'Control_Interno_Financiero', 'Auditoría de Control Interno Financiero', 'Jhonny Arias', 'La \"Auditoría de Control Interno Financiero\" es un proceso para evaluar la efectividad de los controles internos de una empresa en la protección de sus activos financieros y la precisión de su información contable. Se revisan políticas, procedimientos y prácticas financieras para identificar fortalezas y áreas de mejora.', '2024-05-12 15:47:48');

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
-- Indices de la tabla `agendaauditorias`
--
ALTER TABLE `agendaauditorias`
  ADD PRIMARY KEY (`id_agenda`),
  ADD KEY `auditor` (`auditor`),
  ADD KEY `fk_plantilla_id` (`fk_plantilla_id`);

--
-- Indices de la tabla `auditoria`
--
ALTER TABLE `auditoria`
  ADD PRIMARY KEY (`id_auditar`),
  ADD KEY `agenda_auditorias_id` (`agenda_auditorias_id`);

--
-- Indices de la tabla `evaluacionactividad`
--
ALTER TABLE `evaluacionactividad`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_actividad` (`id_actividad`),
  ADD KEY `auditoria_id` (`auditoria_id`);

--
-- Indices de la tabla `formulario`
--
ALTER TABLE `formulario`
  ADD PRIMARY KEY (`id_actividad`),
  ADD KEY `FK_ID_PLANTILLA` (`FK_ID_PLANTILLA`),
  ADD KEY `ACTIVIDAD` (`ACTIVIDAD`(768));

--
-- Indices de la tabla `historialauditoria`
--
ALTER TABLE `historialauditoria`
  ADD PRIMARY KEY (`id_historial`),
  ADD KEY `auditoria_id` (`auditoria_id`),
  ADD KEY `auditor_id` (`auditor_id`),
  ADD KEY `fk_plantilla_id` (`fk_plantilla_id`);

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
-- AUTO_INCREMENT de la tabla `agendaauditorias`
--
ALTER TABLE `agendaauditorias`
  MODIFY `id_agenda` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auditoria`
--
ALTER TABLE `auditoria`
  MODIFY `id_auditar` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `evaluacionactividad`
--
ALTER TABLE `evaluacionactividad`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `formulario`
--
ALTER TABLE `formulario`
  MODIFY `id_actividad` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `historialauditoria`
--
ALTER TABLE `historialauditoria`
  MODIFY `id_historial` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `plantilla`
--
ALTER TABLE `plantilla`
  MODIFY `ID_PLANTILLA` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `users`
--
ALTER TABLE `users`
  MODIFY `ID_USER` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `agendaauditorias`
--
ALTER TABLE `agendaauditorias`
  ADD CONSTRAINT `agendaauditorias_ibfk_1` FOREIGN KEY (`auditor`) REFERENCES `users` (`FULL_NAME`),
  ADD CONSTRAINT `agendaauditorias_ibfk_2` FOREIGN KEY (`fk_plantilla_id`) REFERENCES `plantilla` (`ID_PLANTILLA`);

--
-- Filtros para la tabla `auditoria`
--
ALTER TABLE `auditoria`
  ADD CONSTRAINT `auditoria_ibfk_1` FOREIGN KEY (`agenda_auditorias_id`) REFERENCES `agendaauditorias` (`id_agenda`);

--
-- Filtros para la tabla `evaluacionactividad`
--
ALTER TABLE `evaluacionactividad`
  ADD CONSTRAINT `evaluacionactividad_ibfk_1` FOREIGN KEY (`id_actividad`) REFERENCES `formulario` (`id_actividad`),
  ADD CONSTRAINT `evaluacionactividad_ibfk_2` FOREIGN KEY (`auditoria_id`) REFERENCES `auditoria` (`id_auditar`);

--
-- Filtros para la tabla `formulario`
--
ALTER TABLE `formulario`
  ADD CONSTRAINT `formulario_ibfk_1` FOREIGN KEY (`FK_ID_PLANTILLA`) REFERENCES `plantilla` (`ID_PLANTILLA`);

--
-- Filtros para la tabla `historialauditoria`
--
ALTER TABLE `historialauditoria`
  ADD CONSTRAINT `historialauditoria_ibfk_1` FOREIGN KEY (`auditoria_id`) REFERENCES `auditoria` (`id_auditar`) ON DELETE CASCADE,
  ADD CONSTRAINT `historialauditoria_ibfk_2` FOREIGN KEY (`auditor_id`) REFERENCES `users` (`ID_USER`) ON DELETE CASCADE,
  ADD CONSTRAINT `historialauditoria_ibfk_3` FOREIGN KEY (`fk_plantilla_id`) REFERENCES `plantilla` (`ID_PLANTILLA`) ON DELETE CASCADE;

--
-- Filtros para la tabla `plantilla`
--
ALTER TABLE `plantilla`
  ADD CONSTRAINT `plantilla_ibfk_1` FOREIGN KEY (`OWNER`) REFERENCES `users` (`FULL_NAME`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
