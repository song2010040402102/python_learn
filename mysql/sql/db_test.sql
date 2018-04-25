# Host: ubuntu  (Version 5.7.21-0ubuntu0.16.04.1)
# Date: 2018-04-25 10:25:08
# Generator: MySQL-Front 5.4  (Build 4.153) - http://www.mysqlfront.de/

/*!40101 SET NAMES utf8 */;

#
# Structure for table "tb_test"
#

DROP TABLE IF EXISTS `tb_test`;
CREATE TABLE `tb_test` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

#
# Data for table "tb_test"
#

INSERT INTO `tb_test` VALUES (1,'ABC'),(2,'DEF'),(3,'GHI'),(4,'abc');
