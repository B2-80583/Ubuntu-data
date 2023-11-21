import pandas as pd


def function():
    series =  pd.Series([10,20,30,40,50,60,70,80,90,100])
#     print(series[5]) #indexing
#     print((series[9]))
#     print(series[-1])
# function()
    print(series + 10)
    print(series >= 50)
    print(series == 50)
    print(series[series >=  35])
function()