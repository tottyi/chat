-- Adminer 4.8.1 MySQL 5.7.31 dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

SET NAMES utf8mb4;

DROP DATABASE IF EXISTS `chat`;
CREATE DATABASE `chat` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */;
USE `chat`;

DROP TABLE IF EXISTS `chat`;
CREATE TABLE `chat` (
  `text_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_n_from` char(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `login_n_for` char(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `text` tinytext COLLATE utf8mb4_unicode_ci,
  PRIMARY KEY (`text_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `f_name` char(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `l_name` char(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `login_name` char(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `login_passw` char(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


-- 2022-02-23 14:56:06
