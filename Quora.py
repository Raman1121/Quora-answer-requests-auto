from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.quora.com/answer/requests" 

#Opening up connection, grabbing the page.
uclient = urlopen(url) 
page_html = uclient.read()
uclient.close()

#HTML Parsing
page_soup = BeautifulSoup(page_html, "html.parser")

#Grabbing each question.
containers = page_soup.findAll("div", {"class": "_type_serif_title_medium pass_color_to_child_links"})

#Looping through all the questions and printing them.
for container in containers:
	question = container.div.a.span.span.text
	print(question)







