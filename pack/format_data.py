


def format_data(data):
    import pandas as pd
    import numpy as np
    import time
    from datetime import datetime
    import dask
    import dask.dataframe as dd
    data['Date1'] = dd.to_datetime(data['Date-Time'])
    data['hour'] = dd.to_datetime(data['Date-Time'], format='%H:%M').dt.hour
    data['minute'] = dd.to_datetime(data['Date-Time'], format='%H:%M').dt.minute
    data['second'] = dd.to_datetime(data['Date-Time'], format='%H:%M').dt.second
    data['date'] = dd.to_datetime(data['Date-Time']) 
    data['date1'] = data['date'].dt.date
    return data