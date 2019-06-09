# %%
import pandas as pd
#!cat lec25.csv

dframe = pd.read_csv('lec25.csv')
dframe

# header無し
dframe = pd.read_csv('lec25.csv', header=None)
dframe

