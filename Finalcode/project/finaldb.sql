/*
SQLyog Community Edition- MySQL GUI v7.01 
MySQL - 5.0.27-community-nt : Database - 032-cosmetics
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`032-cosmetics` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `032-cosmetics`;

/*Table structure for table `products` */

DROP TABLE IF EXISTS `products`;

CREATE TABLE `products` (
  `PRODUCT_ID` int(255) NOT NULL auto_increment,
  `NAME` varchar(255) default NULL,
  `PRICE` varchar(255) default NULL,
  `DESCRIPTION` longtext,
  `TYPE` varchar(255) default NULL,
  `PCS` varchar(255) default NULL,
  `filenamepath` varchar(255) default NULL,
  PRIMARY KEY  (`PRODUCT_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `products` */

insert  into `products`(`PRODUCT_ID`,`NAME`,`PRICE`,`DESCRIPTION`,`TYPE`,`PCS`,`filenamepath`) values (1,'skin lacto','2000','Re\'equil Ceramide & Hyaluronic Acid Moisturiser For Normal To Dry Skin','Combination','6','static/profile/download.jpg'),(2,'Lakme ','9999','  Best Lakme Products','Combination','5','static/profile/as.jpg'),(3,'Tresemme Smooth & Shine','1500','Tresemme Smooth & Shine Pro Collection Shampoo - Vitamin H & Silk Protein, 580 ml Bottle','Dry','3','static/profile/images_1.jpg'),(4,'Legal frame','6000','A cosmetic product is defined in the Regulation as any substance ','Oily','3','static/profile/ff.jpg'),(5,'Stainless Steel Herbal Cosmetic','9000','Stainless Steel Herbal Cosmetic Products at Best Price in Pune','Combination','4','static/profile/f.jpg'),(6,'Love Beauty','10000','Love Beauty & Planet Natural Murumuru Butter and Rose Sulfate Free Body Wash','Normal','4','static/profile/d.jpg');

/*Table structure for table `recomdedpro` */

DROP TABLE IF EXISTS `recomdedpro`;

CREATE TABLE `recomdedpro` (
  `id` int(255) NOT NULL auto_increment,
  `productname` varchar(255) default NULL,
  `productid` varchar(255) default NULL,
  `comment` longtext,
  `username` varchar(255) default NULL,
  `username_img` varchar(255) default NULL,
  `USERID` varchar(255) default NULL,
  `producttype` varchar(255) default NULL,
  `rating` varchar(255) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `recomdedpro` */

insert  into `recomdedpro`(`id`,`productname`,`productid`,`comment`,`username`,`username_img`,`USERID`,`producttype`,`rating`) values (1,'skin lacto','1','not good but also bad','roshan','static/profile/client_1.jpg','1','Combination','4'),(2,'Lakme ','2','this was good product','roshan','static/profile/client_1.jpg','1','Combination','2'),(3,'Tresemme Smooth & Shine','3','not good but also bad','roshan','static/profile/client_1.jpg','1','Dry','5'),(4,'Legal frame','4','not good but also bad','roshan','static/profile/client_1.jpg','1','Oily','4'),(5,'skin lacto','1','this was good product','yash','static/profile/client_2.jpg','2','Combination','3'),(6,'Lakme ','2','this was good product','yash','static/profile/client_2.jpg','2','Combination','5'),(7,'Stainless Steel Herbal Cosmetic','5','this was good product','yash','static/profile/client_2.jpg','2','Combination','3'),(8,'Tresemme Smooth & Shine','3','This paper focuses on predicting the yield of the crop by applying various machine learning techniques.','yash','static/profile/client_2.jpg','2','Dry','4'),(9,'Love Beauty','6','not good but also bad','yash','static/profile/client_2.jpg','2','Normal','5');

/*Table structure for table `userregisters` */

DROP TABLE IF EXISTS `userregisters`;

CREATE TABLE `userregisters` (
  `Id` int(255) NOT NULL auto_increment,
  `Username` varchar(255) default NULL,
  `Email` varchar(255) default NULL,
  `Mobile` varchar(255) default NULL,
  `Password` varchar(255) default NULL,
  `Profile_Img` varchar(255) default NULL,
  `Address` varchar(255) default NULL,
  `Pancard` varchar(255) default NULL,
  PRIMARY KEY  (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `userregisters` */

insert  into `userregisters`(`Id`,`Username`,`Email`,`Mobile`,`Password`,`Profile_Img`,`Address`,`Pancard`) values (1,'roshan','sujay@gmail.com','9561161391','Abc@123','static/profile/client_1.jpg','mumbai','456123123123'),(2,'yash','stawar59@gmail.com','8796655332','Yash@123','static/profile/client_2.jpg','vikroli','963258741147');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
