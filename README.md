# mottPractice

***********   Library USED   ***********

pandas: https://pandas.pydata.org/

***********   How to run   ***********

1. Open the mottPractice.py in your preferred editor. 

2. Set up your file root at line 4 (accumRainfall.csv). Or make sure this file saved under same directory as source csv file.

3. Compile and run the file

4. Four parameters are required to get the output for the questions:

      Please enter the column name for datetime from the table: unixdatetime
      Please enter the column name for values from the table: value
      Please enter total running minute:  60
      Please enter how long the peak period minute are: 30


***********   Notes   ***********

1. There are 91 lines of data in the original data source captured in different date and time, also, the total rain time are 60 minute. So I assume rain time will be the same for each record.

2. Time zone is using UTC instead of EDT(where Pennsylvania based) as it won't affect the result this time.

3. According to "Twenty-Four Hour Rainfall Extreme Events" (https://climate.met.psu.edu/features/rainextreme.php). The average extreme rain fall values in Pennsylvania history are about 2 - 4 inches per day, which about 5 - 10 cms. Based on the data provided, so I assume the unit is millimetre.

4. If new data comes in incrementally.Ideally, each line of the record will have a unique id in ascending order.The new data should be sorted and merged with existing data into the same data frame. 
