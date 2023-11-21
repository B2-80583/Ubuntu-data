from bs4 import BeautifulSoup
import json

# read the content of html file

with open("moneyControl.html", "r") as file:
    data = file.read()

soup = BeautifulSoup(data, "html.parser")
table_tag = soup.find("section", {"id"= ''})
tr_tag = table_tag.find_all("tr")[1]
my_table_tag = tr_tag.find("tr")
tr_tags = my_table_tag.find_all('tr')

for index in range(2, len(tr_tags)):
    tr = tr_tags[index]
    print(tr)
    td_tags = tr.find_all('td')
    company_name = td_tags[0].text.strip
    high = td_tags[1].text.strip
    low = td_tags[2].text.strip
    percent_change = td_tags[3].text.strip

print(f"company_name = {company_name}, high = {high}, low = {low}, percent_change = {percent_change}")

