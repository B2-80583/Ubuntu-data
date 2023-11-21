
from bs4 import BeautifulSoup

with open("data.html", "r") as file:
    data = file.read()

soup = BeautifulSoup(data, "html.parser")

section = soup.find("section" ,{"id" : "top_gainer"})

table_tag = section.find("table")
tbody = table_tag.find("tbody")

rows = tbody.find("tr")

for index in rows:

    columns = rows.find_all("td")

    company_name = columns[0].text
    high = columns[1].text
    low = columns[2].text

print(company_name, high, low)