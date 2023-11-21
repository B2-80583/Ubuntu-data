import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

browser = webdriver.Chrome()
product_laptop = []

browser.get('https://www.flipkart.com/search?q=laptop+under+under+150000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&p%5B%5D=facets.price_range.from%3D20000&p%5B%5D=facets.price_range.to%3DMax&p%5B%5D=facets.rating%255B%255D%3D1%25E2%2598%2585%2B%2526%2Babove&page=1')

section = browser.find_element(By.CLASS_NAME,"_1YokD2 _3Mn1Gg")
product_name = section.find_elements(By.CLASS_NAME, "_4rR01T")
product_rating = section.find_elements(By.CLASS_NAME, "_3LWZlK")
product_description = section.find_elements(By.CLASS_NAME, "_1xgFaf")
price = section.find_elements(By.CLASS_NAME, "_30jeq3 _1_WHN1")

if section is not None:
    for name in product_name:
        product_laptop.append(name.text)

    for rating in section.find_elements(product_rating):
        if rating.text is None or rating is None:
            product_laptop.append('0')
        else:
            product_laptop.append(rating.text)

    for description in section.find_elements(product_description):
        product_laptop.append(product_description.text)

    for price in section.find_elements(price):
        if price.text is None:
            product_laptop.append('0')
            print('Null values.....')
        else:
            product_laptop.append(str(price.text))

data = {'product_name': product_name, 'product price': price, 'product rating': product_rating,
        'product discription': product_description}

df = pd.DataFrame(data)
df.to_csv("flipkart_laptop_data.csv", index=False)
print('')
