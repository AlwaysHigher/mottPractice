import pandas as pd
from datetime import datetime

df = pd.read_csv ("accumRainfall.csv", sep = '\t', encoding='utf-16')

try:
    date_col_name = input ('Please enter the column name for datetime from the table:')
    value_col_name = input ('Please enter the column name for values from the table:')
    running_mins = int (input ('Please enter total running minute:'))
    peak_mins = int (input ('Please enter how long the peak period minute are:'))

    df[date_col_name] = pd.to_datetime(df[date_col_name],unit='s')
    date_time = df[date_col_name].tolist()
    value = df[value_col_name].tolist()
except KeyError:
    print('Please enter correct column name.')
    exit()
except ValueError:
    print('Please enter valid running time.')
    exit()

def de_accumulate(v,t) :
    da = t/len(v)
    return da

def max_rainfall(l,p,r) :

    data = {}

    try:
        array_len_index = int(r/p)
        split = [l[i:i+len(l)//array_len_index+1] for i in range(0, len(l), 1)]
    except ZeroDivisionError:
            print('Peak period must longer than total running minute.')
            exit()

    for i in split:
        j = sum(i)
        k = split.index(i)
        data[k] = j

    max_value = max(data.items(), key=lambda x : x[1])
    max_index = max_value[0]
    peak_value = max_value[1]
    return max_index, peak_value

rain_time = round (de_accumulate(value, running_mins),2)

time_index, peak_rain = max_rainfall(value,peak_mins,running_mins)

print ('The de-accumulated values are:', value)
print ('The average rain time for each records are', rain_time,'minute.')
print('Peak period starts after around', int(round(time_index*rain_time)) ,'mins, and the accumulated rain fall for the peak periold is:', round(peak_rain,2),'mm.')
