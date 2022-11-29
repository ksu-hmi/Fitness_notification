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
#enable logging
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])


#CODE TO PULL THE MOVIES EVERY DAY OF THE WEEK
#XPATH FROM MOVIE TITLES EVERYDAY
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

#PRINT THE MOVIES 
print('Monday: ' + mon.text)
print('Tuesday: ' + tue.text)
print('Wednesday: ' + wed.text)
print('Thursday: ' + thu.text)
print('Friday: ' + fri.text)
print('Saturday: ' + sat.text)
print('Sunday: ' + sun.text)


#CODE TO FIND ALL MONDAY CLASSES 
#FINDS THE IMG FIRST AND THEN WITHIN THE IMG FIND THE 'alt' ATTRIBUTE THAT CONTAINS THE CLASS NAME
monclass1 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[1]/table/tbody/tr[4]/td/ul/li[1]/img').get_attribute('alt')
monclass2 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[1]/table/tbody/tr[4]/td/ul/li[2]/img').get_attribute('alt')
monclass3 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[1]/table/tbody/tr[4]/td/ul/li[3]/img').get_attribute('alt')
monclass4 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[1]/table/tbody/tr[4]/td/ul/li[4]/img').get_attribute('alt')
monclass5 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[1]/table/tbody/tr[4]/td/ul/li[5]/img').get_attribute('alt')
monclass6 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[1]/table/tbody/tr[4]/td/ul/li[6]/img').get_attribute('alt')
monclass7 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[1]/table/tbody/tr[4]/td/ul/li[7]/img').get_attribute('alt')
monclass8 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[1]/table/tbody/tr[4]/td/ul/li[8]/img').get_attribute('alt')
monclass9 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[1]/table/tbody/tr[4]/td/ul/li[9]/img').get_attribute('alt')
monclass10 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[1]/table/tbody/tr[4]/td/ul/li[10]/img').get_attribute('alt')
monclass11 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[1]/table/tbody/tr[4]/td/ul/li[11]/img').get_attribute('alt')
monclass12 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[1]/table/tbody/tr[4]/td/ul/li[12]/img').get_attribute('alt')
monclass13 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[1]/table/tbody/tr[4]/td/ul/li[13]/img').get_attribute('alt')
monclass14 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[1]/table/tbody/tr[4]/td/ul/li[14]/img').get_attribute('alt')

print("-----MONDAY CLASSES-----")
print(monclass1)
print(monclass2)
print(monclass3)
print(monclass4)
print(monclass5)
print(monclass6)
print(monclass7)
print(monclass8)
print(monclass9)
print(monclass10)
print(monclass11)
print(monclass12)
print(monclass13)
print(monclass14)