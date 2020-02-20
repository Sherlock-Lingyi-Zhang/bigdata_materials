
# Lab 10: Text Analytics with Hive (solution)

**Lab Demonstration Video (Start from 4:44)**

<iframe src="https://www.youtube.com/embed/w3GmbL56ATg" width="560" height="315" frameborder="0" allowfullscreen="allowfullscreen" allow="autoplay; encrypted-media"></iframe>
*This lab was recorded earlier and some of it no longer corresponds exactly to our latest lab instruction. Please start from 4:44*

1. find the five most common bigrams. 
```sql
SELECT EXPLODE(NGRAMS(SENTENCES(LOWER(message)), 2, 5))
AS bigrams
FROM ratings
WHERE prod_id = 1274673;
```
2. Find the five most common  _trigrams_. 
```sql
SELECT EXPLODE(NGRAMS(SENTENCES(LOWER(message)), 3, 5))
AS bigrams
FROM ratings
WHERE prod_id = 1274673;
```
3. look at a few comments that contain "ten times more": 
```sql
SELECT message
FROM ratings
WHERE prod_id = 1274673
AND message LIKE '%ten times more%'
LIMIT 3;
```
4. Write and execute a query that will find all distinct comments containing the word "red" that are associated with product ID 1274673. 
```sql
SELECT message
FROM ratings
WHERE prod_id = 1274673
AND message LIKE '%red%'
LIMIT 3;
```
5. Write and run a query that will display the record for product ID  1274673  in the `products` table. 
```sql
SELECT *
FROM products
WHERE prod_id = 1274673;
```
6. Run a query to identify similar products("16GB USB Flash Drive"): 
```sql
SELECT *
FROM products
WHERE name LIKE '%16 GB USB Flash Drive%'
AND brand='Orion';
```
