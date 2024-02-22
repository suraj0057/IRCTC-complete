-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 22, 2024 at 03:21 AM
-- Server version: 10.4.6-MariaDB
-- PHP Version: 7.1.32

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `rail_ticket_application`
--

-- --------------------------------------------------------

--
-- Table structure for table `rail_ticket_application_train`
--

CREATE TABLE `rail_ticket_application_train` (
  `id` bigint(20) NOT NULL,
  `trainNo` bigint(20) NOT NULL,
  `trainName` varchar(100) NOT NULL,
  `source` varchar(100) NOT NULL,
  `destination` varchar(100) NOT NULL,
  `arrivalTime` time(6) NOT NULL,
  `departureTime` time(6) NOT NULL,
  `sleeperAvailable` bigint(20) NOT NULL,
  `sleeperWaiting` bigint(20) NOT NULL,
  `acAvailable` bigint(20) NOT NULL,
  `acWaiting` bigint(20) NOT NULL,
  `sleeperPrice` bigint(20) NOT NULL,
  `acPrice` bigint(20) NOT NULL,
  `journeyDate` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `rail_ticket_application_train`
--

INSERT INTO `rail_ticket_application_train` (`id`, `trainNo`, `trainName`, `source`, `destination`, `arrivalTime`, `departureTime`, `sleeperAvailable`, `sleeperWaiting`, `acAvailable`, `acWaiting`, `sleeperPrice`, `acPrice`, `journeyDate`) VALUES
(2, 11040, 'Maharashtra express', 'pune', 'pachora', '20:20:00.000000', '20:50:00.000000', 0, 10, 0, 2, 550, 250, '2024-02-22'),
(3, 11040, 'Maharashtra express', 'pune', 'pachora', '20:20:00.000000', '20:50:00.000000', 0, 10, 3, 0, 550, 250, '2024-02-23'),
(4, 11040, 'Maharashtra express', 'pune', 'pachora', '20:20:00.000000', '20:50:00.000000', 0, 10, 3, 0, 550, 250, '2024-02-24'),
(5, 11040, 'Maharashtra express', 'pune', 'pachora', '20:20:00.000000', '20:50:00.000000', 0, 10, 3, 0, 550, 250, '2024-02-25'),
(6, 11040, 'Maharashtra express', 'pune', 'pachora', '20:20:00.000000', '20:50:00.000000', 0, 10, 3, 0, 550, 250, '2024-02-26'),
(7, 11040, 'Maharashtra express', 'pune', 'pachora', '20:20:00.000000', '20:50:00.000000', 0, 10, 3, 0, 550, 250, '2024-02-27'),
(8, 11040, 'Maharashtra express', 'pune', 'pachora', '20:20:00.000000', '20:50:00.000000', 0, 10, 3, 0, 550, 250, '2024-02-28'),
(9, 11040, 'Maharashtra express', 'pune', 'pachora', '20:20:00.000000', '20:50:00.000000', 0, 10, 3, 0, 550, 250, '2024-02-29'),
(10, 11070, 'Jhelum Express', 'pune', 'pachora', '17:11:00.000000', '17:25:00.000000', 100, 0, 30, 0, 255, 650, '2024-02-23'),
(11, 11070, 'Jhelum Express', 'pune', 'pachora', '17:11:00.000000', '17:25:00.000000', 10, 0, 0, 4, 255, 650, '2024-02-24'),
(12, 11070, 'Jhelum Express', 'pune', 'pachora', '17:11:00.000000', '17:25:00.000000', 11, 0, 1, 0, 255, 650, '2024-02-25');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `rail_ticket_application_train`
--
ALTER TABLE `rail_ticket_application_train`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `rail_ticket_application_train`
--
ALTER TABLE `rail_ticket_application_train`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
