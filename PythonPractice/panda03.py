import pandas as pd
def function():
     names = ['person1','person2','person3','person4']
     ages = [20,30,40]
     addresses = ['pune','mumbai','karad']

     data_frame = pd.DataFrame(names,ages,addresses)

def function01():
    df = pd.read_csv('housing.csv')
    print(df)
function01()
