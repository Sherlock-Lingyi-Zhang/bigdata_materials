
# Lab: Using HiveQL to Analyze an Advertising Campaign (solution)

## Step 1. Calculating Revenue and Profit

##### 1. which top three products has Dualcore sold more of than any other?

```sql

-- NOTE: Since we use a GROUP BY clause, Hive requires
-- that we include all selected fields in that grouping.
-- If we don't, Hive throws an error with a message like:
--
--    SemanticException [Error 10025]: Expression
--    not in GROUP BY key 'fieldname'
--

SELECT brand, name, COUNT(p.prod_id) AS sold
FROM products p
JOIN order_details d
ON (p.prod_id = d.prod_id)
GROUP BY brand, name, p.prod_id
ORDER BY sold DESC
LIMIT 3;
```

|brand|name|sold|
|--|--|--|
|Byteweasel|"Tablet PC (10 in. display, 64 GB)"|119801|
|Dualcore|8GB DDR3-1600 (PC3-12800) Dual Channel Desktop Memory Kit (2x4GB)|29053|
|Megachango|F Jack Male-to-Male Cable (12 in.)|14566|


##### 2. What was Dualcore’s total revenue in May, 2013? 


```sql
SELECT SUM(price) AS revenue
FROM products p
JOIN order_details d
ON (d.prod_id = p.prod_id)
JOIN orders o
ON (d.order_id = o.order_id)
WHERE YEAR(order_date) = 2013
  AND MONTH(order_date) = 05;
-- Answer: 3206820724
```

##### 3. What was Dualcore’s gross profit (sales price minus cost) in May, 2013? 

```sql
SELECT SUM(price - cost) AS profit
FROM products p
JOIN order_details d
ON (d.prod_id = p.prod_id)
JOIN orders o
ON (d.order_id = o.order_id)
WHERE YEAR(order_date) = 2013
  AND MONTH(order_date) = 05;

-- Answer: 3206820724
```

##### 4. Rewrite the gross profit query to format the value in dollars and cents (e.g., \$2000000.00). 

```sql
SELECT PRINTF("$%.2f", SUM(price - cost) / 100) AS profit
FROM products p
JOIN order_details d
ON (d.prod_id = p.prod_id)
JOIN orders o
ON (d.order_id = o.order_id)
WHERE YEAR(order_date) = 2013
  AND MONTH(order_date) = 05;

-- Answer: 3206820724
```

## Step #2. Show Per-Month Sales Before and After Campaign
```sql
SELECT substr(order_date,1,7) as year_date
, count(*) as orders FROM orders 
where substr(order_date,1,7) between '2013-02' and '2013-05'
group by substr(order_date,1,7);
```

|year_date|orders|
|--|--|
|2013-02|76170|
|2013-03|84549|
|2013-04|87853|
|2013-05|115038|

**Answer**: Though we see an significant increase in sales in May, we may not conclude that the advertising campaign was affective because there could be seasonal effect or other events that cause this.

## Step #3: Count Advertised Product Sales by Month

For the advertised product:

```sql
select recent_orders.month, count(*) as num_orders 
from (SELECT order_id, substr(order_date,1,7) as month FROM orders 
where substr(order_date,1,7) between '2013-02' and '2013-05') 
recent_orders join (select order_id from order_details 
where prod_id = 1274348) tablets on recent_orders.order_id=tablets.order_id
group by recent_orders.month;
```

|recent_orders.month|num_orders|
|--|--|
|2013-02|3598|
|2013-03|3904|
|2013-04|4134|
|2013-05|49514|


For non-advertised products:

```sql
select recent_orders.month, count(*) as num_orders 
from (SELECT order_id, substr(order_date,1,7) as month FROM orders 
where substr(order_date,1,7) between '2013-02' and '2013-05') 
recent_orders join (select order_id from order_details 
where prod_id <> 1274348) tablets on recent_orders.order_id=tablets.order_id
group by recent_orders.month;

```

|recent_orders.month|num_orders|
|--|--|
|2013-02|160308|
|2013-03|177834|
|2013-04|184506|
|2013-05|198112|

**Answer**: These two sets of data give us more confidence in concluding that advertising campaign did drive sales increases. Essentially, what we obtain is similar to the result of a `quasi-experiment` where the control group is the non-advertised products and the treated group is the advertised product. If the treated group is singularly affected relative to the control group, we rule out the effects of time trends or other factors that impact all products. 

## Step #4: (Optional Hive Challenge) Calculate Average Order Size

The answer is: 5.2795250265129781

**Answer**: yes, people do tend to buy other products along with the promoted tablets.

Solution is available upon request.


*Lab credit: Cloudera, Inc.* 
