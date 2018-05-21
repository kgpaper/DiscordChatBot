# 투표개설 SQL


DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createVote`(
    IN p_vote_key VARCHAR(200),
    IN p_vote_manager VARCHAR(200),
    IN p_vote_subject VARCHAR(1000),
    IN p_vote_description VARCHAR(5000),
    IN p_vote_selection VARCHAR(5000),
    IN p_vote_anonymous INT,
    IN p_vote_duplicate INT,
    IN p_vote_deadline INT,
    IN p_vote_write_date INT,
    IN p_vote_people VARCHAR(5000)
)
BEGIN
      insert into votetest
        (
            vote_key,
            vote_manager,
            vote_subject,
            vote_description,
            vote_selection,
            vote_anonymous,
            vote_duplicate,
            vote_deadline,
            vote_write_date,
            vote_people
        )
        values
        (
            p_vote_key,
            p_vote_manager,
            p_vote_subject,
            p_vote_description,
            p_vote_selection,
            p_vote_anonymous,
            p_vote_duplicate,
            p_vote_deadline,
            p_vote_write_date,
            p_vote_people
        );
END$$
DELIMITER ;