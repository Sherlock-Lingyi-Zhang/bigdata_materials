# Lab 13 - Using AWS EMR to Analyze Web Logs (Solution)

### Demonstration Video Part 1 - Starting EMR cluster

<iframe width="560" height="315" src="https://www.youtube.com/embed/H5sCajcbE74" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

### Demonstration Video Part 2 - Connect to the EMR Cluster

<iframe width="560" height="315" src="https://www.youtube.com/embed/XXP6DlKkhmk" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>



## Step 3

1\. Open Hue

2\. copy and run the query

3\. Let's find the number of rows in the table:

```sql
select count(*) from cloudfront_logs;
```

4\. copy and run the query

5\. copy and run the query

6\. Load the data (for '2014-07-05') into the external table from cloudfront_logs.

```sql
insert into csvexport select * from cloudfront_logs;
WHERE date_time = '2014-07-05';
```

## Appendix

1\. What is the distribution of traffic (number of visits) per hour of day? (hint use **substring** function on the **time** field to get hours)

```sql
select substring(Time,0,2) hour, count(*) as cnt 
from cloudfront_logs 
group by substring(Time,0,2);
```
```
14  2000
15  998
20  1998
Time taken: 27.111 seconds, Fetched: 3 row(s)
```

2\. What are the top 10 browsers used to access these websites?

```sql
select browser, count(*) cnt from cloudfront_logs 
group by browser order by cnt desc limit 10;
```
```
Lynx,889
Safari,875
Opera,835
Chrome,828
Firefox,795
IE,774
```

3\. What are the top 3 request IPs by total number of visits? what are their total bytes transmitted? (you can answer the two questions in one query)
```sql
select requestip, count(*) cnt, sum(bytes) as total_bytes 
from cloudfront_logs 
group by  requestip order by cnt desc limit 3;
```

```
requestip,cnt,total_bytes
10.0.0.15,4473,15364115
10.0.0.16,364,1158115
10.0.0.9,20,72387

```
