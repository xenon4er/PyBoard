-- phpMyAdmin SQL Dump
-- version 3.4.5deb1
-- http://www.phpmyadmin.net
--
-- Хост: localhost
-- Время создания: Апр 11 2012 г., 23:39
-- Версия сервера: 5.1.61
-- Версия PHP: 5.3.6-13ubuntu3.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- База данных: `klimov_k_v`
--

-- --------------------------------------------------------

--
-- Структура таблицы `countries`
--

CREATE TABLE IF NOT EXISTS `countries` (
  `cntr_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`cntr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Структура таблицы `g2r`
--

CREATE TABLE IF NOT EXISTS `g2r` (
  `g2r_id` int(11) NOT NULL AUTO_INCREMENT,
  `fk_rl_id` int(11) NOT NULL,
  `fk_gr_id` int(11) NOT NULL,
  PRIMARY KEY (`g2r_id`),
  KEY `fk_rl_id` (`fk_rl_id`),
  KEY `fk_gr_id` (`fk_gr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Структура таблицы `genders`
--

CREATE TABLE IF NOT EXISTS `genders` (
  `gndr_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`gndr_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Дамп данных таблицы `genders`
--

INSERT INTO `genders` (`gndr_id`, `name`) VALUES
(1, 'male'),
(2, 'female');

-- --------------------------------------------------------

--
-- Структура таблицы `groups`
--

CREATE TABLE IF NOT EXISTS `groups` (
  `gr_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `fk_mstr_id` int(11) NOT NULL,
  PRIMARY KEY (`gr_id`),
  KEY `fk_mstr_id` (`fk_mstr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Структура таблицы `member_group`
--

CREATE TABLE IF NOT EXISTS `member_group` (
  `m2g_id` int(11) NOT NULL AUTO_INCREMENT,
  `fk_usr_id` int(11) NOT NULL,
  `fk_gr_id` int(11) NOT NULL,
  PRIMARY KEY (`m2g_id`),
  KEY `fk_usr_id` (`fk_usr_id`),
  KEY `fk_gr_id` (`fk_gr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Структура таблицы `messages`
--

CREATE TABLE IF NOT EXISTS `messages` (
  `msg_id` int(11) NOT NULL AUTO_INCREMENT,
  `text` longtext NOT NULL,
  `create_date` datetime NOT NULL,
  `changed_date` datetime DEFAULT NULL,
  `fk_msg_prnt_id` int(11) DEFAULT NULL,
  `fk_msg_st_id` int(11) NOT NULL,
  `fk_sndr_usr_id` int(11) NOT NULL,
  `fk_sct_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`msg_id`),
  KEY `fk_msg_prnt_id` (`fk_msg_prnt_id`),
  KEY `fk_msg_st_id` (`fk_msg_st_id`),
  KEY `fk_sndr_usr_id` (`fk_sndr_usr_id`),
  KEY `fk_sct_id` (`fk_sct_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=22 ;

--
-- Дамп данных таблицы `messages`
--

INSERT INTO `messages` (`msg_id`, `text`, `create_date`, `changed_date`, `fk_msg_prnt_id`, `fk_msg_st_id`, `fk_sndr_usr_id`, `fk_sct_id`) VALUES
(2, 'First msg :)', '2012-04-07 00:00:00', NULL, NULL, 1, 3, NULL),
(3, 'second', '2012-04-07 00:00:01', NULL, 2, 1, 3, 2),
(7, 'Hi!', '2012-04-07 23:45:03', NULL, 2, 1, 6, NULL),
(8, 'jiji', '2012-04-07 23:55:16', NULL, 2, 1, 6, NULL),
(9, 'second', '2012-04-08 00:24:54', NULL, NULL, 1, 6, NULL),
(10, 'Do you like Python?', '2012-04-08 00:26:04', NULL, NULL, 1, 6, 5),
(11, 'Yes, of course', '2012-04-08 00:26:20', NULL, 10, 1, 6, 5),
(12, 'hi guis', '2012-04-08 21:13:26', NULL, NULL, 1, 9, NULL),
(13, '34679', '2012-04-08 21:13:33', NULL, 12, 1, 9, NULL),
(14, '4579', '2012-04-08 21:13:37', NULL, 12, 1, 9, NULL),
(15, 'iyiyh', '2012-04-08 21:13:58', NULL, NULL, 1, 9, 3),
(16, '345678\r\n', '2012-04-10 13:02:20', NULL, NULL, 1, 10, 2),
(17, 'First Message\r\n', '2012-04-10 13:02:32', NULL, 16, 1, 10, 2),
(18, '345879', '2012-04-10 13:02:39', NULL, 16, 1, 10, 2),
(19, '23456789', '2012-04-10 16:33:27', NULL, 2, 1, 11, NULL),
(20, 'hello world', '2012-04-10 17:04:26', NULL, NULL, 1, 13, 3),
(21, 'hello python', '2012-04-10 17:04:56', NULL, 20, 1, 13, 3);

-- --------------------------------------------------------

--
-- Структура таблицы `message_states`
--

CREATE TABLE IF NOT EXISTS `message_states` (
  `msg_st_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`msg_st_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Дамп данных таблицы `message_states`
--

INSERT INTO `message_states` (`msg_st_id`, `name`) VALUES
(1, 'verified'),
(2, 'nonverified'),
(3, 'deleted');

-- --------------------------------------------------------

--
-- Структура таблицы `rules`
--

CREATE TABLE IF NOT EXISTS `rules` (
  `rl_id` int(11) NOT NULL AUTO_INCREMENT,
  `text` varchar(255) NOT NULL,
  PRIMARY KEY (`rl_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Структура таблицы `sections`
--

CREATE TABLE IF NOT EXISTS `sections` (
  `sct_id` int(11) NOT NULL AUTO_INCREMENT,
  `sct_name` varchar(255) NOT NULL,
  `description` text,
  `create_date` datetime NOT NULL,
  `fk_sct_prnt_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`sct_id`),
  KEY `fk_sct_prnt_id` (`fk_sct_prnt_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Дамп данных таблицы `sections`
--

INSERT INTO `sections` (`sct_id`, `sct_name`, `description`, `create_date`, `fk_sct_prnt_id`) VALUES
(2, 'Others', 'Section about all', '2012-04-07 00:00:00', NULL),
(3, 'Tech Section', 'Techincal support', '2012-04-07 00:00:00', NULL),
(4, 'PyBoard support', NULL, '2012-04-07 00:00:00', 3),
(5, 'Python', 'About Python', '2012-04-07 00:00:00', 3);

-- --------------------------------------------------------

--
-- Структура таблицы `sessions`
--

CREATE TABLE IF NOT EXISTS `sessions` (
  `sssn_id` int(11) NOT NULL AUTO_INCREMENT,
  `sid` int(11) NOT NULL,
  `fk_user_id` int(11) DEFAULT NULL,
  `last_active` datetime NOT NULL,
  PRIMARY KEY (`sssn_id`),
  UNIQUE KEY `sid` (`sid`),
  KEY `fk_user_id` (`fk_user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Структура таблицы `settings`
--

CREATE TABLE IF NOT EXISTS `settings` (
  `stngs_id` int(11) NOT NULL AUTO_INCREMENT,
  `text` longtext NOT NULL,
  `st_key` varchar(255) NOT NULL,
  PRIMARY KEY (`stngs_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Дамп данных таблицы `settings`
--

INSERT INTO `settings` (`stngs_id`, `text`, `st_key`) VALUES
(3, 'showsection', 'defaultaction'),
(2, 'Daiver''s Forum', 'ForumName');

-- --------------------------------------------------------

--
-- Структура таблицы `users`
--

CREATE TABLE IF NOT EXISTS `users` (
  `users_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `passwdhash` varchar(255) DEFAULT NULL,
  `tmphash` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `avatar` varchar(255) DEFAULT NULL,
  `fk_gndr_id` int(11) NOT NULL,
  `fk_usr_st_id` int(11) DEFAULT NULL,
  `fk_cntr_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`users_id`),
  KEY `fk_gndr_id` (`fk_gndr_id`),
  KEY `fk_usr_st_id` (`fk_usr_st_id`),
  KEY `fk_cntr_id` (`fk_cntr_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=15 ;

--
-- Дамп данных таблицы `users`
--

INSERT INTO `users` (`users_id`, `name`, `passwdhash`, `tmphash`, `email`, `avatar`, `fk_gndr_id`, `fk_usr_st_id`, `fk_cntr_id`) VALUES
(3, 'Daiver', '0', '012d1ccf70c63a4bbb745d6f23a1537be1fc14b1', 'ra22341@ya.ru', NULL, 1, NULL, NULL),
(4, 'user', 'pass', '012d1ccf70c63a4bbb745d6f23a1537be1fc14b1', 'ya@ya.ru', NULL, 1, 1, NULL),
(6, 'admin', 'ad87109bfff0765f4dd8cf4943b04d16a4070fea', '012d1ccf70c63a4bbb745d6f23a1537be1fc14b1', 'empty', NULL, 1, 1, NULL),
(8, 'dark', '5f6955d227a320c7f1f6c7da2a6d96a851a8118f', '012d1ccf70c63a4bbb745d6f23a1537be1fc14b1', '890', NULL, 1, 1, NULL),
(9, 'lexa', '8cb2237d0679ca88db6464eac60da96345513964', '012d1ccf70c63a4bbb745d6f23a1537be1fc14b1', 'lexa', NULL, 1, 1, NULL),
(10, 'One', '40bd001563085fc35165329ea1ff5c5ecbdbbeef', '012d1ccf70c63a4bbb745d6f23a1537be1fc14b1', '123', NULL, 1, 1, NULL),
(11, 'sasha', '40bd001563085fc35165329ea1ff5c5ecbdbbeef', '012d1ccf70c63a4bbb745d6f23a1537be1fc14b1', '85852585285', NULL, 1, 1, NULL),
(12, 'login', '30274c47903bd1bac7633bbf09743149ebab805f', '012d1ccf70c63a4bbb745d6f23a1537be1fc14b1', 'ff@hotmail.com', NULL, 2, 1, NULL),
(13, 'fl', 'd0cf1ef21f0ce65584e2453a3fb427f6591adca8', '012d1ccf70c63a4bbb745d6f23a1537be1fc14b1', 'fl@fl.com', NULL, 1, 1, NULL),
(14, 'logina', '356a192b7913b04c54574d18c28d46e6395428ab', '012d1ccf70c63a4bbb745d6f23a1537be1fc14b1', 'vjnkvnskjsvnk', NULL, 2, 1, NULL);

-- --------------------------------------------------------

--
-- Структура таблицы `user_states`
--

CREATE TABLE IF NOT EXISTS `user_states` (
  `st_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`st_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Дамп данных таблицы `user_states`
--

INSERT INTO `user_states` (`st_id`, `name`) VALUES
(1, 'verified'),
(2, 'nonverified'),
(3, 'banned'),
(4, 'deleted');

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `g2r`
--
ALTER TABLE `g2r`
  ADD CONSTRAINT `g2r_ibfk_3` FOREIGN KEY (`fk_rl_id`) REFERENCES `rules` (`rl_id`),
  ADD CONSTRAINT `g2r_ibfk_4` FOREIGN KEY (`fk_gr_id`) REFERENCES `groups` (`gr_id`);

--
-- Ограничения внешнего ключа таблицы `groups`
--
ALTER TABLE `groups`
  ADD CONSTRAINT `groups_ibfk_1` FOREIGN KEY (`fk_mstr_id`) REFERENCES `users` (`users_id`);

--
-- Ограничения внешнего ключа таблицы `member_group`
--
ALTER TABLE `member_group`
  ADD CONSTRAINT `member_group_ibfk_1` FOREIGN KEY (`fk_usr_id`) REFERENCES `users` (`users_id`),
  ADD CONSTRAINT `member_group_ibfk_2` FOREIGN KEY (`fk_gr_id`) REFERENCES `groups` (`gr_id`);

--
-- Ограничения внешнего ключа таблицы `messages`
--
ALTER TABLE `messages`
  ADD CONSTRAINT `messages_ibfk_3` FOREIGN KEY (`fk_msg_st_id`) REFERENCES `message_states` (`msg_st_id`),
  ADD CONSTRAINT `messages_ibfk_4` FOREIGN KEY (`fk_sndr_usr_id`) REFERENCES `users` (`users_id`),
  ADD CONSTRAINT `messages_ibfk_5` FOREIGN KEY (`fk_sct_id`) REFERENCES `sections` (`sct_id`);

--
-- Ограничения внешнего ключа таблицы `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `users_ibfk_3` FOREIGN KEY (`fk_gndr_id`) REFERENCES `genders` (`gndr_id`),
  ADD CONSTRAINT `users_ibfk_4` FOREIGN KEY (`fk_usr_st_id`) REFERENCES `user_states` (`st_id`),
  ADD CONSTRAINT `users_ibfk_5` FOREIGN KEY (`fk_cntr_id`) REFERENCES `countries` (`cntr_id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
