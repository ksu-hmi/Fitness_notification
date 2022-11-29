#first need to install selenium and also chronium to use the below code
from selenium import webdriver
#allows for searching of elements
from selenium.webdriver.common.by import By
#the explicit wait code -- waits for a certan condition to occur before proceeding further  
# in the code both of the imports (WebDriverWait & ExpectedCondition) needed.
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#website used for scrape
website = "https://www.onelifefitness.com/gyms/atlanta-holly-springs?hsLang=en"
#the path to chromedriver
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

#getting the url 
driver.get(website)

#making the page load before code executes
driver.implicitly_wait(10)  # seconds
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

//*[@id="divContent"]/table[2]/tbody/tr[1]/td[1]/table/tbody/tr[2]

#CODE TO PULL THE MOVIES EVERY DAY OF THE WEEK
mon = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[2]/td')
tue = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[2]/td')
wed = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[2]/td')
thu = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[4]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[2]/td')
fri = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[5]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[2]/td')
sat = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[6]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[2]/td')
sun = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[7]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[2]/td')
print('Monday: ' + mon.text)
print('Tuesday: ' + tue.text)
print('Wednesday: ' + wed.text)
print('Thursday: ' + thu.text)
print('Friday: ' + fri.text)
print('Saturday: ' + sat.text)
print('Sunday: ' + sun.text)

#CODE TO FIND ALL MONDAY CLASSES 
