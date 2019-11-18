# import dependencies
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

# Page I'm scraping
my_url = 'https://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48?name=Desktop%2DGraphics%2DCards&Order=BESTSELLING'

# Creating a variable uClient that accesses the URL, reads HTML on the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# Save the html contents of the page and parse them
page_soup = soup(page_html, "html.parser")

# Create CSV with headers for name and shipping
filename = "products.csv"
f = open(filename, "w")

headers = "product_name, shipping\n"
f.write(headers)

# Find the class that contains all info for GFX cards
containers = page_soup.findAll("div", {"class":"item-container"})

# Loop through each GFX card container and pull product name and shipping
for container in containers:
    title_container = container.findAll("a", {"class":"item-title"})
    product_name = title_container[0].text

    shipping_container = container.findAll("li", {"class":"price-ship"})
    shipping = shipping_container[0].text.strip()

    # Write to CSV, replace commas, and new line after shipping
    f.write(product_name.replace(",", "|") + "," + shipping + "\n")