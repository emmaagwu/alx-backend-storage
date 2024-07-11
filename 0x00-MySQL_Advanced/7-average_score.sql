-- SQL script to create a stored procedure to compute and store the average score only if not already done

-- Drop the stored procedure if it already exists
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

-- Create a stored procedure to compute and store the average score for a student

DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser (
    IN input_user_id INT
)
BEGIN
    DECLARE avg_score FLOAT;
    DECLARE current_avg FLOAT;
    
    -- Calculate the average score for the given user
    SELECT AVG(score) INTO avg_score
    FROM corrections
    WHERE user_id = input_user_id;
    
    -- Get the current average score from the users table
    SELECT average_score INTO current_avg
    FROM users
    WHERE id = input_user_id;
    
    -- Check if the average score needs to be updated
    IF avg_score <> current_avg THEN
        -- Update the average_score in the users table only if it's different
        UPDATE users
        SET average_score = avg_score
        WHERE id = input_user_id;
    END IF;
END//

DELIMITER ;
