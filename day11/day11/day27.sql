-- MySQL dump 10.13  Distrib 5.6.43, for Win64 (x86_64)
--
-- Host: localhost    Database: py27_day11
-- ------------------------------------------------------
-- Server version	5.6.43

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
-- Table structure for table `class`
--

DROP TABLE IF EXISTS `class`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `class` (
  `cid` int(11) DEFAULT NULL,
  `classname` char(12) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `class`
--

LOCK TABLES `class` WRITE;
/*!40000 ALTER TABLE `class` DISABLE KEYS */;
INSERT INTO `class` VALUES (1,'py27');
/*!40000 ALTER TABLE `class` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `class2`
--

DROP TABLE IF EXISTS `class2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `class2` (
  `cid` int(11) NOT NULL,
  `classname` char(12) DEFAULT NULL,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `class2`
--

LOCK TABLES `class2` WRITE;
/*!40000 ALTER TABLE `class2` DISABLE KEYS */;
INSERT INTO `class2` VALUES (1,'py27'),(3,'py26');
/*!40000 ALTER TABLE `class2` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `class3`
--

DROP TABLE IF EXISTS `class3`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `class3` (
  `cid` int(11) NOT NULL,
  `classname` char(12) DEFAULT NULL,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `class3`
--

LOCK TABLES `class3` WRITE;
/*!40000 ALTER TABLE `class3` DISABLE KEYS */;
INSERT INTO `class3` VALUES (2,'py27'),(3,'py26');
/*!40000 ALTER TABLE `class3` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `department`
--

DROP TABLE IF EXISTS `department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `department` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `department`
--

LOCK TABLES `department` WRITE;
/*!40000 ALTER TABLE `department` DISABLE KEYS */;
INSERT INTO `department` VALUES (200,'技术'),(201,'人力资源'),(202,'销售'),(203,'运营');
/*!40000 ALTER TABLE `department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `emp`
--

DROP TABLE IF EXISTS `emp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `emp` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT NULL,
  `sex` enum('male','female') NOT NULL DEFAULT 'male',
  `age` int(11) DEFAULT NULL,
  `dep_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `emp`
--

LOCK TABLES `emp` WRITE;
/*!40000 ALTER TABLE `emp` DISABLE KEYS */;
INSERT INTO `emp` VALUES (1,'egon','male',18,200),(2,'alex','female',48,201),(3,'wupeiqi','male',38,201),(4,'yuanhao','female',28,202),(5,'liwenzhou','male',18,200),(6,'jingliyang','female',18,204);
/*!40000 ALTER TABLE `emp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `employee` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `emp_name` varchar(20) NOT NULL,
  `sex` enum('male','female') NOT NULL DEFAULT 'male',
  `age` int(3) unsigned NOT NULL DEFAULT '28',
  `hire_date` date NOT NULL,
  `post` varchar(50) DEFAULT NULL,
  `post_comment` varchar(100) DEFAULT NULL,
  `salary` double(15,2) DEFAULT NULL,
  `office` int(11) DEFAULT NULL,
  `depart_id` int(11) DEFAULT NULL,
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES (1,'egon','male',18,'2017-03-01','老男孩驻沙河办事处外交大使',NULL,7300.33,401,1),(2,'alex','male',78,'2015-03-02','teacher',NULL,1000000.31,401,1),(3,'wupeiqi','male',81,'2013-03-05','teacher',NULL,8300.00,401,1),(4,'yuanhao','male',73,'2014-07-01','teacher',NULL,3500.00,401,1),(5,'liwenzhou','male',28,'2012-11-01','teacher',NULL,2100.00,401,1),(6,'jingliyang','female',18,'2011-02-11','teacher',NULL,9000.00,401,1),(7,'jinxin','male',18,'1900-03-01','teacher',NULL,30000.00,401,1),(8,'成龙','male',48,'2010-11-11','teacher',NULL,10000.00,401,1),(9,'歪歪','female',48,'2015-03-11','sale',NULL,3000.13,402,2),(10,'丫丫','female',38,'2010-11-01','sale',NULL,2000.35,402,2),(11,'丁丁','female',18,'2011-03-12','sale',NULL,1000.37,402,2),(12,'星星','female',18,'2016-05-13','sale',NULL,3000.29,402,2),(13,'格格','female',28,'2017-01-27','sale',NULL,4000.33,402,2),(14,'张野','male',28,'2016-03-11','operation',NULL,10000.13,403,3),(15,'程咬金','male',18,'1997-03-12','operation',NULL,20000.00,403,3),(16,'程咬银','female',18,'2013-03-11','operation',NULL,19000.00,403,3),(17,'程咬铜','male',18,'2015-04-11','operation',NULL,18000.00,403,3),(18,'程咬铁','female',18,'2014-05-12','operation',NULL,17000.00,403,3);
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `server_info`
--

DROP TABLE IF EXISTS `server_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `server_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` char(20) DEFAULT NULL,
  `ip` char(15) DEFAULT NULL,
  `port` int(5) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ip` (`ip`,`port`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `server_info`
--

LOCK TABLES `server_info` WRITE;
/*!40000 ALTER TABLE `server_info` DISABLE KEYS */;
INSERT INTO `server_info` VALUES (1,'mysql','192.168.12.38',3306),(2,'mysql','192.168.12.39',3306),(3,'nginx','192.168.12.38',80),(5,'xxxx',NULL,80);
/*!40000 ALTER TABLE `server_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `server_info2`
--

DROP TABLE IF EXISTS `server_info2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `server_info2` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` char(20) DEFAULT NULL,
  `ip` char(15) NOT NULL DEFAULT '',
  `port` int(5) NOT NULL DEFAULT '0',
  PRIMARY KEY (`ip`,`port`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `server_info2`
--

LOCK TABLES `server_info2` WRITE;
/*!40000 ALTER TABLE `server_info2` DISABLE KEYS */;
/*!40000 ALTER TABLE `server_info2` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stu`
--

DROP TABLE IF EXISTS `stu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stu` (
  `id` int(11) DEFAULT NULL,
  `name` char(12) DEFAULT NULL,
  `cid` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stu`
--

LOCK TABLES `stu` WRITE;
/*!40000 ALTER TABLE `stu` DISABLE KEYS */;
INSERT INTO `stu` VALUES (2,'立立',300);
/*!40000 ALTER TABLE `stu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stu2`
--

DROP TABLE IF EXISTS `stu2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stu2` (
  `id` int(11) DEFAULT NULL,
  `name` char(12) DEFAULT NULL,
  `class_id` int(11) DEFAULT NULL,
  KEY `class_id` (`class_id`),
  CONSTRAINT `stu2_ibfk_1` FOREIGN KEY (`class_id`) REFERENCES `class2` (`cid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stu2`
--

LOCK TABLES `stu2` WRITE;
/*!40000 ALTER TABLE `stu2` DISABLE KEYS */;
INSERT INTO `stu2` VALUES (1,'立立',1),(2,'汤汤',1);
/*!40000 ALTER TABLE `stu2` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stu3`
--

DROP TABLE IF EXISTS `stu3`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stu3` (
  `id` int(11) DEFAULT NULL,
  `name` char(12) DEFAULT NULL,
  `class_id` int(11) DEFAULT NULL,
  KEY `class_id` (`class_id`),
  CONSTRAINT `stu3_ibfk_1` FOREIGN KEY (`class_id`) REFERENCES `class3` (`cid`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stu3`
--

LOCK TABLES `stu3` WRITE;
/*!40000 ALTER TABLE `stu3` DISABLE KEYS */;
INSERT INTO `stu3` VALUES (1,'立立',2),(2,'汤汤',2);
/*!40000 ALTER TABLE `stu3` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `student` (
  `id` int(11) DEFAULT NULL,
  `name` char(12) DEFAULT NULL,
  `phone` char(11) DEFAULT NULL,
  `gender` enum('male','female') DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES (1,'alex','13838443838','male'),(1,'alex','13838443838','male');
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student2`
--

DROP TABLE IF EXISTS `student2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `student2` (
  `id` int(11) DEFAULT NULL,
  `name` char(12) NOT NULL,
  `phone` char(11) DEFAULT NULL,
  `gender` enum('male','female') DEFAULT NULL,
  UNIQUE KEY `id` (`id`),
  UNIQUE KEY `phone` (`phone`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student2`
--

LOCK TABLES `student2` WRITE;
/*!40000 ALTER TABLE `student2` DISABLE KEYS */;
INSERT INTO `student2` VALUES (1,'alex','13838384438','male');
/*!40000 ALTER TABLE `student2` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student3`
--

DROP TABLE IF EXISTS `student3`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `student3` (
  `id` int(11) DEFAULT NULL,
  `name` char(12) NOT NULL,
  `phone` char(11) DEFAULT NULL,
  `gender` enum('male','female') DEFAULT 'male',
  UNIQUE KEY `id` (`id`),
  UNIQUE KEY `phone` (`phone`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student3`
--

LOCK TABLES `student3` WRITE;
/*!40000 ALTER TABLE `student3` DISABLE KEYS */;
INSERT INTO `student3` VALUES (1,'alex','13838384438','male');
/*!40000 ALTER TABLE `student3` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student5`
--

DROP TABLE IF EXISTS `student5`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `student5` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` char(12) NOT NULL,
  `phone` char(11) DEFAULT NULL,
  `gender` enum('male','female') DEFAULT 'male',
  UNIQUE KEY `id` (`id`),
  UNIQUE KEY `phone` (`phone`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student5`
--

LOCK TABLES `student5` WRITE;
/*!40000 ALTER TABLE `student5` DISABLE KEYS */;
INSERT INTO `student5` VALUES (1,'alex','13838384438','male'),(2,'松松','13233334444','male'),(4,'立立','13266669999','male');
/*!40000 ALTER TABLE `student5` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student6`
--

DROP TABLE IF EXISTS `student6`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `student6` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` char(12) NOT NULL,
  `phone` char(11) DEFAULT NULL,
  `gender` enum('male','female') DEFAULT 'male',
  UNIQUE KEY `id` (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `phone` (`phone`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student6`
--

LOCK TABLES `student6` WRITE;
/*!40000 ALTER TABLE `student6` DISABLE KEYS */;
/*!40000 ALTER TABLE `student6` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student7`
--

DROP TABLE IF EXISTS `student7`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `student7` (
  `name` char(12) NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `phone` char(11) DEFAULT NULL,
  `gender` enum('male','female') DEFAULT 'male',
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `id` (`id`),
  UNIQUE KEY `phone` (`phone`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student7`
--

LOCK TABLES `student7` WRITE;
/*!40000 ALTER TABLE `student7` DISABLE KEYS */;
/*!40000 ALTER TABLE `student7` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student8`
--

DROP TABLE IF EXISTS `student8`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `student8` (
  `name` char(12) NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `phone` char(11) DEFAULT NULL,
  `gender` enum('male','female') DEFAULT 'male',
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `phone` (`phone`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student8`
--

LOCK TABLES `student8` WRITE;
/*!40000 ALTER TABLE `student8` DISABLE KEYS */;
/*!40000 ALTER TABLE `student8` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t1`
--

DROP TABLE IF EXISTS `t1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t1` (
  `a` int(11) DEFAULT NULL,
  `b` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t1`
--

LOCK TABLES `t1` WRITE;
/*!40000 ALTER TABLE `t1` DISABLE KEYS */;
INSERT INTO `t1` VALUES (1,2),(3,4),(5,6);
/*!40000 ALTER TABLE `t1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t2`
--

DROP TABLE IF EXISTS `t2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t2` (
  `c` int(11) DEFAULT NULL,
  `d` int(11) DEFAULT NULL,
  `e` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t2`
--

LOCK TABLES `t2` WRITE;
/*!40000 ALTER TABLE `t2` DISABLE KEYS */;
INSERT INTO `t2` VALUES (1,1,1),(2,2,2),(3,3,3);
/*!40000 ALTER TABLE `t2` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-09-22 19:30:31
