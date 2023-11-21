# collectig data from websites == scraping
from bs4 import BeautifulSoup

# create the data source

data = """
<html>
<body>
<head></head>
<p> paragraph 1 </p>
<h1> header </h1>
<span> this is a span </span>
</body>
</html>
"""

# create a soup
# parse the html contents using html parser

# parser =
# - paragram which understand the structure of file
# - it extract the information as per requirement

soup = BeautifulSoup(data, "html.parser")

# get the contents of paragraph (p tag)
p_contents = soup.find("p")
print(p_contents)

# get the contents of header 1 (h1)
h1_content = soup.find('h1')
print(h1_content)




