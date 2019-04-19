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
-- Table structure for table `ndm_node`
--

-- DROP TABLE IF EXISTS `ndm_node`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
-- CREATE TABLE `ndm_node` (
--   `id` char(32) NOT NULL,
--   `name` varchar(128) NOT NULL,
--   `show_name` varchar(128) NOT NULL,
--   `hint` varchar(128) NOT NULL,
--   `x` int(11) NOT NULL,
--   `y` int(11) NOT NULL,
--   `type` varchar(128) NOT NULL,
--   `create_time` datetime(6) NOT NULL,
--   `comment` longtext,
--   PRIMARY KEY (`id`)
-- ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ndm_node`
--

-- LOCK TABLES `ndm_node` WRITE;
/*!40000 ALTER TABLE `ndm_node` DISABLE KEYS */;
INSERT INTO `ndm_node`  (id,name,show_name,hint,x,y,type,create_time,comment) VALUES ('03374f316ce7421fb100b6a1ff8ce4d6','s_27_2','27层二层交换机2','10.10.10.22',150,800,'switch','2018-07-06 10:12:37.091093',NULL),('06b0579fe0dd44ed9fd9934557e9b5c8','p_30_1','30层POE1','10.10.10.1',650,450,'switch','2018-07-06 10:12:37.105226',NULL),('118507f8fcf04268b3b0e7c15e238e25','s_31_2c_5','31层二层交换机5','10.10.10.16',450,350,'switch','2018-07-06 10:12:37.096392',NULL),('126d9098252b47f69a8333bae89367a5','p_30_2','30层POE2','10.10.10.2',650,550,'switch','2018-07-06 10:12:37.082332',NULL),('24711861690a4e2a92cdaf761e44b1a0','s_28_2','28层二层交换机2','10.10.10.28',650,800,'switch','2018-07-06 10:12:37.071891',NULL),('2611138edadd4e86962eca8d143ac01f','s_30_2c_6','30层二层交换机6','10.10.10.19',550,550,'switch','2018-07-06 10:12:37.108311',NULL),('36c5cad7470b4d19b2cdcea14d3b6d1f','s_30_2c_1','30层二层交换机1','10.10.10.3',50,550,'switch','2018-07-06 10:12:37.103914',NULL),('37e8cadee3ec48c09433d1e65c5e6b9d','vpn_r_31','31层VPN路由','172.16.111.3',250,180,'router','2018-07-06 10:12:37.079171',NULL),('3e9608b61ae54379b6f1051c73cd735f','sslvpn','深信服sslvpn','172.30.100.100',140,230,'sslvpn','2018-07-06 11:32:56.942000',''),('3f1bb7b64fa647a6b2c75e0781ac40d0','s_27_4','27层二层交换机4','10.10.10.24',350,800,'switch','2018-07-06 10:12:37.101620',NULL),('40b3765cc6e241e79f4a2e2e0915f914','p_28_1','28层POE1','10.10.10.26',650,700,'switch','2018-07-06 10:12:37.080991',NULL),('4401b09db5fb4b82b9b7eecd5c0b7fe2','wlc','Cisco无线控制器','10.10.24.10',270,450,'wlc','2018-07-06 11:30:46.950724',''),('49070a18ada047edb73b2ad95da590e1','liantong_internet','联通','111.202.106.229',650,150,'internet','2018-07-06 10:12:37.093271',NULL),('538d19e2ca944de5bb1fed6e5598f7ac','core_s_30','30层核心交换机','10.10.10.254',440,450,'switch','2018-07-06 10:12:37.065543',NULL),('53aad47aefc546ed94c2d90589e81518','s_28_5','28层二层交换机5','10.10.10.31',950,800,'switch','2018-07-06 10:12:37.106744',NULL),('53b22dd16fea4d9c8e41e05d7e5f25ad','sangfor_ac','深信服上网行为管理','172.16.111.4(1.1.1.2)',550,250,'ac','2018-07-06 11:25:50.604512',''),('56f38b911e164ec1b31a62854097576a','s_28_3','28层二层交换机3','10.10.10.29',750,800,'switch','2018-07-06 10:12:37.090156',NULL),('5bd2c565ff254ac5aa27099932d6982f','s_31_2c_1','31层二层交换机1','10.10.10.10',50,350,'switch','2018-07-06 10:12:37.058231',NULL),('5d4857f4d2fd4ebaa7b0da169583a477','p_31_1','31层POE1','10.10.10.9',550,350,'switch','2018-07-06 10:12:37.086826',NULL),('6c10f1cd105246aeaefeb86f18b830f8','s_27_5','27层二层交换机5','10.10.10.25',450,800,'switch','2018-07-06 10:12:37.070295',NULL),('78d963273cae41108e9804e03ada6d84','s_30_2c_5','30层二层交换机5','10.10.10.18',450,550,'switch','2018-07-06 10:12:37.100452',NULL),('86e2527162c144e694d21bc99310c8e9','s_28_1','28层二层交换机1','10.10.10.27',550,800,'switch','2018-07-06 10:12:37.083569',NULL),('8ec26dc2adc54c56b1bffe03a2d6eb0c','p_30_4','30层POE4','10.10.10.6',850,550,'switch','2018-07-06 10:12:37.085820',NULL),('94256573679e4c2e941715698ea6fbf7','s_31_2c_3','31层二层交换机3','10.10.10.14',250,350,'switch','2018-07-06 10:12:37.111279',NULL),('99a357503a9048c4bec9e7b98ba148fd','p_31_2','31层POE2','10.10.10.12',650,350,'switch','2018-07-06 10:12:37.089227',NULL),('a4370ac10da847578c20814d52e1efb5','p_30_3','30层POE3','10.10.10.5',750,550,'switch','2018-07-06 10:12:37.098064',NULL),('ae45ad8208b34aaf9ffeb653ca1d7b72','s_27_3','27层二层交换机3','10.10.10.23',250,800,'switch','2018-07-06 10:12:37.067170',NULL),('af2c25383a384a0caa05d2981d575c16','p_31_3','31层POE3','10.10.10.13',750,350,'switch','2018-07-06 10:12:37.076168',NULL),('b6619a7944104bba8b3ceea7366eff89','s_31_2c_4','31层二层交换机4','10.10.10.15',350,350,'switch','2018-07-06 10:12:37.073362',NULL),('baee653e5e38460b8d8cc117d82b2ce4','s_27_1','27层二层交换机1','10.10.10.21',50,800,'switch','2018-07-06 10:12:37.099257',NULL),('c6ec575bd6c349ecb6efcd8df36dc64f','s_30_2c_4','30层二层交换机4','10.10.10.17',350,550,'switch','2018-07-06 10:12:37.109837',NULL),('cecad3c05ef0423c864a10c6c8d7dc36','s_31_2c_2','31层二层交换机2','10.10.10.11',150,350,'switch','2018-07-06 10:12:37.114476',NULL),('cf8df0eaf88a4b4bbcd6f490d99a4c36','firewall','31层防火墙','172.16.111.1',470,170,'firewall','2018-07-06 10:12:37.092190',NULL),('d39d057d1f1e4763b4e29eccd9c8b30c','yidong_internet','移动','39.155.227.162',120,80,'internet','2018-07-06 10:12:37.068676',NULL),('d8c5bc39d6044909abac850ddabd0640','s_28_4','28层二层交换机4','10.10.10.30',850,800,'switch','2018-07-06 10:12:37.074861',NULL),('dbbe24b65bb240b9b15b64f66175b768','s_30_2c_3','30层二层交换机3','10.10.10.7',250,550,'switch','2018-07-06 10:12:37.084829',NULL),('e40ac82cc7c742b08a53908992056075','p_28_2','28层POE2','10.10.10.32',800,700,'switch','2018-07-06 10:12:37.112696',NULL),('e438d2f5e2ff4b4ca97109767b10633b','converge_p_31','31层汇聚POE','10.10.10.8',350,250,'switch','2018-07-06 10:12:37.102770',NULL),('e6c062bf615349ddbe014f985a7080da','alibaba_network','阿里互通','172.168.200.2',350,50,'lan','2018-07-06 10:12:37.087940',NULL),('f638e15a40584379b87b468fac6a40d4','p_27_1','27层POE1','10.10.10.20',410,700,'switch','2018-07-06 10:12:37.077295',NULL),('fb97cfff34c3445f94edf84244a0c9cd','s_30_2c_2','30层二层交换机2','10.10.10.4',150,550,'switch','2018-07-06 10:12:37.094852',NULL);
/*!40000 ALTER TABLE `ndm_node` ENABLE KEYS */;
-- UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-07-09 10:06:54
