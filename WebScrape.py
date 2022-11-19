#To use this code, you will first need to install the two packagtes being imported below using pip or manual install method.

from bs4 import BeautifulSoup
import requests

#grab basic content from a web page
url = "https://www.onelifefitness.com/gyms/atlanta-holly-springs?hsLang=en"
page = requests.get(url)

#using the html parser to process the webpage text content
soup = BeautifulSoup(page.text,'html.parser')

for img in soup.find_all('img',alt=True):
    print(img)


