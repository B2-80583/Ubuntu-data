import pandas as pd
import numpy as np

# series_numbers = pd.Series([10,30,40,60,70])
# print(series_numbers)
# print(type(series_numbers))
# print(series_numbers[series_numbers.size - 1])
# print(series_numbers.dtype)
# print(series_numbers.ndim)
# print(series_numbers.shape)
# print(series_numbers.values)
# print(series_numbers.index)


def function01():


   models = ["iphone", "s22", "one plus", "pixel", "note 5 pro"]
   companies = ["apple","samsung","one plus","google","xiami"]

   print(f"the models we have: {models} ")
   print(f"the companies of that models: {companies}")
   phones = pd.Series(models , index=companies)
   print(phones)

   print(phones['apple'])
   # print(phones['nokia'])

   companies_phones = pd.Series(companies , index = models)
   print(companies_phones)
function01()


