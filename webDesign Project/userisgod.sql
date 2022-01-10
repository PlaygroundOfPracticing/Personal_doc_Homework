-- phpMyAdmin SQL Dump
-- version 2.11.9.2
-- http://www.phpmyadmin.net
--
-- 主机: 127.0.0.1:3306
-- 生成日期: 2020 年 12 月 08 日 05:24
-- 服务器版本: 5.1.28
-- PHP 版本: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- 数据库: `userisgod`
--

-- --------------------------------------------------------

--
-- 表的结构 `comment`
--

CREATE TABLE IF NOT EXISTS `comment` (
  `id` tinyint(6) unsigned zerofill NOT NULL COMMENT '图片的id，也就是名字',
  `comment` varchar(100) CHARACTER SET utf8 NOT NULL COMMENT '主键。因为一个图片下可有多个评论。',
  `critic` varchar(100) CHARACTER SET utf8 NOT NULL,
  PRIMARY KEY (`comment`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- 导出表中的数据 `comment`
--

INSERT INTO `comment` (`id`, `comment`, `critic`) VALUES
(000003, 'glassï¼Ÿ', 'Mio'),
(000004, 'I love this guitar!', 'Mio'),
(000004, 'Where you broungt i?', 'Mio'),
(000004, 'Is it a fender Mustang?', 'Mio'),
(000001, 'This ship looks nice.', 'Mio'),
(000001, 'What is the caliber of this gun?', 'Mio'),
(000007, 'Where was this picture taken?', 'Mio'),
(000003, 'How much is your camera?', 'Mio'),
(000002, 'pineapple? sounds great!', 'Mio'),
(000007, 'sweet purple', 'root'),
(000008, '1144', 'testDelete'),
(000008, 'hi, im you too.', 'root'),
(000002, 'i â¥(^_-) GUANGZHOU', 'root');

-- --------------------------------------------------------

--
-- 表的结构 `user`
--

CREATE TABLE IF NOT EXISTS `user` (
  `id` tinyint(6) unsigned zerofill NOT NULL AUTO_INCREMENT,
  `Name` varchar(32) CHARACTER SET utf8 NOT NULL,
  `Password` char(32) CHARACTER SET utf8 NOT NULL,
  `Sexual` varchar(32) CHARACTER SET utf8 NOT NULL,
  `authority` tinyint(1) DEFAULT NULL COMMENT '是否具有管理员权限',
  `ipaddress` varchar(15) CHARACTER SET utf8 NOT NULL COMMENT '访问用户的IP地址',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=19 ;

--
-- 导出表中的数据 `user`
--

INSERT INTO `user` (`id`, `Name`, `Password`, `Sexual`, `authority`, `ipaddress`) VALUES
(000016, 'onlinetest', '12333', 'Unknown', 0, '127.0.0.1'),
(000004, '1', '1', 'test', 0, '127.0.0.1'),
(000015, 'testDelete', '1234', 'test', 0, '127.0.0.1'),
(000007, 'root', 'root', 'admin', 0, '127.0.0.1'),
(000001, 'Mio', 'fenderJB62', 'admin', 1, '127.0.0.1'),
(000017, 'iptest', '121', 'Unknown', 0, '127.0.0.1'),
(000018, '13360998939', '11', 'Unknown', 0, '10.173.167.87');
