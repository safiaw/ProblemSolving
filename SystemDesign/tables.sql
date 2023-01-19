CREATE TABLE payments (
		customer_name VARCHAR(128),
		processed_at DATE,
		amount INT
		);

CREATE TABLE balances (
		username VARCHAR(128),
		balance INT
		);
		
CREATE TABLE large_table (
		random_int INT
		);
		
INSERT INTO payments (customer_name, processed_at, amount) VALUES 
                     ('clement', '2019-12-15', 10), 
					 ('antoine', '2020-01-01', 100), 
					 ('clement', '2020-01-02', 10),
					 ('antoine', '2020-01-02', 100),
					 ('antoine', '2019-01-03', 100),
					 ('simon', '2020-02-05', 1000),
					 ('antoine', '2020-02-01', 100),
					 ('clement', '2020-02-03', 10),
					 ('meghan', '2020-01-12', 80),
					 ('meghan', '2020-01-13', 70),
					 ('meghan', '2020-01-14', 90),
					 ('alex', '2019-12-11', 10),
					 ('clement', '2020-02-01', 10),
					 ('marli', '2020-01-18', 10),
					 ('alex', '2019-12-15', 10),
					 ('marli', '2020-01-25', 10),
					 ('marli', '2020-02-02', 10);
					 
INSERT INTO balances (username, balance) VALUES
					 ('antoine',10),
					 ('clement',1000);
		

BEGIN
			DECLARE startindex INT DEFAULT 0;
			DECLARE endindex INT DEFAULT 50000000;
			WHILE startindex < endindex DO
			
               INSERT large_table (random_int) SELECT FLOOR((RAND() * 1000000000)+1);
			   SET startindex=startindex+1;
			END WHILE;
END
