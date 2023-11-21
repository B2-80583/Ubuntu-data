from bs4 import BeautifulSoup

data = """
<html>
<body>
<head></head>
<h1> header 1 </h1>
<h1> header 2 </h1>
<h1> header 3 </h1>

<div> this is a division 1 </div>
<div> this is a division 2 </div>
<div> this is a division 3 </div>

<div> <p> the is paragraph inside div </div>
</div>
<p> this is paragraph outside div </p>

<span> this is a span </span>



</body>
</html>
"""
soup = BeautifulSoup(data, "html.parser")
div_elements = soup.find_all("div")
for div_element in div_elements:
    print(f"content of div = {div_element.text}")

# find the second occurance of header

h1_elements = soup.find_all("h1")
print(f"h1_element content = {h1_elements[1].text}")

# get the content of p tag outside the div
p_tag = soup.find_all("p")
print(p_tag[1].text)

div_tag = soup.find('div')
p_tag = div_tag.find('p')
print(p_tag)
# print(soup.find('body'))

