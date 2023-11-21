from selenium import webdriver
from selenium.webdriver.common.by import By
import json


# load the browser
browser = webdriver.Chrome()

# browse as site
browser.get("https://www.moneycontrol.com/stocks/marketstats/nsegainer/index.php")

# find the section
section = browser.find_element(By.ID, "mc_content")

# find the table
table = section.find_element(By.TAG_NAME, "table")

# find tbody
tbody = table.find_element(By.TAG_NAME, "tbody")

# find tr
rows = table.find_elements(By.TAG_NAME, "tr")

# collect all gainers
top_gainers = []

# for every row, get the columns and read the info
for row in rows:
    # find the td tags for every row
    columns = row.find_elements(By.TAG_NAME, "td")

    # skip the hidden columns
    if len(columns) < 7:
        continue

    a = columns[0].find_element(By.TAG_NAME, "a")
    company_name = a.text
    high = columns[1].text
    low = columns[2].text
    last_price = columns[3].text
    previous_price = columns[4].text
    change = columns[5].text
    gain = columns[6].text

    top_gainers.append({
        "company_name": company_name,
        "high": float(high.replace(",", "")),
        "low": float(low.replace(",", "")),
        "last_price": float(last_price.replace(",", "")),
        "previous_price": float(previous_price.replace(",", "")),
        "change": float(change),
        "gain": float(gain)
    })

print("TOP GAINERS: ", top_gainers, "\n", len(top_gainers))

json_data = json.dumps(top_gainers)

print("JSON DUMP: ", json_data)
with open("./top_gainers_selenium.json", "w") as file:
    file.write(json_data)

# exit the browser
browser.quit()