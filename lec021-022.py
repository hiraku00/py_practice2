# %%
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

#------------------
# lec021
#------------------
ser1 = Series(range(3), index=['C','A','B'])
ser1

ser1.sort_index()
ser1

ser1.order()

from numpy.random import randn

ser2 = Series(randn(10))
ser2

ser2.rank()
ser2

ser2.sort()
ser2

ser2.rank()

#------------------
# lec022
#------------------
arr = np.array([[1,2,np.nan], [np.nan,3,4]])
arr

dframe1 = DataFrame(arr, index=['A','B'], columns=['One','Two','Three'])
dframe1

# columnで集約
dframe1.sum()
# Rowで集約
dframe1.sum(axis=1)

dframe1.min()

dframe1.describe()

#-------
# 株価データ

import pandas.io.data as pdweb
import datetime

prices = pdweb.get_data_yahoo(['CVX','XOM','BP'],
                                start=datatime.datetime(2010,1,1),
                                end=datetime.datetime(2013,1,1))['Adj Close']
