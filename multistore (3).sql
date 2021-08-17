-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 17, 2021 at 07:54 AM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 7.4.15

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `multistore`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `last_login` varchar(255) DEFAULT NULL,
  `type_1` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`email`, `password`, `last_login`, `type_1`) VALUES
('ADMIN2@GMAIL.COM', '123', NULL, 'Admin'),
('admin@gmail.com', 'admin@123', '2021-08-16 10:39:22', 'Admin');

-- --------------------------------------------------------

--
-- Table structure for table `bill`
--

CREATE TABLE `bill` (
  `BilliD` int(50) NOT NULL,
  `dateOfBill` varchar(255) NOT NULL,
  `billBy` int(255) NOT NULL,
  `totalAmount` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `bill`
--

INSERT INTO `bill` (`BilliD`, `dateOfBill`, `billBy`, `totalAmount`) VALUES
(22, '07/30/21', 12345, '1100'),
(23, '07/30/21', 12345, '2560'),
(27, '08/14/21', 12345, '4814');

-- --------------------------------------------------------

--
-- Table structure for table `billdetails`
--

CREATE TABLE `billdetails` (
  `detail_ID` int(255) NOT NULL,
  `bill_ID` int(255) NOT NULL,
  `product_ID` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  `price` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `billdetails`
--

INSERT INTO `billdetails` (`detail_ID`, `bill_ID`, `product_ID`, `quantity`, `price`) VALUES
(12, 22, 7, 2, 1100),
(13, 23, 7, 1, 550),
(14, 23, 1, 3, 2010),
(21, 27, 7, 1, 550),
(22, 27, 3, 1, 568),
(23, 27, 15, 3, 3696);

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

CREATE TABLE `category` (
  `CategoryName` varchar(255) NOT NULL,
  `Description` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `category`
--

INSERT INTO `category` (`CategoryName`, `Description`) VALUES
('BUTTER', 'ADSLHFLASF\n'),
('Juices', 'fresh and good quality juice.\n'),
('makhan mali', 'tasy and spice'),
('malaimakhan', 'kajal');

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `PID` int(11) NOT NULL,
  `PName` varchar(255) NOT NULL,
  `PPrice` int(100) NOT NULL,
  `PDescription` varchar(500) NOT NULL,
  `CatergoryName` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`PID`, `PName`, `PPrice`, `PDescription`, `CatergoryName`) VALUES
(1, 'kali DASF', 670, 'dsdsadas', 'malaimakhan'),
(3, 'lal mirch', 568, 'lal mirch	\n', 'malaimakhan'),
(6, 'jam', 500, 'mixed fruit jam\n', 'makhan mali'),
(7, 'chikku jam', 550, 'chikku jam\n', 'malaimakhan'),
(13, 'imli', 0, 'imloi\n', 'malaimakhan'),
(14, 'imli 2', 0, 'dkjshf\n', 'malaimakhan'),
(15, 'fas', 1232, 'asbdhflkn	\n', 'malaimakhan');

-- --------------------------------------------------------

--
-- Table structure for table `storeview`
--

CREATE TABLE `storeview` (
  `StoreID` int(255) NOT NULL,
  `StoreName` varchar(255) NOT NULL,
  `emailID` varchar(255) NOT NULL,
  `Location` varchar(255) NOT NULL,
  `Password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `storeview`
--

INSERT INTO `storeview` (`StoreID`, `StoreName`, `emailID`, `Location`, `Password`) VALUES
(15, 'D-mart', 'dmart@gmail.com', 'amritsar', '1234'),
(5546, 'gdfgfdgg', 'dfsgdfgdf', 'dfgdfgdg', 'gdgs'),
(12345, 'ambaji goods', 'ambaji@gmail.com', 'amritsa', '12345');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`email`);

--
-- Indexes for table `bill`
--
ALTER TABLE `bill`
  ADD PRIMARY KEY (`BilliD`),
  ADD KEY `billBy` (`billBy`);

--
-- Indexes for table `billdetails`
--
ALTER TABLE `billdetails`
  ADD PRIMARY KEY (`detail_ID`),
  ADD KEY `billdetails_ibfk_1` (`product_ID`),
  ADD KEY `bill_ID` (`bill_ID`);

--
-- Indexes for table `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`CategoryName`);

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`PID`),
  ADD KEY `products_ibfk_1` (`CatergoryName`);

--
-- Indexes for table `storeview`
--
ALTER TABLE `storeview`
  ADD PRIMARY KEY (`StoreID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bill`
--
ALTER TABLE `bill`
  MODIFY `BilliD` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `billdetails`
--
ALTER TABLE `billdetails`
  MODIFY `detail_ID` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `PID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `bill`
--
ALTER TABLE `bill`
  ADD CONSTRAINT `bill_ibfk_1` FOREIGN KEY (`billBy`) REFERENCES `storeview` (`StoreID`);

--
-- Constraints for table `billdetails`
--
ALTER TABLE `billdetails`
  ADD CONSTRAINT `billdetails_ibfk_1` FOREIGN KEY (`product_ID`) REFERENCES `products` (`PID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `billdetails_ibfk_2` FOREIGN KEY (`bill_ID`) REFERENCES `bill` (`BilliD`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `products`
--
ALTER TABLE `products`
  ADD CONSTRAINT `products_ibfk_1` FOREIGN KEY (`CatergoryName`) REFERENCES `category` (`CategoryName`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
