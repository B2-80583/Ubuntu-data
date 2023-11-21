import pandas as pd
import requests
from bs4 import BeautifulSoup

product_data = []

for i in range(1, 101):
    url = ("https://www.flipkart.com/search?q=laptop+under+under+150000&otracker=search&otracker1=search&marketplace"
           "=FLIPKART&as-show=on&as=off&p%5B%5D=facets.price_range.from%3D20000&p%5B%5D=facets.price_range.to%3DMax&p"
           "%5B%5D=facets.rating%255B%255D%3D1%25E2%2598%2585%2B%2526%2Babove&page=") + str(i)
    r = requests.get(url)

    print("\nFetching the URL ...")

    soup = BeautifulSoup(r.text, "lxml")
    box = soup.find("div", class_="_1YokD2 _3Mn1Gg")

    print(f"\nScrapping the data from page {i} ...")

    if box is not None:
        for products_list_element in box.find_all("div", class_="_13oc-S"):
            product_name = products_list_element.find("div", class_="_4rR01T")
            product_price = products_list_element.find("div", class_="_30jeq3 _1_WHN1")
            product_rating = products_list_element.find("div", class_="_3LWZlK")
            product_description = products_list_element.find("ul", class_="_1xgFaf")
            product_url_link = products_list_element.find_all("a", class_="_1fQZEK", href=True)
            product_url = product_url_link[0]['href']
            try:
                if product_name is not None or product_description is not None or product_price is not None or product_rating is not None:
                    filtered_price = ''
                    for l in str(product_price.text):
                        for letter in l:
                            if letter != 'â' or letter != '‚' or letter != '¹':
                                filtered_price += letter
                    product_data.append([product_name.text, filtered_price, product_rating.text,
                                         product_description.text, product_url])
            except Exception as e:
                pass

print("\nCollecting scrapped data ...")

print("\nRe-Structured the data ...")

dataset = pd.DataFrame(data=product_data, columns=["Product", "Price", "Rating", "Description", "Url"])
dataset.to_csv("flipkart_laptop_data.csv", index=False)

print("\nData dumped in CSV ...")
