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

Part two was to give visual plots
- Visuals are given for first 5 questions
- Plots are missing for brand, cheapest gas station per region, and price change frequency due to lack of creativity

Task 2: define a business model
- Given in text file

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
- all input processing is pipelined for easier usage

Result:
Linear regression: mean squared error score for cross validation was 0.054527€ with a standard deviation of 0,010€
Tree regression:
- depth of 2: mean squared error score for cross validation was 0.058914€ with a standard deviation of 0,01102€
- depth of 8: mean squared error score for cross validation was 0.038280€ with a standard deviation of 0,00252€
- depth of 10: mean squared error score for cross validation was 0.0363371€ with a standard deviation of 0,00225€
- depth of 12: mean squared error score for cross validation was 0.035224€ with a standard deviation of 0,00261€
With the last step, the standard deviation increased a little bit, which could be the beginning of overfitting or just by chance

Task 4
- Used cross validation with the results given in Task 3
- Model can predict (DecisionTreeRegressor with depth of 12) prices with and accuracy of 0.035€ and a standard deviation of of 0.002€
- Prices can change hourly by up to 10%
- The cheapest brand (Mr Wash) is on average 7% cheaper than ARAL,  
- On Wednesday, Diesel is 1% cheaper than on Sunday
- The predictor uses these correlations for an accurate-enough prediction. The saving potetial is estimated to be more than 5% on average.  

Task 5
- Presentation slides given as powerpoint
