USE testDB;
select count(num1),sum(num2) from rand_numbers group by num4 order by count(num3) DESC;
