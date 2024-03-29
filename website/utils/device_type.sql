-- MySQL dump 10.13  Distrib 5.7.20, for osx10.12 (x86_64)
--
-- Host: localhost    Database: ndm
-- ------------------------------------------------------
-- Server version	5.7.20

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `ndm_device_type`
--

-- DROP TABLE IF EXISTS `ndm_device_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
-- CREATE TABLE `ndm_device_type` (
--   `id` char(32) NOT NULL,
--   `name` varchar(128) NOT NULL,
--   `create_time` datetime(6) NOT NULL,
--   `comment` longtext,
--   PRIMARY KEY (`id`)
-- ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ndm_device_type`
--

-- LOCK TABLES `ndm_device_type` WRITE;
/*!40000 ALTER TABLE `ndm_device_type` DISABLE KEYS */;
INSERT INTO `ndm_device_type` (id,name,create_time,comment) VALUES ('2467e3a5852d429da26ef5b19237a0c7','华为-USG6530-Firewall','2018-07-05 17:15:57.304363',NULL),('4e12f3ad307346348664ae677e94532b','华为-S5720-28X-PWR-SI-AC','2018-07-05 17:15:57.301718',NULL),('b2a5f1fe050c47629ca3d68aebc76ca4','华为-S5700S-52P-LI-AC','2018-07-05 17:15:57.286761',NULL),('b4dff366f2aa4fcb9f0831fbdc2dd415','华为-S5700-24TP-PWR-SI','2018-07-05 17:15:57.295053',NULL),('d44bd505a4d343c78a60644587ed55f6','华为-AR2220E-S-Router','2018-07-05 17:15:57.303138',NULL),('d82947d6307a48ebb5a560efefd53720','华为-S5720-56C-EI-AC','2018-07-05 17:15:57.300221',NULL),('f3d59571ea8e42fe9262578b856312bd','华为-AR3260E-S-Router','2018-07-05 17:15:57.298584',NULL);
/*!40000 ALTER TABLE `ndm_device_type` ENABLE KEYS */;
-- UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-07-09 17:25:48
