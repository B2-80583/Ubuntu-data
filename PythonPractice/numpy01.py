import numpy as np

def print_array_info(array):
    print(f"falgs =  {array.flags}")
    print(f"size =  {array.size}")
    print(f"type =  {array.dtype}")
    print(f"bytes =  {array.nbytes}")
    print(f"size =  {array.itemsize}")
    print(f"diamension =  {array.ndim}")
    print((f"shape = {array.shape}"))
def function():
    a1 = np.array([10,20,30,40,50])
    print_array_info(a1)
function()

def function01():
    a2 = np.array([10,"rashmi",True])
    print_array_info(a2)
function01()
# def function04():
#     a3 = np.array([
#         [10,20]
#         [30,40,50]
#         [50,69.79]
#     ])
# function04()