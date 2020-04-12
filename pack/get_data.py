import pandas as pd
import numpy as np
import time
from datetime import datetime
import dask
import dask.dataframe as dd


def import_data():
    import dask.dataframe as dd
    data=dd.read_csv(r'/Users/Yuxin/Desktop/github/practicepy.csv', parse_dates=[2], dtype={'#RIC':str,'Domain':str,'GMT Offset':int,
                                                               'Type':str,'Price':float,'Volume':float,
                                                               'Buyer ID ':float,'Bid Price':float,
                                                               'Bid Size':float,'Ask Price':float,
                                                               'Ask Size':float,'Qualifiers':str})
    return data



def format_data(data):

    data['Date1'] = dd.to_datetime(data['Date-Time'])
    data['hour'] = dd.to_datetime(data['Date-Time'], format='%H:%M').dt.hour
    data['minute'] = dd.to_datetime(data['Date-Time'], format='%H:%M').dt.minute
    data['second'] = dd.to_datetime(data['Date-Time'], format='%H:%M').dt.second
    data['date'] = dd.to_datetime(data['Date-Time']) 
    data['date1'] = data['date'].dt.date
    return data