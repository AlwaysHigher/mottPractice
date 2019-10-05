import pandas as pd
from datetime import datetime

df = pd.read_csv ("accumRainfall.csv", sep = '\t', encoding='utf-16')


try:
    date_col_name = input ('Please enter the column name for datetime from the table:')
    value_col_name = input ('Please enter the column name for values from the table:')
    running_mins = int (input ('Please enter total running minute:'))

    df[date_col_name] = pd.to_datetime(df[date_col_name],unit='s')
    date_time = df[date_col_name].tolist()
    value = df[value_col_name].tolist()
except KeyError:
    print('Please enter correct column name.')
    exit()
except ValueError:
    print('Please enter valid running time.')
    exit()



def max_rainfall(l) :

    data = {}

    split = [l[i:i+len(l)//2+1] for i in range(0, len(l), 1)]

    for i in split:
        j = sum(i)
        k = split.index(i)
        data[k] = j

    max_value = max(data.items(), key=lambda x : x[1])
    max_index = max_value[0]
    peak_value = max_value[1]
    return max_index, peak_value

def accumulate(i) :
    total = 0
    for v in i :
        total += v
    return total

time_index, peak_rain = max_rainfall(value)

#print ('The de-accumulated rain fall data are:', value)
print('Peak period starts after around', int(time_index/len(date_time)*running_mins) ,'mins, and the accumulated rain fall for the peak periold is:', round(peak_rain,2),'mm.')
