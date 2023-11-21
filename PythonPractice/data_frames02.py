import pandas as pd


#
# df = pd.read_csv('Salary_Data.csv')
# print(df)
# print(df.isna())
# # count of na record
#
# print(df.isna().sum())
#
# # to deal with Na values
# df_replace = df.fillna(0)
# print(df_replace.isna().sum())
# print()
#
# # try
#
#
#
# df['bonus'] = df['salary'] * 0.10
# df['New salary'] = df['New salary'] + df['bonus']
# print(df.columns)
# print(df)

def function():
    df = pd.read_csv('50_Startups.csv')
    print(df.columns)

    # df.drop('state', axis=1, inplace=True)
    # print(df.columns)
    #
    # df.drop('Administration', axis=1, inplace=True)
    # print(df.columns)
    #
    # df.drop('Marketing', axis=1, inplace=True)
    # print(df.columns)

    # df.drop(['state', 'Administration','Marketing'], axis =1, inplace = True)
    # print(df.columns)

    # del df['state']
    # print(df.columns)

    # print(df.Profit)
    # print(df['Profit'])

    # print(df[['Administration', 'Marketing', 'Profit']])

    # get value at 0 ,0 position 0th row and 0th col

    # print(df.iloc[0, 0])
    #
    # print(df.iloc[0,3])
    rows,colm = df.shape
    for index in range(rows):
        if df.iloc[index, 4] == 155752.60:
            print(index)

function()