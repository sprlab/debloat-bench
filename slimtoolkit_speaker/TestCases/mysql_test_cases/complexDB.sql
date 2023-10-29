USE testDB;
CREATE TABLE rand_numbers (
    num1 INT NOT NULL,
    num2 INT NOT NULL,
    num3 INT NOT NULL,
    num4 INT NOT NULL
);


drop procedure if exists doWhile;
DELIMITER //  
CREATE PROCEDURE doWhile()   
BEGIN
DECLARE i INT DEFAULT 0; 
WHILE (i <= 200) DO
    INSERT INTO rand_numbers (num1,num2,num3,num4) values (1,1,1,1);
    SET i = i+1;
END WHILE;
END;
//

CALL doWhile();

