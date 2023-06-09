from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'

# opening up connection, grabbing the page
uClient = uReq(my_url)

page_html = uClient.read()

uClient.close()
page_soup = soup(page_html, "html.parser")

#grabs each product
containers= page_soup.findAll("div", {"class": "item-container"})

filename = "products.csv"
f = open(filename, "w")

headers = "product_name, shipping"
f.write(headers)

for container in containers:

	#brand names have been changed since tutorial came out
	#some products have brand name = Nonetype
	#which is incompatible with the format of the tutorial
	

	#brand = container.div.div.a.img["title"]

	title_container = container.findAll("a", {"class":"item-title"})
	product_name = title_container[0].text

	shipping_container = container.findAll("li", {"class": "price-ship"})
	shipping = shipping_container[0].text

	#print("brand: "+brand)
	print("product_name: "+product_name)
	print("shipping: "+shipping)

	f.write(product_name.replace(",", "|") + "," + shipping + "\n")

f.close()
