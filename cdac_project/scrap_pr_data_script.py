import pandas as pd
import requests
from bs4 import BeautifulSoup


product_review_data = []
df = pd.read_csv("datasets/flipkart_laptop_cleaned_data.csv")
pr_id = 0


for review_url in df['Review Url']:
    print(f'SCRAPPING PRODUCT REVIEWS FOR {pr_id + 1}st PRODUCT ... \n')
    pr_id += 1
    r = requests.get(str(review_url))

    soup = BeautifulSoup(r.text, "lxml")
    box = soup.find("div", class_="_1YokD2 _3Mn1Gg col-9-12")
    # print(box)
    if box is not None:
        for product_review_element in box.find_all("div", class_="col _2wzgFH K0kLPL"): # col _2wzgFH K0kLPL
            if product_review_element is not None:
                review_title = product_review_element.find("p", class_="_2-N8zT") # _2-N8zT
                customer_rating = product_review_element.find("div", class_="_3LWZlK _1BLPMq")
                review_details = product_review_element.find("div", class_="t-ZTKy")
                upvote = product_review_element.find("div", class_="_1LmwT9")
                downvote = product_review_element.find("div", class_="_1LmwT9 pkR4jH")
                if customer_rating is not None:
                    product_review_data.append([pr_id,review_title.text, customer_rating.text, review_details.text, upvote.text, downvote.text])
                else:
                    product_review_data.append([pr_id, review_title.text, '', review_details.text, upvote.text, downvote.text])

dataset = pd.DataFrame(data=product_review_data, columns=["Product Review ID", "Title", "rating", "detail_review", "upvote", "downvote"])
dataset.to_csv("datasets/flipkart_laptop_review_data.csv", index=False)