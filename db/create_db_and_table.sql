CREATE DATABASE votetest DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
CREATE TABLE `vote_test` (
  `vote_index` int(11) NOT NULL AUTO_INCREMENT,
  `vote_key` varchar(30) DEFAULT NULL,
  `vote_manager` varchar(45) DEFAULT NULL,
  `vote_subject` varchar(1000) DEFAULT NULL,
  `vote_description` varchar(5000) DEFAULT NULL,
  `vote_selection` varchar(5000) DEFAULT NULL,
  `vote_anonymous` int(2) DEFAULT NULL,
  `vote_duplicate` int(2) DEFAULT NULL,
  `vote_deadline` int(11) DEFAULT NULL,
  `vote_write_date` int(11) DEFAULT NULL,
  `vote_people` varchar(5000) DEFAULT NULL,
  PRIMARY KEY (`vote_index`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
