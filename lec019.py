# %% 

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

ser1 = Series(np.arange(3), index=['A', 'B', 'C'])
ser1 = 2*ser1

ser1

ser1['B']
ser1[1]
ser1[0:3]
ser1[['A', 'B']]
ser1[ser1>3]
ser1[ser1>3] = 10
ser1


