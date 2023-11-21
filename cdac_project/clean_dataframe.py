import pandas as pd


# Read csv
df = pd.read_csv("flipkart_laptop_data.csv")

# df['Products'] = pd.unique(df['Product'])

# Blank list to store the product-review urls/links
review_urls = []

# Cleaning Data
df['Price'] = df['Price'].str.replace('₹', '')
df['Price'] = df['Price'].str.replace(',', '')
df['Price'] = df['Price'].astype(float)
df['Url'] = 'https://www.flipkart.com' + df['Url']




# Construct the product-review links from product links
for link in df['Url']:
    url = link.split('/p/')
    review_link = url[0] + '/product-reviews/' + url[1]
    review_urls.append(review_link)

# Store the list as column in the DataFrame
df['Review Url'] = review_urls

# Save to csv
df.to_csv("flipkart_laptop_cleaned_data.csv", index=False)

print(df.info())

