/*
Powerful queries
*/

/* sum the number of payments for each user */
SELECT customer_name, count(*) AS number_of_payments
FROM payments
GROUP BY customer_name
ORDER BY number_of_payments DESC;

/* sum the payment amounts for each month */
SELECT sum(amount) as sum_of_payments, extract(year from processed_at) as year, extract(month from processed_at) as month
FROM payments
GROUP BY month, year
ORDER BY sum_of_payments DESC;

/* sum the payment amounts for each month for each user */
SELECT customer_name, sum(amount) as sum_of_payments, extract(year from processed_at) as year, extract(month from processed_at) as month
FROM payments
GROUP BY customer_name, month, year
ORDER BY customer_name DESC;

/* Find the largest single-user payments for each month */
SELECT max(amount) as max_amount, year, month
FROM ( SELECT customer_name, sum(amount) as amount, extract(year from processed_at) as year, extract(month from processed_at) as month
FROM payments GROUP BY customer_name, month, year) as monthly_sums
GROUP BY year, month;

/* Transactions */
/* Transfer 100 from Clement to Antoine */
START TRANSACTION;
UPDATE balances SET balance = balance - 100 where username = 'clement';
UPDATE balances SET balance = balance + 100 where username = 'antoine';
COMMIT;


/* Find 10 largest ints */
SELECT * from large_table ORDER BY random_int DESC LIMIT 10;


/* Create and index on the ints in the table */
CREATE INDEX large_table_random_int on large_table(random_int);