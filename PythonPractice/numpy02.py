import numpy as np


def function1():
    a1 = np.array([10,20,30,40,50,60,70,80,90,100])
    print(a1[0])
    print(a1[a1.size-1])
    print(a1[-1])
    print(a1[-a1.size])
# function1()

def slicing01():
    a1 = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    print(a1[2:7])
    print(a1[8:10])
    print(a1[:5])
    print(a1[7:])
    print(a1[:])
# slicing01()

def function02():
    a1 = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    # # # list01 = [1,3,4,5,8]
    # # # values =[]
    # # # for index in list01:
    # # #     values.append(list01[index])
    #        a2 = np.array[[values]]
    #
    #
    # print(a1[[3,2,5,6,9]])
    # print(a1[[2,5,1,0,7,8]])

# function02()

def function03():
    a1 = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    # values = (f"{a1[[False,True,False,True,False,False,True,False,True,False]]}")
    # print(values)
    # values01 = (f"{a1[[True,True,True,False,False,True,False,True,True,False]]}")
    # values02 = (f"{a1[[False,False,False,True,True,False,True,True,False,True]]}")
    # print(values01,values02)
# function03()
# broadcast mathematical operation
#     print(a1 + 60)
#     print(a1 - 5)
#     print(a1 * 5)
#     print(a1 / 5)
#     print(a1 ** 2)
#
# broadcast relational operator
#     print(a1>45)
#     print(a1 < 45)
#     print(a1 <= 30)
#     print(a1 != 39)
#     print(a1 == 45)
# function03()

# def filtering():
#     salaries = np.array([20,30,50,60,70,80,90])
#     print(salaries > 50)
#     print(salaries[salaries > 30])
# filtering()


