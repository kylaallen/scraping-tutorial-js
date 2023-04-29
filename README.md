# Kyla's Web Scraping Tutorial


## About The Project
The tutorial I chose is a web scraping tutorial that demonstrates how to extract information from a website using Python and BeautifulSoup. Specifically, the tutorial focuses on scraping product information from the Newegg website, including the brand name, product name, and shipping price for each product. Included in this project is the code used to scrape the information: scrape_demo.py and the csv file with my collected data: products.csv.

### Built With
* [BeautifulSoup][BeatifulSoup-url]
* [Sublime][Sublime-url]
* [Python][Python-url]
* [Link to YouTube Tutorial][link-url]

### Steps to Complete the Tutorial
1. Open a code editor or IDE, such as Sublime, and create a new Python file.
2. Import the required libraries for web scraping: urllib and BeautifulSoup. You can do this by including the following code at the beginning of your file:
```sh
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
```
3. Define the URL of the web page you want to scrape. In this case, we will use the Newegg website to scrape graphics card information:
mathematica
```sh
my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'
```
4. Open a connection to the web page using the urlopen() method and read the contents of the page using the read() method:
```sh
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
```
5. Parse the HTML content of the page using BeautifulSoup and the "html.parser":
```sh
page_soup = soup(page_html, "html.parser")
```
6. Find the containers that hold the product information using the findAll() method and the appropriate class or tag name. In this case, we want to find all the "item-container" divs:
```sh
containers= page_soup.findAll("div", {"class": "item-container"})
```
7. Create a CSV file to store the scraped information, and define the headers:
```sh
filename = "products.csv"
f = open(filename, "w")
headers = "product_name, shipping"
f.write(headers)
```
8. Loop through each container and extract the product name and shipping information. In this case, we want to find the product name within the "item-title" tag and the shipping information within the "price-ship" class:
```sh
for container in containers:
    title_container = container.findAll("a", {"class":"item-title"})
    product_name = title_container[0].text

    shipping_container = container.findAll("li", {"class": "price-ship"})
    shipping = shipping_container[0].text

    f.write(product_name.replace(",", "|") + "," + shipping + "\n")
```
9. Close the CSV file:
```sh
f.close()
```
10. Run the Python script and verify that the CSV file was created with the desired product information.

*Note: Be sure to test the code on a small sample of data before attempting to scrape a large dataset, as web scraping can be resource-intensive and may violate website terms of use or copyright laws.






[link-url]: https://www.youtube.com/watch?v=XQgXKtPSzUI&authuser=1
[BeatifulSoup-url]: https://www.crummy.com/software/BeautifulSoup/
[Sublime-url]: https://www.sublimetext.com/ 
[Python-url]: https://www.python.org/
