# Introduction-to-Data-Science

Mandatory Exercise

Task 1: understanding data
Questions Given: 
- How many locations are in the data
- How many brands?
- What min, max price for each gasoline type and month
-
Own questions:
- Find Average Cheapest Gas Station for every Autobahn
- Find cheapest Weekday and Daytime
- Find Cheapest Brand
- Find Cheapest Gas Station for each region (where region == first three digits of region code)
- How often do prices change (count distinct prices for each gas station and build average)

Part two was to give visual plots (still to be done)

Task 2: define a business model

Task 3: develop a predictive model
1. Simpeler one:
predicts price for given longitude, latitude and day of week

Models:
- models tried were linear regression and decision tree regression

Data preparation:
- build datafram from SQL, extracting day of week and longitude/latitude and grouping them to calculate average diesel price for each group
- days of week was one-hot encoded
- longitude/latitude were standardized with StandardScaler()

Result:
Linear regression: mean squared error score for cross validation was 0.03935€ with a standard deviation of 0,00178€
Tree regression: mean squared error score for cross validation was 0.00810€ with a standard deviation of 0,00321€

2. Improved one:
predicts price for given region, year, month, day of week, hour and brand

Models:
- models tried were linear regression and decision tree regression

Data preparation:
- build datafram from SQL
- days of week was one-hot encoded
- brands were categorized into 17 most popular brands and 1 category for "others" , then one-hot encoded
- region was chosen as first three digits from postal code
- hours were transformed with a sin() function
- numerical values were standardized with StandardScaler()

Result:
Linear regression: mean squared error score for cross validation was 0.054527€ with a standard deviation of 0,010€
Tree regression: pending

Task 4
-  to be done
Task 5
- presentation
