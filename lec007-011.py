# %%
import numpy as np

############################################################
# Lec007
############################################################
my_list1 = [1,2,3,4]
my_array1 = np.array(my_list1)
my_array1

my_list2 = [11,22,33,44]
my_lists = [my_list1, my_list2]
my_lists

my_array2 = np.array(my_lists)
my_array2

my_array2.shape
my_array2.dtype

np.zeros(5)
my_zeros = np.zeros(5)
my_zeros.dtype

np.ones((5,5))

np.empty((3,4))

np.eye(5)

range(5)
np.arange(5)

################################
count = 0
for x in range(5):
    print(x)
    count += 1
print('ループ回数:{}'.format(count))
################################
count = 0
for x in range(1, 5):
    print(x)
    count += 1
print('ループ回数:{}'.format(count))
################################
count = 0
for x in range(0, 10, 2):
    print(x)
    count += 1
print('ループ回数:{}'.format(count))
################################

np.arange(5, 50, 2)


############################################################
# Lec008
############################################################
5/2

arr1 = np.array([[1,2,3,4],[5,6,7,8]])
arr1

arr1 * arr1

arr1 - arr1

1 / arr1

arr1 ** 3

############################################################
# Lec009
############################################################
arr = np.arange(0, 11)
arr

arr[8]

# slice
# 最初:以降、最後:より前まで(-1)
arr[1:5]
arr[2:]
arr[:6]
arr[:]
arr

# arrayのsliceは参照でしかない
slice_arr = arr[0:6]
slice_arr
slice_arr[:]=99
slice_arr
arr

# 元のarrayをcopy
arr_copy = arr.copy()
arr_copy
arr_copy[:]=99
arr_copy
arr

# 2次元のarray
arr_2d = np.array([[5,10,15],[20,25,30],[35,40,45]])
arr_2d

arr_2d[1]
arr_2d[0][1]
arr_2d[0,1]

# 右上の2×2を取り出す
# -> 2行目より前を取得、1番目の列以降
arr_2d[:2,1:]

arr_2d[2]
arr_2d[2,:]

# 便利な添字
arr2d = np.zeros((10,10))
arr2d
arr_len = arr2d.shape[1]
arr_len
for i in range(arr_len):
    arr2d[i] = i
arr2d

# 2,4,6,8行目を取り出す
arr2d[[2,4,6,8]]
# 順番も指定可能
arr2d[[6,4,2,7]]


#--------------------------
a = np.array([[1,2]])
a
a.shape

b = np.array([3,4])
b
b.shape

a+b

a = [1,2,3,4,5]
a
a[1:-1]
a[1:3]
a[:-2]
#--------------------------

############################################################
# Lec010
############################################################
arr = np.arange(9).reshape((3,3))
arr

# 行列の転置
arr.T
# 同じ
arr.transpose()
# 最初が行、次が列
arr.transpose((0,1))
arr.transpose((1,0))

arr.swapaxes(0,1)
arr.swapaxes(1,0)
arr

np.dot(arr.T, arr)

# 2×2の行列が3つの3次元の行列
arr3d = np.arange(12).reshape((3,2,2))
arr3d
arr3d[0]

arr3d.transpose((0,2,1))

#--------------------------
a = np.array([[1,2]])
a
a.shape

b = np.array([3,4])
b
b.shape

a+b

a = [1,2,3,4,5]
a
a[1:-1]
a[1:3]
a[:-2]
#--------------------------

# https://note.nkmk.me/python-list-array-numpy-ndarray/
#=========================
# list
#=========================
'''
組み込み型
何もimportせずに使える
異なる型を格納できる
リストのリストによって多次元配列を表現することも可能
厳密には配列と異なるが、配列ライクな簡単な処理を行うのであればリストlistで十分な場合が多い
'''
l = ['apple', 100, 0.123]
print(l)

l_2d = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
print(l_2d)

print(l_2d[1][1])

l_num = [0, 10, 20, 30]

print(min(l_num))
# 0

print(max(l_num))
# 30

print(sum(l_num))
# 60

print(sum(l_num) / len(l_num))
# 15.0

l_str = ['apple', 'orange', 'banana']
print(l_str)
for s in l_str:
    print(s)

#=========================
# array
#=========================
'''
標準モジュールarrayをimportして使う
8.7. array — 効率のよい数値アレイ — Python 3.6.5 ドキュメント
同じ型しか格納できない
一次元配列のみ
型に制限がある以外はリストと同様の処理が可能

コンストラクタarray.array()で型コードを指定して生成する。型コードの一覧は公式ドキュメント参照。
型コードと一致しない型の要素は格納できない
'''

import array

arr_int = array.array('i', [0, 1, 2])
print(arr_int)

arr_float = array.array('f', [0.0, 0.1, 0.2])
print(arr_float)

# arr_int = array.array('i', [0, 0.1, 2])
# TypeError: integer argument expected, got float


#=========================
# 多次元配列 - numpy.ndarray
#=========================
'''
NumPyをインストール、importして使う
同じ型しか格納できない
object型で様々な型へのポインタを格納することはできる
関連記事: NumPyのデータ型dtype一覧とastypeによる変換（キャスト）
多次元配列を表現できる
数値計算のためのメソッド・関数が豊富で、高速な演算が可能
行列演算や画像処理など様々な場面で使える
関連記事: Python, NumPyで行列の演算（逆行列、行列式、固有値など）
関連記事: Python, NumPyで画像処理（読み込み、演算、保存）
'''

arr = np.array([0, 1, 2])
print(arr)
# [0 1 2]

arr_2d = np.array([[0, 1, 2], [3, 4, 5]])
print(arr_2d)
# [[0 1 2]
#  [3 4 5]]

'''要素ごとに演算をしたり、行列積を求めたりできる。'''
arr_2d_sqrt = np.sqrt(arr_2d)
print(arr_2d_sqrt)
# [[0.         1.         1.41421356]
#  [1.73205081 2.         2.23606798]]

arr_1 = np.array([[1, 2], [3, 4]])
arr_2 = np.array([[1, 2, 3], [4, 5, 6]])

arr_product = np.dot(arr_1, arr_2)
print(arr_product)
# [[ 9 12 15]
#  [19 26 33]]

#=========================
# 独断と偏見によるそれぞれの使い分け
#=========================
'''
いわゆる配列ライクな処理をするのであればリストlistで十分な場合が多い。

標準モジュールarrayは格納する要素の型が制限されているので厳密なメモリ管理が可能だが、特に気にする必要がなければlist、より効率的な数値計算を行いたければnumpy.ndarrayのほうが適当。メモリサイズ、メモリアドレスを必要とするような処理以外に使いどころはない（と思う）。

多次元配列を扱う場合や配列に対する数値計算（科学技術演算）を行う場合はNumPy配列numpy.ndarrayを使う。

コンピュータビジョンライブラリOpenCVや機械学習ライブラリscikit-learnなど多くのライブラリでNumPy配列numpy.ndarrayが使われているので、それらのライブラリを使うと自動的にnumpy.ndarrayを使うことになる。

なお、listとnumpy.ndarrayは相互に変換する事が可能。以下の記事を参照。

関連記事: NumPy配列ndarrayとPython標準のリストを相互に変換
'''

#=========================
# データ分析ライブラリpandas
#=========================
'''
表で表現されるような二次元データ（列ごとに特徴量の値を持つもの）に対して統計的な処理を行う場合は、データ分析ライブラリpandasが便利。

Python Data Analysis Library — pandas: Python Data Analysis Library
pandasでは二次元データをpandas.DataFrameとして扱う。（pandas.Seiriesとして一次元データを扱うことも可能）

pandas.DataFrameもpandas.Seriesも内部ではnumpy.ndarrayでデータを保持しているが、行・列ごとの操作や表計算ソフトにおけるピボットテーブルのような操作など、データ処理に便利な関数やメソッドが豊富に用意されている。

雰囲気は以下のような感じ。列ごとの平均値を算出したり、属性を指定して集計したりしている。
'''
import pandas as pd

df = pd.read_csv('data/src/sample_pandas_normal.csv', index_col=0)
df['sex'] = ['Female', 'Male', 'Male', 'Male', 'Female', 'Male']
print(df)
#          age state  point     sex
# name                             
# Alice     24    NY     64  Female
# Bob       42    CA     92    Male
# Charlie   18    CA     70    Male
# Dave      68    TX     70    Male
# Ellen     24    CA     88  Female
# Frank     30    NY     57    Male

print(df.mean())
# age      34.333333
# point    73.500000
# dtype: float64

print(df.pivot_table(index='state', columns='sex', aggfunc='mean'))
#          age        point      
# sex   Female  Male Female  Male
# state                          
# CA      24.0  30.0   88.0  81.0
# NY      24.0  30.0   64.0  57.0
# TX       NaN  68.0    NaN  70.0

'''例のような数値と文字列を含んだデータはNumPyだと扱いが面倒だが、pandasだと非常に簡単。'''


############################################################
# Lec011
############################################################
arr = np.arange(11)
arr

# 平方根
np.sqrt(arr)

# 自然対数の底eを累乗した値
np.exp(arr)

# 正規分布に従う乱数を生成
A = np.random.randn(10)
A
B = np.random.randn(10)
B
np.add(A, B)
np.maximum(A, B)

