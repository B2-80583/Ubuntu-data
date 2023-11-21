from bs4 import BeautifulSoup

data = """
<html>
<body>
<head></head>


<div id = "div1"> this is a division 1 </div>
<div> id = "div2"> this is a division 2 </div>
<div> id = "div3"> this is a division 3 </div>

<div> class = "mydiv1"> this is a division mydiv1 </div>
<span> this is a span </span>

</body>
</html>
"""

soup = BeautifulSoup(data,"html.parser")

# find the contents of div with id - "div1"

div_tag = soup.find("div", {"id": "div1"})
print(div_tag.text)

# find the contents of the div with class = "mydiv1"
# find the contents of the div with name = "mydiv1"
class_tag = soup.find("div", {"class": "mydiv1"})
print(class_tag.text)

