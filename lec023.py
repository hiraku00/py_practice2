# %%
#==========================
# lec023
#==========================
import numpy as np
from pandas import Series, DataFrame
import pandas as pd

data = Series(['one','two',np.nan,'four'])
data

data.isnull()

data.dropna()

dframe = DataFrame([[1,2,3], [np.nan,5,6], [7,np.nan,9], [np.nan,np.nan,np.nan]])
dframe

dframe.dropna()

dframe.dropna(how='all')

dframe.dropna(axis=1)


dframe2 = DataFrame([[1,2,3,np.nan],[2,np.nan,5,6],[np.nan,7,np.nan,9],[1,np.nan,np.nan,np.nan]])
dframe2

# 欠損値ではない値が2個以上
dframe2.dropna(thresh=2)
# 欠損値ではない値が3個以上
dframe2.dropna(thresh=3)
# 欠損値を別の値で埋める
dframe2.fillna(1)

dframe2
# 埋めるデータを指定
dframe2.fillna({0:0,1:1,2:2,3:3})

# inplace=Trueにすると、元のDataFrameを変更してくれます。
# dframe2 = dframe2.fillna(....)と同じ
dframe2 = dframe2.fillna(0, inplace=True)
dframe2

dframe2 = DataFrame([[1,2,3,np.nan],[2,np.nan,5,6],[np.nan,7,np.nan,9],[1,np.nan,np.nan,np.nan]])
dframe2
# dframe2 = dframe2.fillna(....)
dframe2


#==========================
# lec024 indexの階層構造
#==========================
from numpy.random import randn

ser = Series(np.random.randn(6), index=[[1,1,1,2,2,2], ['a','b','c','a','b','c']])
ser

ser.index

ser[1]
ser[2]

ser
ser[:,'a']

dframe = ser.unstack()
dframe

dframe.unstack()
# 先に列名が来ているので、転置する
dframe.T.unstack()

dframe2 = DataFrame(np.arange(16).reshape((4,4)),
                    index=[['a','a','b','b'], [1,2,1,2]],
                    columns=[['NY','NY','LA','SF'], ['cold','hot','hot','cold']])
dframe2

# 列方向に名前をつける
dframe2.index.names = ['INDEX_1', 'INDEX_2']
dframe2

# 列方向に名前をつける
dframe2.columns.names = ['Cities', 'Temp']
dframe2

# 名前を使った操作(列方向の入替)
dframe2.swaplevel('Cities', 'Temp', axis=1)
dframe2

# レベル1(INDEX_2)でソート
dframe2.sortlevel(1)

dframe2.sortlevel(1).sortlevel(0)

# 階層的なレベルに応じた計算方法
dframe2
# Tempに着目して(Citiesを無視)合計を算出
dframe2.sum(level='Temp', axis=1)



