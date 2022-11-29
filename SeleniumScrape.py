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



#CODE TO FIND ALL MONDAY CLASSES Times
montime1 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[1]/table/tbody/tr[4]/td/ul/li[1]/div[1]')
montime1 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[2]/table/tbody/tr[4]/td/ul/li[1]/div[1]')
montime2 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[1]/table/tbody/tr[4]/td/ul/li[2]/div[1]')
montime3 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[1]/table/tbody/tr[4]/td/ul/li[3]/div[1]')
montime4 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[1]/table/tbody/tr[4]/td/ul/li[4]/div[1]')
montime5 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[1]/table/tbody/tr[4]/td/ul/li[5]/div[1]')
montime6 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[1]/table/tbody/tr[4]/td/ul/li[6]/div[1]')
montime7 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[1]/table/tbody/tr[4]/td/ul/li[7]/div[1]')
montime8 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[1]/table/tbody/tr[4]/td/ul/li[8]/div[1]')
montime9 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[1]/table/tbody/tr[4]/td/ul/li[9]/div[1]')
montime10 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[1]/table/tbody/tr[4]/td/ul/li[10]/div[1]')
montime11 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[1]/table/tbody/tr[4]/td/ul/li[11]/div[1]')
montime12 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[1]/table/tbody/tr[4]/td/ul/li[12]/div[1]')
montime13 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[1]/table/tbody/tr[4]/td/ul/li[13]/div[1]')
montime14 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[1]/table/tbody/tr[4]/td/ul/li[14]/div[1]')

print(montime1.text)
print(montime2.text)
print(montime3.text)
print(montime4.text)
print(montime5.text)
print(montime6.text)
print(montime7.text)
print(montime8.text)
print(montime9.text)
print(montime10.text)
print(montime12.text)
print(montime12.text)
print(montime13.text)
print(montime14.text)

##CODE TO FIND ALL MONDAY CLASSES INSTRUCTOR
moninstructor1 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[1]/table/tbody/tr[4]/td/ul/li[1]/div[2]/table/tbody/tr/td')
moninstructor2 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[1]/table/tbody/tr[4]/td/ul/li[2]/div[2]/table/tbody/tr/td')
moninstructor3 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[1]/table/tbody/tr[4]/td/ul/li[3]/div[2]/table/tbody/tr/td')
moninstructor4 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[1]/table/tbody/tr[4]/td/ul/li[4]/div[2]/table/tbody/tr/td')
moninstructor5 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[1]/table/tbody/tr[4]/td/ul/li[5]/div[2]/table/tbody/tr/td')
moninstructor6 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[1]/table/tbody/tr[4]/td/ul/li[6]/div[2]/table/tbody/tr/td')
moninstructor7 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[1]/table/tbody/tr[4]/td/ul/li[7]/div[2]/table/tbody/tr/td')
moninstructor8 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[1]/table/tbody/tr[4]/td/ul/li[8]/div[2]/table/tbody/tr/td')
moninstructor9 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[1]/table/tbody/tr[4]/td/ul/li[9]/div[2]/table/tbody/tr/td')
moninstructor10 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[1]/table/tbody/tr[4]/td/ul/li[10]/div[2]/table/tbody/tr/td')
moninstructor11 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[1]/table/tbody/tr[4]/td/ul/li[11]/div[2]/table/tbody/tr/td')
moninstructor12 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[1]/table/tbody/tr[4]/td/ul/li[12]/div[2]/table/tbody/tr/td')
moninstructor13 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[1]/table/tbody/tr[4]/td/ul/li[13]/div[2]/table/tbody/tr/td')
moninstructor14 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[1]/table/tbody/tr[4]/td/ul/li[14]/div[2]/table/tbody/tr/td')

print(moninstructor1.text)
print(moninstructor2.text)
print(moninstructor3.text)
print(moninstructor4.text)
print(moninstructor5.text)
print(moninstructor6.text)
print(moninstructor7.text)
print(moninstructor8.text)
print(moninstructor9.text)
print(moninstructor10.text)
print(moninstructor11.text)
print(moninstructor12.text)
print(moninstructor13.text)
print(moninstructor14.text)