-- phpMyAdmin SQL Dump
-- version 3.4.5deb1
-- http://www.phpmyadmin.net
--
-- Хост: localhost
-- Время создания: Апр 07 2012 г., 13:11
-- Версия сервера: 5.1.61
-- Версия PHP: 5.3.6-13ubuntu3.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- База данных: `ForumDB`
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

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
  `fk_msg_prnt_id` int(11) NOT NULL,
  `fk_msg_st_id` int(11) NOT NULL,
  `fk_sndr_usr_id` int(11) NOT NULL,
  `fk_sct_id` int(11) NOT NULL,
  PRIMARY KEY (`msg_id`),
  KEY `fk_msg_prnt_id` (`fk_msg_prnt_id`),
  KEY `fk_msg_st_id` (`fk_msg_st_id`),
  KEY `fk_sndr_usr_id` (`fk_sndr_usr_id`),
  KEY `fk_sct_id` (`fk_sct_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Структура таблицы `message_states`
--

CREATE TABLE IF NOT EXISTS `message_states` (
  `msg_st_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`msg_st_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

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
  `create_date` datetime NOT NULL,
  `fk_sct_prnt_id` int(11) NOT NULL,
  PRIMARY KEY (`sct_id`),
  KEY `fk_sct_prnt_id` (`fk_sct_prnt_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Структура таблицы `settings`
--

CREATE TABLE IF NOT EXISTS `settings` (
  `stngs_id` int(11) NOT NULL AUTO_INCREMENT,
  `text` longtext NOT NULL,
  `st_key` varchar(255) NOT NULL,
  PRIMARY KEY (`stngs_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Дамп данных таблицы `settings`
--

INSERT INTO `settings` (`stngs_id`, `text`, `st_key`) VALUES
(1, 'Daiver''s Forum', 'ForumName');

-- --------------------------------------------------------

--
-- Структура таблицы `users`
--

CREATE TABLE IF NOT EXISTS `users` (
  `users_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `avatar` varchar(255) DEFAULT NULL,
  `fk_gndr_id` int(11) NOT NULL,
  `fk_usr_st_id` int(11) NOT NULL,
  `fk_cntr_id` int(11) NOT NULL,
  PRIMARY KEY (`users_id`),
  KEY `fk_gndr_id` (`fk_gndr_id`),
  KEY `fk_usr_st_id` (`fk_usr_st_id`),
  KEY `fk_cntr_id` (`fk_cntr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Структура таблицы `user_states`
--

CREATE TABLE IF NOT EXISTS `user_states` (
  `st_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`st_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

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
  ADD CONSTRAINT `messages_ibfk_5` FOREIGN KEY (`fk_sct_id`) REFERENCES `sections` (`sct_id`),
  ADD CONSTRAINT `messages_ibfk_3` FOREIGN KEY (`fk_msg_st_id`) REFERENCES `message_states` (`msg_st_id`),
  ADD CONSTRAINT `messages_ibfk_4` FOREIGN KEY (`fk_sndr_usr_id`) REFERENCES `users` (`users_id`);

--
-- Ограничения внешнего ключа таблицы `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `users_ibfk_5` FOREIGN KEY (`fk_cntr_id`) REFERENCES `countries` (`cntr_id`),
  ADD CONSTRAINT `users_ibfk_3` FOREIGN KEY (`fk_gndr_id`) REFERENCES `genders` (`gndr_id`),
  ADD CONSTRAINT `users_ibfk_4` FOREIGN KEY (`fk_usr_st_id`) REFERENCES `user_states` (`st_id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
