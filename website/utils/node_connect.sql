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
-- Table structure for table `ndm_node_connect`
--

-- DROP TABLE IF EXISTS `ndm_node_connect`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
-- CREATE TABLE `ndm_node_connect` (
--   `id` char(32) NOT NULL,
--   `ip1_id` char(32) NOT NULL,
--   `ip2_id` char(32) NOT NULL,
--   `mode` varchar(128) NOT NULL,
--   `create_time` datetime(6) NOT NULL,
--   `comment` longtext,
--   PRIMARY KEY (`id`),
--   KEY `ndm_node_connect_ip1_id_9db9fb0b` (`ip1_id`),
--   KEY `ndm_node_connect_ip2_id_ccc63396` (`ip2_id`),
--   CONSTRAINT `ndm_node_connect_ip1_id_9db9fb0b_fk_ndm_node_id` FOREIGN KEY (`ip1_id`) REFERENCES `ndm_node` (`id`),
--   CONSTRAINT `ndm_node_connect_ip2_id_ccc63396_fk_ndm_node_id` FOREIGN KEY (`ip2_id`) REFERENCES `ndm_node` (`id`)
-- ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ndm_node_connect`
--

-- LOCK TABLES `ndm_node_connect` WRITE;
/*!40000 ALTER TABLE `ndm_node_connect` DISABLE KEYS */;
INSERT INTO `ndm_node_connect` (id,ip1_id,ip2_id,mode,create_time,comment) VALUES ('03482ee6552d4375bb6e1b808d740e4c','e438d2f5e2ff4b4ca97109767b10633b','5bd2c565ff254ac5aa27099932d6982f','reticle','2018-07-06 10:52:58.673328',''),('130ad2286ba34bdab9cd7cbccf158c2f','f638e15a40584379b87b468fac6a40d4','03374f316ce7421fb100b6a1ff8ce4d6','reticle','2018-07-06 11:11:47.542564',''),('1a6d7304d69442a3966b482b695dcf28','40b3765cc6e241e79f4a2e2e0915f914','86e2527162c144e694d21bc99310c8e9','reticle','2018-07-06 11:09:09.641170',''),('1d560587ab0c4a9684bbb8bf8f6efe9d','49070a18ada047edb73b2ad95da590e1','cf8df0eaf88a4b4bbcd6f490d99a4c36','optical','2018-07-06 10:48:59.036864',''),('20263e035ea546039b794808909c91d7','40b3765cc6e241e79f4a2e2e0915f914','53aad47aefc546ed94c2d90589e81518','reticle','2018-07-06 11:10:12.968532',''),('28fcc06941f64773924a3ed443411ba0','cecad3c05ef0423c864a10c6c8d7dc36','f638e15a40584379b87b468fac6a40d4','optical','2018-07-06 10:57:04.528798',''),('29a1723536ac405594240327aa1ace7d','e438d2f5e2ff4b4ca97109767b10633b','3e9608b61ae54379b6f1051c73cd735f','reticle','2018-07-06 11:35:01.950733',''),('2fa0a76599a4477dad8f3e11863d308c','b6619a7944104bba8b3ceea7366eff89','e438d2f5e2ff4b4ca97109767b10633b','reticle','2018-07-06 10:54:16.897823',''),('2ff07bc6e75641e98fe9cf46e05ec304','e438d2f5e2ff4b4ca97109767b10633b','53b22dd16fea4d9c8e41e05d7e5f25ad','reticle','2018-07-06 11:28:08.656162',''),('31be571901c84525b992f004450a4f2c','a4370ac10da847578c20814d52e1efb5','538d19e2ca944de5bb1fed6e5598f7ac','reticle','2018-07-06 10:56:31.343317',''),('41fe00fe4de14c6c869fcb9b9045336b','538d19e2ca944de5bb1fed6e5598f7ac','4401b09db5fb4b82b9b7eecd5c0b7fe2','reticle','2018-07-06 11:31:45.467081',''),('4aa2db985bf04953b35230bcebcec6b7','118507f8fcf04268b3b0e7c15e238e25','e438d2f5e2ff4b4ca97109767b10633b','reticle','2018-07-06 10:53:40.013044',''),('4d88d0c3035a4c46aa429be04a192433','e438d2f5e2ff4b4ca97109767b10633b','5d4857f4d2fd4ebaa7b0da169583a477','reticle','2018-07-06 10:54:08.120068',''),('54eae371fb9741f0bf80b7f74c41b3f9','538d19e2ca944de5bb1fed6e5598f7ac','36c5cad7470b4d19b2cdcea14d3b6d1f','reticle','2018-07-06 10:55:23.762176',''),('57aee4b3541541519e35e852717222fc','e438d2f5e2ff4b4ca97109767b10633b','538d19e2ca944de5bb1fed6e5598f7ac','reticle','2018-07-06 10:54:50.864019',''),('5bcb89e1b69b496bbe8601a1aeeb3262','e438d2f5e2ff4b4ca97109767b10633b','99a357503a9048c4bec9e7b98ba148fd','reticle','2018-07-06 10:54:29.608311',''),('66588c63a2fb40d88a139282380c2212','538d19e2ca944de5bb1fed6e5598f7ac','dbbe24b65bb240b9b15b64f66175b768','reticle','2018-07-06 10:55:32.575165',''),('66f72573949d4795b0a72563b37e9338','40b3765cc6e241e79f4a2e2e0915f914','e40ac82cc7c742b08a53908992056075','reticle','2018-07-06 11:10:37.566499',''),('679c752d3c9541e0a23d0e1f18a910f7','e438d2f5e2ff4b4ca97109767b10633b','cecad3c05ef0423c864a10c6c8d7dc36','reticle','2018-07-06 10:53:05.333037',''),('68821dfa95584461b4658b896035f2d6','e6c062bf615349ddbe014f985a7080da','cf8df0eaf88a4b4bbcd6f490d99a4c36','optical','2018-07-06 10:48:44.248035',''),('6df8645352624d71888b703bf5aaefb6','40b3765cc6e241e79f4a2e2e0915f914','56f38b911e164ec1b31a62854097576a','reticle','2018-07-06 11:10:05.994891',''),('70c3abef73c14672847aaad74f9d3509','40b3765cc6e241e79f4a2e2e0915f914','f638e15a40584379b87b468fac6a40d4','reticle','2018-07-06 11:08:48.123578',''),('7ee4bd78d9024125824266ec30202dfd','538d19e2ca944de5bb1fed6e5598f7ac','fb97cfff34c3445f94edf84244a0c9cd','reticle','2018-07-06 10:55:40.611342',''),('85331499bb4143b987fa75396c160aab','f638e15a40584379b87b468fac6a40d4','baee653e5e38460b8d8cc117d82b2ce4','reticle','2018-07-06 11:11:37.787610',''),('857d315e44d44d47b085c56d517a33c8','538d19e2ca944de5bb1fed6e5598f7ac','78d963273cae41108e9804e03ada6d84','reticle','2018-07-06 10:56:00.632240',''),('8c6f70ebed264f9989566a2d7f8b04cf','538d19e2ca944de5bb1fed6e5598f7ac','c6ec575bd6c349ecb6efcd8df36dc64f','reticle','2018-07-06 10:56:07.574239',''),('8e5ada1bbde441738c0b3d4f23907588','e438d2f5e2ff4b4ca97109767b10633b','37e8cadee3ec48c09433d1e65c5e6b9d','reticle','2018-07-06 10:49:16.674932',''),('8fb7c618df6148fd8d98e4321c3ea8fd','538d19e2ca944de5bb1fed6e5598f7ac','8ec26dc2adc54c56b1bffe03a2d6eb0c','reticle','2018-07-06 10:56:37.093216',''),('9a3df9ea17264fa0b8911b552f1fe457','03374f316ce7421fb100b6a1ff8ce4d6','f638e15a40584379b87b468fac6a40d4','reticle','2018-07-06 11:07:43.977037',''),('9c13c36d6f6e45dfbad1c43658d0da6e','94256573679e4c2e941715698ea6fbf7','e438d2f5e2ff4b4ca97109767b10633b','reticle','2018-07-06 10:53:49.315580',''),('9d58cea6a0d74af8bda9ed87ea8afdfb','538d19e2ca944de5bb1fed6e5598f7ac','2611138edadd4e86962eca8d143ac01f','reticle','2018-07-06 10:55:53.946188',''),('a2ed160912f34d9c88957d3333e9e99b','3f1bb7b64fa647a6b2c75e0781ac40d0','f638e15a40584379b87b468fac6a40d4','reticle','2018-07-06 11:08:16.378192',''),('a84157edd21142fc90a4736f50eb01ae','40b3765cc6e241e79f4a2e2e0915f914','d8c5bc39d6044909abac850ddabd0640','reticle','2018-07-06 11:10:20.397411',''),('b5943647eedd44c48dfb6fcddd6b6ee8','40b3765cc6e241e79f4a2e2e0915f914','24711861690a4e2a92cdaf761e44b1a0','reticle','2018-07-06 11:09:31.922732',''),('bc9de7a3f4ea4170a8632c82adaa068b','e438d2f5e2ff4b4ca97109767b10633b','af2c25383a384a0caa05d2981d575c16','reticle','2018-07-06 10:53:30.205916',''),('be71b8de42db452cb627dbe2acb8af50','e438d2f5e2ff4b4ca97109767b10633b','cf8df0eaf88a4b4bbcd6f490d99a4c36','reticle','2018-07-06 10:49:25.063398',''),('d58ef7fd5f66407fb07c9ec6f5d4e656','ae45ad8208b34aaf9ffeb653ca1d7b72','f638e15a40584379b87b468fac6a40d4','reticle','2018-07-06 11:08:37.709819',''),('d6880994bace4521aa573df6ece57b52','538d19e2ca944de5bb1fed6e5598f7ac','126d9098252b47f69a8333bae89367a5','reticle','2018-07-06 10:56:21.115491',''),('dcb13c38012c428bbafb5f9d089b56c9','37e8cadee3ec48c09433d1e65c5e6b9d','d39d057d1f1e4763b4e29eccd9c8b30c','optical','2018-07-06 10:47:57.895979',''),('e3edbfa74def44e1a27385a095e5735d','f638e15a40584379b87b468fac6a40d4','6c10f1cd105246aeaefeb86f18b830f8','reticle','2018-07-06 11:08:26.015403',''),('f0ac9e9527704a679d7c4e1108adccde','538d19e2ca944de5bb1fed6e5598f7ac','06b0579fe0dd44ed9fd9934557e9b5c8','reticle','2018-07-06 10:55:07.921867','');
/*!40000 ALTER TABLE `ndm_node_connect` ENABLE KEYS */;
-- UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-07-09 10:08:59
