import pandas as pd
from datetime import datetime

df = pd.read_csv ("accumRainfall.csv", sep = '\t', encoding='utf-16')
df['unixdatetime'] = pd.to_datetime(df['unixdatetime'],unit='s')

#df['unixdatetime'].index = pd.DatetimeIndex(df['unixdatetime'].index).tz_localize('UTC').tz_convert('US/Eastern')

date_time = df['unixdatetime'].tolist()
value = df['value'].tolist()

def max_rainfall(l) :

    data = {}

    split = [l[i:i+46] for i in range(0, len(l), 1)]

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

print ('The accumulated rain fall is:', round(accumulate(value),2),'mm.')
print('Peak period starts after around', int(time_index/91*60) ,'mins, and the accumulated rain fall for the peak periold is:', round(peak_rain,2),'mm.')
