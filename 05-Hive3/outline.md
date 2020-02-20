# Text Analytics with Hive

## Learning Objectives

Hive provides rich functions for analyzing textual data including both unstructured data (e.g. online reviews) and semi-structured textual data (e.g. web logs). These include both standard string functions, regular expression functions, and functions that are useful for computing n-grams. 

In this section, you will learn:

- How to use Hive's string functions
- How to use regular expressions in Hive
- How to load text files that does not use consistent delimiters
- How to obtain n-grams as part of sentiment analysis
- How to estimate how often words or phrases occur in text
- How to handle JSON-formatted data
- How to query JSON-encoded fields with Hive
- How to use TRANSFORM for custom record processing
- How to add support for a User Deﬁned Function (UDF)

---

## Class 1: Hive Text Analytics

**[slides](Hive5-HiveText.pdf) / [print version](Hive5-HiveText-Print.pdf)**

### Pre-class Activities

Watch the following clips on this topic, then complete the **self-assessment 10**.

**Hive Text Functions (11:13)**

<iframe width="560" height="315" src="https://www.youtube.com/embed/hHvwdrdb0AU" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

**Regular Expression (23:02)**

<iframe width="560" height="315" src="https://www.youtube.com/embed/gRa81_kruBw" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>


**SerDes (8:32)**

<iframe width="560" height="315" src="https://www.youtube.com/embed/t_hb1LmMCaU" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

--

**Sentiment Analysis and N-grams (6:28)**

<iframe width="560" height="315" src="https://www.youtube.com/embed/8Uomf_apzeU" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>


- Complete **self-assessment 10** on Canvas.

### In Class

- discuss regex, sentiment analysis.

- Complete [Lab 10: Text Analytics with Hive](lab10-text.md): you will use Hive's text processing functions to analyze customers' comments and product ratings.
    + [solution](lab10-text-solution.md)

- Complete [Lab 11: Log Data Analysis with Hive](lab11-weblog.md): this lab lets you use regular expression to analyze web log data.
    + [solution](lab11-weblog-solution.md)

---

## Class 2: Extending Hive (JSON, Custom Scripts, and UDFs)

**[slides](Hive6-ExtendingHive.pdf) / [print version](Hive6-ExtendingHive-Print.pdf)**

### Pre-work

Watch the following clips on this topic, then complete the **self-assessment 11**.

**JSON, Custom Scripts, and UDF (25:04)**

<iframe width="560" height="315" src="https://www.youtube.com/embed/iomgvmi9lTw" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

- Complete **self-assessment 11** on Canvas.

### In Class

- choice of SerDes

- Complete [Lab 12: Work with JSON documents and External Scripts in Hive](lab12-extension.md)
    + [solution](lab12-extension-solution.md)

## Assignments

- **Homework Assignment 3**

## Resources

### Hive Text Analytics

- [Hive Documentation on String-based Functions](https://cwiki.apache.org/confluence/display/Hive/LanguageManual+UDF#LanguageManualUDF-StringFunctions) 
- [Hive Lauangage Manual - SerDe](https://cwiki.apache.org/confluence/display/Hive/SerDe#SerDe-Built-inSerDes)
- Example of Hive-based Sentiment Analysis:[https://acadgild.com/blog/sentiment-analysis-on-tweets-with-apache-hive-using-afinn-dictionary](https://acadgild.com/blog/sentiment-analysis-on-tweets-with-apache-hive-using-afinn-dictionary) 
- [Statistics and Data Mining in Hive](https://cwiki.apache.org/confluence/display/Hive/StatisticsAndDataMining)


### Regular Expression

- Test your Regular Expression online: [http://myregexp.com/](http://myregexp.com/) 
- Learn Regular Expression - Step by  Step: [https://regexone.com/](http://myregexp.com/) 
- Regular Expression - Quick Start:[http://www.regular-expressions.info/quickstart.html](http://www.regular-expressions.info/quickstart.html)
- Regular Expression - Comprehensive Reading:[https://www.regular-expressions.info/tutorial.html](https://www.regular-expressions.info/tutorial.html) 
- [Regex Cheat Sheet (pdf) - AddedByets.com](regular-expressions-cheat-sheet-v2.pdf)
- Quick-Start: Regex Cheat Sheet(online):[http://www.rexegg.com/regex-quickstart.html](http://www.rexegg.com/regex-quickstart.html)