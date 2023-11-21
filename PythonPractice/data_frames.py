import pandas as  pd

df = pd.read_csv('50_Startups.csv')
# print(df)
# print(type(df))
# print(df.dtypes)
# print(df.ndim)
# print(df.shape)
# print(df.size)
# rows, cols = df.shape
# print(rows,cols)
#
# # print(df.columns)
#
# print(df.head(5))
#
# print(df.tail(10))

df.info()
print(df.describe())