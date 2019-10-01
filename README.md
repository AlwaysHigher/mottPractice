# mottPractice

***********   Library USED   ***********

pandas: https://pandas.pydata.org/

***********   How to run   ***********

1. Open the mottPractice.py in your preferred editor. 

2. Set up your file root at line 4 (accumRainfall.csv). Or make sure this file saved under same directory as source csv file.

3. Compile and run the file

***********   Notes   ***********

1. According to the unixdate time, it seems the data is not captured for one hour period of time. In order to complete the questions, I will assume the data is recorded at regular intervals 60 minute. 

2. Time zone is using UTC instead of EDT(where Pennsylvania based) as it won't affect the result this time.

3. According to "Twenty-Four Hour Rainfall Extreme Events" (https://climate.met.psu.edu/features/rainextreme.php). The average extreme rain fall values in Pennsylvania history are about 2 - 4 inches, which about 5 - 10 cms. Based on the data provided, so I assume the unit is millimetre.

4. We can use pd.read_sql_table() method if the data source from a sql table. 

5. If new data comes in incrementally.
  
  a. Data from two different data sources and we don't want to save new data to database:
     Load both files into one data frame.
  b. Already have first bit data in database, also would like to have new data in the database:
     Insert new data to the existing table, then read whole table to dataframe.
  
 The new data should be merged with existing data together into the same data frame, and sorted by datatime. 
    
