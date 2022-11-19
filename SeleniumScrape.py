#first need to install selenium and also chronium to use the below code
from selenium import webdriver
#give us access to different keys on the key board (like the enter key, escape key, etc...)
from selenium.webdriver.common.keys import Keys
#allows for searching of elements
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options 
#perform select strategies and choose the choices from the dropdown list
from selenium.webdriver.support.ui import Select
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

#getting the url 
driver.get("https://www.onelifefitness.com/gyms/atlanta-holly-springs?hsLang=en")
print(driver.title)

#After instepcting the region select area -- it is telling to find the element ID
classopt = driver.find_element(By.ID, ('selectClasses'))
#Send the key "GA" since that's the region that we want

#Tells it to press the "enter" key on the keyboard to search
#region.send_keys(Keys.RETURN)

#so we can see what is happening and delays it for 5 seconds
#time.sleep(10)

print(classopt)