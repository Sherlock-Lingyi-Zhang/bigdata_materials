
# Lab 10: Text Analytics with Hive 

**Source code**: [right click on this link](https://github.umn.edu/deliu/bigdata19/blob/master/05-Hive3/lab10-text/lab10-text.md), open it in a new tab, then right click on the Raw button, save link as, change the file extension to ".md", then save.

**In this lab, you will use Hive s text processing features to analyze customers' comments and product ratings. You will uncover problems and propose potential solutions.**

**IMPORTANT**: This exercise builds on outputs in Lab 8. If you were unable to complete any previous exercise or think you may have made a mistake, run the following command to prepare for this exercise before continuing: 

```bash
$ ~/scripts/analyst/catchup.sh
# then choose 8 (Gaining Insight with Sentiment Analysis) 
```

**Files used in this lab**
- (Hive table) `dualcore.products` 
- (Hive table) `dualcore.ratings` (produced in Lab 8)

## Analyze Rating Comments

Customer ratings and feedback are great sources of information for both customers and retailers like Dualcore. 

However, customer comments are typically free-form text and must be handled differently. Fortunately, Hive provides extensive support for text processing. 

We observed earlier that customers are very dissatisfied with one of the products we sell. Although numeric ratings can help identify  _which_  product that is, they don't tell us  _why_ customers don't like the product. Although we could simply read through all the comments associated with that product to learn this information, that approach doesn't scale. Next, you will use Hive's text processing support to analyze the comments. 

1. Write a query that normalizes all comments on that product to lowercase, breaks them into individual words using the `SENTENCES` function, passes those to the `NGRAMS` function to find the five most common bigrams (two-word combinations), and then use `EXPLODE` to break up ngrams outcomes into separate rows. 

    ```sql
    SELECT ____
    AS bigrams
    FROM ratings
    WHERE prod_id = 1274673;
    ```
2. Most of these words are too common to provide much insight, though the word "expensive" does stand out in the list. Modify the previous query to find the five most common  _trigrams_  (three-word combinations), and then run that query in Hive. 

3. Among the patterns you see in the result is the phrase "ten times more." This might be related to the complaints that the product is too expensive. Now that you've identified a specific phrase, look at a few comments that contain it by running this query: 

    ```sql
    SELECT message
    FROM ratings
    WHERE prod_id = 1274673
    AND message LIKE '%ten times more%'
    LIMIT 3;
    ```

    You should see three comments that say, "Why does the red one cost ten times more than the others?" 

4. We can infer that customers are complaining about the price of this item, but the comment alone doesn't provide enough detail. One of the words ("red") in that comment was also found in the list of trigrams from the earlier query.  Write and execute a query that will find all distinct comments containing the word "red" that are associated with product ID 1274673. 

5. The previous step should have displayed two comments: 
    + "What is so special about red?" 
    + "Why does the red one cost ten times more than the others?" 

    The second comment implies that this product is overpriced relative to similar products. Write and run a query that will display the record for product ID  1274673  in the `products` table. 

6. Your query should have shown that the product was a "16GB USB Flash Drive (Red)" from the "Orion" brand. Next, run this query to identify similar products: 

    ```sql
    SELECT *
    FROM products
    WHERE name LIKE '%16 GB USB Flash Drive%'
    AND brand='Orion';
    ```

    The query results show that we have three almost identical products, but the product with the negative reviews (the red one) costs about ten times as much as the others, just as some of the comments said.  

    Based on the cost and price columns, it appears that doing text processing on the product ratings has helped us uncover a pricing error. 

**This is the end of the Lab**

*Lab Credit: Cloudera, Inc.*