

# Supermarket Data Analysis Project for Company XYZ

   Company XYZ owns a supermarket chain across the country. Each major branch, located in 3 cities across the country, recorded sales         information for 3 months, to help the company understand sales trends and determine its growth, as the rise of supermarkets competition     is seen to increase.
   
   The collected data was analyzed to derive useful insights to help the growth of the company.
   


   
# Project Steps

## Step 1 - Loading the Dataset
   In this step, I combined the dataset from each branch (3 branches) into one dataset for easy analysis. I wrote the syntaxes that read      multiple files from my current working directory and exported all to a CSV file after combining. 

## Step 2 - Data Exploration
   In this step, I explored the loaded dataset using some built-in Pandas function.

## Step 3 - Dealing with DateTime Features
   I observed that the `date` and `time` columns were not in the appropriate data type so I converted them to the appropriate datatypes        that is `datetime` datatype using the `to_datetime()` method. 
   
## Step 4 - Unique Values in Columns
   I got a list of the categorical columns in the dataset. I iterated through the columns and checked if each element was an object           datatype. 
   
## Step 5 - Aggregration with GroupBy
   I created a groupby object with the "City Column". Then I generated an aggregation function of the sum and mean.
   
## Step 6 - Data Visualization
   In this section, I provided answers to some questions by generating charts and making use of different plotting styles. I utilized the     `Seaborn visualization` library to generate the plots. For all visualizations, I included a chart title by using the seaborn `set_title`   method.



# Insights

   I was able to uncover the following insights:
   
   i. Port Harcourt had the highest gross income. It also had the highest total income.
   
   ii. The higest Gross Margin Percentage came from Lagos which means that the Lagos Branch gave the highest profit. 
   - Therefore, the stock in Lagos can be increased since Lagos gives the highest profitablity.
   
   iii. Port Harcourt had the highest mean Rating while Abuja had the lowest. 
   - Also, Port Harcourt had the highest tax in total.
   
   iv. Payment by Cash and Epay had the lead while card payment had lesser people engaging it.
   
   v. The highest profit came from Payment by Epay.
   
   vi. The highest tax on a single purchase is on Card Payment, while the minimum is on payment by cash. 
       ALSO:
       - Payment by cash never had a maximum rating (of 10). 
       - The highest total gross income for the three modes of payment came from payment by cash. 
       - The maximum gross income from a single customer came from payment by card, while the minimum came from payment by cash.

   vii. The greatest portion of the total income came from payment by Cash, while the lowest  came from Card payment.

   - However, the least total income from a single Payment came through Cash while the highest came by Card, followed by Epay.
   - From here, it will be better for a customer willing to buy goods that have low price to use cash, while high price goods should be        bought using card or Epay. But payment by Epay will be the better since there is lesser tax on it.

   viii. Also, Port Harcourt had the highest tax in total.
   
   viii. The mean Rating for both and female was almost the same.

   ix. Purchase by Females accounted for the larger part of the Total Income. Therefore, goods that Females buy can be increased on the        stock.
   
   x. The highest profit of the company came from Fashion Accessories, followed by Food and Beverages. The lowest came from Health and             Beauty. Therefore, improvement should be made on how Fashion Accessories & Food and Beverages are sold since they yield the highest         profits, while for Health and Beauty, more market research should be done on this good to know why it pulls less demand. More               advertisement can be done too to ensure that people are more aware of its availability.
   
   xi. Cash payment was preferred for electronic goods most likely because of testing.
   
   ALSO:
   1. The Customers = 1000
   2. Total females = 501
   3. Total males = 499
   4. Min rating = 4
   5. Max rating = 10
   6. Average Rating = 7
   7. Best Average rating comes from Food and Beverages
   8. Max Average Gross Income from Home and Lifestyle
   9. Min Average Gross Income from Fashion Accessories
   10. Maximum customers buy 10 quantities
   11. Maximum number of customers do E-payment and the least use card payment
   12. Maximum number of customers come from Lagos and the least come from PortHarcourt
   13. Max sales for females came from Fashion accessories
   14. Max sales for males came from Health and Beauty Accessories 

   



# Future Work

 In the future, I will try to:

 1. Work towards getting more external data to make the analysis more insightful.




# Standout Section


  1. I plotted different barplots to understand the realtionship between a number of variables.
  2. I used a heatmap to undrstand the correlation between the variables.




# Executive Summary

   The goal of the project was to analyze Supermarket data from Company XYZ, which has 3 supermarket chains across the country. The data was for about 3 months, and the aim of the analysis was to determine sales trend and upscale growth, especially because competition was on the increase. 
   
   Insights were generated from the analysis which helped to ascertain numerous factors that were responsible for how the sales had been and how to improve on the sales to make Company XYZ more profitable.
   
   With the aid of beautiful visualization plots and cahrts, useful insights were uncovered, and significant in
