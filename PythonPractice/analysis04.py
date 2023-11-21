
from bs4 import BeautifulSoup
# read the content of html file

with open("weather.html", "r") as file:
    data = file.read()


# creat the soup
soup = BeautifulSoup(data, "html.parser")

# find the table tag

table_tag = soup.find("table")

#find the second row (tr)

tr_tag = table_tag.find_all("tr")[13]
# print(tr_tag)

my_table_tag = tr_tag.find("table")

#find the row of required table

tr_tags = my_table_tag.find_all('tr')

for index in range(2,len(tr_tags)):
    tr = tr_tags[index]

    # find all td
    td_tags = tr.find_all('td')
    date = td_tags[0].text.strip()
    max_temp = (td_tags[1].text.strip)
    min_temp = (td_tags[2].text.strip)

print(f"date = {date}, max_temp = {max_temp}, min_temp = {min_temp}")