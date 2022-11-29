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
print("\nShowing Movies in the Cardio Cinema\n")
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

print("\nMONDAY SCHEDULE\n")
print(montime1.text, monclass1, "with", moninstructor1.text)
print(montime2.text, monclass2, "with", moninstructor2.text)
print(montime3.text, monclass3, "with", moninstructor3.text)
print(montime4.text, monclass4, "with", moninstructor4.text)
print(montime5.text, monclass5, "with", moninstructor5.text)
print(montime6.text, monclass6, "with", moninstructor6.text)
print(montime7.text, monclass7, "with", moninstructor7.text)
print(montime8.text, monclass8, "with", moninstructor8.text)
print(montime9.text, monclass9, "with", moninstructor9.text)
print(montime10.text, monclass10, "with", moninstructor10.text)
print(montime11.text, monclass11, "with", moninstructor11.text)
print(montime12.text, monclass12, "with", moninstructor12.text)
print(montime13.text, monclass13, "with", moninstructor13.text)
print(montime14.text, monclass14, "with", moninstructor14.text)

#CODE TO FIND ALL TUESDAY CLASSES, TIMES AND INSTRUCTOR
tueclass1 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[2]/table/tbody/tr[4]/td/ul/li[1]/div[1]').get_attribute('alt')
tueclass2 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[2]/table/tbody/tr[4]/td/ul/li[2]/img').get_attribute('alt')
tueclass3 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[2]/table/tbody/tr[4]/td/ul/li[3]/img').get_attribute('alt')
tueclass4 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[2]/table/tbody/tr[4]/td/ul/li[4]/img').get_attribute('alt')
tueclass5 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[2]/table/tbody/tr[4]/td/ul/li[5]/img').get_attribute('alt')
tueclass6 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[2]/table/tbody/tr[4]/td/ul/li[6]/img').get_attribute('alt')
tueclass7 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[2]/table/tbody/tr[4]/td/ul/li[7]/img').get_attribute('alt')
tueclass8 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[2]/table/tbody/tr[4]/td/ul/li[8]/img').get_attribute('alt')
tueclass9 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[2]/table/tbody/tr[4]/td/ul/li[9]/img').get_attribute('alt')
tueclass10 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[2]/table/tbody/tr[4]/td/ul/li[10]/img').get_attribute('alt')
tueclass11 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[2]/table/tbody/tr[4]/td/ul/li[11]/img').get_attribute('alt')
tueclass12 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[2]/table/tbody/tr[4]/td/ul/li[12]/img').get_attribute('alt')
tueclass13 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[2]/table/tbody/tr[4]/td/ul/li[13]/img').get_attribute('alt')
tueclass14 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[2]/table/tbody/tr[4]/td/ul/li[14]/img').get_attribute('alt')
tueclass15 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[2]/table/tbody/tr[4]/td/ul/li[15]/img').get_attribute('alt')
tueclass16 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[2]/table/tbody/tr[4]/td/ul/li[16]/img').get_attribute('alt')
tueclass17 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[2]/table/tbody/tr[4]/td/ul/li[17]/img').get_attribute('alt')

tuetime1 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[2]/table/tbody/tr[4]/td/ul/li[1]/div[1]')
tuetime2 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[2]/table/tbody/tr[4]/td/ul/li[2]/div[1]')
tuetime3 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[2]/table/tbody/tr[4]/td/ul/li[3]/div[1]')
tuetime4 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[2]/table/tbody/tr[4]/td/ul/li[4]/div[1]')
tuetime5 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[2]/table/tbody/tr[4]/td/ul/li[5]/div[1]')
tuetime6 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[2]/table/tbody/tr[4]/td/ul/li[6]/div[1]')
tuetime7 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[2]/table/tbody/tr[4]/td/ul/li[7]/div[1]')
tuetime8 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[2]/table/tbody/tr[4]/td/ul/li[8]/div[1]')
tuetime9 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[2]/table/tbody/tr[4]/td/ul/li[9]/div[1]')
tuetime10 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[2]/table/tbody/tr[4]/td/ul/li[10]/div[1]')
tuetime11 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[2]/table/tbody/tr[4]/td/ul/li[11]/div[1]')
tuetime12 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[2]/table/tbody/tr[4]/td/ul/li[12]/div[1]')
tuetime13 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[2]/table/tbody/tr[4]/td/ul/li[13]/div[1]')
tuetime14 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[2]/table/tbody/tr[4]/td/ul/li[14]/div[1]')
tuetime15 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[2]/table/tbody/tr[4]/td/ul/li[15]/div[1]')
tuetime16 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[2]/table/tbody/tr[4]/td/ul/li[16]/div[1]')
tuetime17 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[2]/table/tbody/tr[4]/td/ul/li[17]/div[1]')

tueinstructor1 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[2]/table/tbody/tr[4]/td/ul/li[1]/div[2]/table/tbody/tr/td')
tueinstructor2 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[2]/table/tbody/tr[4]/td/ul/li[2]/div[2]/table/tbody/tr/td')
tueinstructor3 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[2]/table/tbody/tr[4]/td/ul/li[3]/div[2]/table/tbody/tr/td')
tueinstructor4 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[2]/table/tbody/tr[4]/td/ul/li[4]/div[2]/table/tbody/tr/td')
tueinstructor5 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[2]/table/tbody/tr[4]/td/ul/li[5]/div[2]/table/tbody/tr/td')
tueinstructor6 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[2]/table/tbody/tr[4]/td/ul/li[6]/div[2]/table/tbody/tr/td')
tueinstructor7 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[2]/table/tbody/tr[4]/td/ul/li[7]/div[2]/table/tbody/tr/td')
tueinstructor8 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[2]/table/tbody/tr[4]/td/ul/li[8]/div[2]/table/tbody/tr/td')
tueinstructor9 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[2]/table/tbody/tr[4]/td/ul/li[9]/div[2]/table/tbody/tr/td')
tueinstructor10 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[2]/table/tbody/tr[4]/td/ul/li[10]/div[2]/table/tbody/tr/td')
tueinstructor11 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[2]/table/tbody/tr[4]/td/ul/li[11]/div[2]/table/tbody/tr/td')
tueinstructor12 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[2]/table/tbody/tr[4]/td/ul/li[12]/div[2]/table/tbody/tr/td')
tueinstructor13 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[2]/table/tbody/tr[4]/td/ul/li[13]/div[2]/table/tbody/tr/td')
tueinstructor14 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[2]/table/tbody/tr[4]/td/ul/li[14]/div[2]/table/tbody/tr/td')
tueinstructor15 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[2]/table/tbody/tr[4]/td/ul/li[15]/div[2]/table/tbody/tr/td')
tueinstructor16 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[2]/table/tbody/tr[4]/td/ul/li[16]/div[2]/table/tbody/tr/td')
tueinstructor17 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[2]/table/tbody/tr[4]/td/ul/li[17]/div[2]/table/tbody/tr/td')

print("\nTUESDAY CLASSES\n")
print(tuetime1.text, tueclass1, "with", tueinstructor1.text)
print(tuetime2.text, tueclass2, "with", tueinstructor2.text)
print(tuetime3.text, tueclass3, "with", tueinstructor3.text)
print(tuetime4.text, tueclass4, "with", tueinstructor4.text)
print(tuetime5.text, tueclass5, "with", tueinstructor5.text)
print(tuetime6.text, tueclass6, "with", tueinstructor6.text)
print(tuetime7.text, tueclass7, "with", tueinstructor7.text)
print(tuetime8.text, tueclass8, "with", tueinstructor8.text)
print(tuetime9.text, tueclass9, "with", tueinstructor9.text)
print(tuetime10.text, tueclass10, "with", tueinstructor10.text)
print(tuetime11.text, tueclass11, "with", tueinstructor11.text)
print(tuetime12.text, tueclass12, "with", tueinstructor12.text)
print(tuetime13.text, tueclass13, "with", tueinstructor13.text)
print(tuetime14.text, tueclass14, "with", tueinstructor14.text)
print(tuetime15.text, tueclass15, "with", tueinstructor15.text)
print(tuetime16.text, tueclass16, "with", tueinstructor16.text)
print(tuetime17.text, tueclass17, "with", tueinstructor17.text)

#CODE TO FIND ALL WEDNESDAY CLASSES, TIMES AND INSTRUCTOR
wedclass1 = driver.find_element(By.XPATH,
	'//*[@id="divContent"]/table[2]/tbody/tr[1]/td[3]/table/tbody/tr[4]/td/ul/li[1]/img').get_attribute('alt')
wedclass2 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[3]/table/tbody/tr[4]/td/ul/li[2]/img').get_attribute('alt')
wedclass3 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[3]/table/tbody/tr[4]/td/ul/li[3]/img').get_attribute('alt')
wedclass4 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[3]/table/tbody/tr[4]/td/ul/li[4]/img').get_attribute('alt')
wedclass5 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[3]/table/tbody/tr[4]/td/ul/li[5]/img').get_attribute('alt')
wedclass6 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[3]/table/tbody/tr[4]/td/ul/li[6]/img').get_attribute('alt')
wedclass7 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[3]/table/tbody/tr[4]/td/ul/li[7]/img').get_attribute('alt')
wedclass8 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[3]/table/tbody/tr[4]/td/ul/li[8]/img').get_attribute('alt')
wedclass9 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[3]/table/tbody/tr[4]/td/ul/li[9]/img').get_attribute('alt')
wedclass10 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[3]/table/tbody/tr[4]/td/ul/li[10]/img').get_attribute('alt')
wedclass11 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[3]/table/tbody/tr[4]/td/ul/li[11]/img').get_attribute('alt')
wedclass12 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[3]/table/tbody/tr[4]/td/ul/li[12]/img').get_attribute('alt')
wedclass13 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[3]/table/tbody/tr[4]/td/ul/li[13]/img').get_attribute('alt')
wedclass14 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[3]/table/tbody/tr[4]/td/ul/li[14]/img').get_attribute('alt')
wedclass15 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[3]/table/tbody/tr[4]/td/ul/li[15]/img').get_attribute('alt')


wedtime1 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[3]/table/tbody/tr[4]/td/ul/li[1]/div[1]')
wedtime2 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[3]/table/tbody/tr[4]/td/ul/li[2]/div[1]')
wedtime3 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[3]/table/tbody/tr[4]/td/ul/li[3]/div[1]')
wedtime4 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[3]/table/tbody/tr[4]/td/ul/li[4]/div[1]')
wedtime5 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[3]/table/tbody/tr[4]/td/ul/li[5]/div[1]')
wedtime6 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[3]/table/tbody/tr[4]/td/ul/li[6]/div[1]')
wedtime7 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[3]/table/tbody/tr[4]/td/ul/li[7]/div[1]')
wedtime8 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[3]/table/tbody/tr[4]/td/ul/li[8]/div[1]')
wedtime9 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[3]/table/tbody/tr[4]/td/ul/li[9]/div[1]')
wedtime10 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[3]/table/tbody/tr[4]/td/ul/li[10]/div[1]')
wedtime11 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[3]/table/tbody/tr[4]/td/ul/li[11]/div[1]')
wedtime12 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[3]/table/tbody/tr[4]/td/ul/li[12]/div[1]')
wedtime13 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[3]/table/tbody/tr[4]/td/ul/li[13]/div[1]')
wedtime14 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[3]/table/tbody/tr[4]/td/ul/li[14]/div[1]')
wedtime15 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[3]/table/tbody/tr[4]/td/ul/li[15]/div[1]')


wedinstructor1 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[3]/table/tbody/tr[4]/td/ul/li[1]/div[2]/table/tbody/tr/td')
wedinstructor2 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[3]/table/tbody/tr[4]/td/ul/li[2]/div[2]/table/tbody/tr/td')
wedinstructor3 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[3]/table/tbody/tr[4]/td/ul/li[3]/div[2]/table/tbody/tr/td')
wedinstructor4 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[3]/table/tbody/tr[4]/td/ul/li[4]/div[2]/table/tbody/tr/td')
wedinstructor5 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[3]/table/tbody/tr[4]/td/ul/li[5]/div[2]/table/tbody/tr/td')
wedinstructor6 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[3]/table/tbody/tr[4]/td/ul/li[6]/div[2]/table/tbody/tr/td')
wedinstructor7 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[3]/table/tbody/tr[4]/td/ul/li[7]/div[2]/table/tbody/tr/td')
wedinstructor8 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[3]/table/tbody/tr[4]/td/ul/li[8]/div[2]/table/tbody/tr/td')
wedinstructor9 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[3]/table/tbody/tr[4]/td/ul/li[9]/div[2]/table/tbody/tr/td')
wedinstructor10 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[3]/table/tbody/tr[4]/td/ul/li[10]/div[2]/table/tbody/tr/td')
wedinstructor11 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[3]/table/tbody/tr[4]/td/ul/li[11]/div[2]/table/tbody/tr/td')
wedinstructor12 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[3]/table/tbody/tr[4]/td/ul/li[12]/div[2]/table/tbody/tr/td')
wedinstructor13 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[3]/table/tbody/tr[4]/td/ul/li[13]/div[2]/table/tbody/tr/td')
wedinstructor14 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[3]/table/tbody/tr[4]/td/ul/li[14]/div[2]/table/tbody/tr/td')
wedinstructor15 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[3]/table/tbody/tr[4]/td/ul/li[15]/div[2]/table/tbody/tr/td')
 

print("\nWEDNESDAY CLASSES\n")
print(wedtime1.text, wedclass1, "with", wedinstructor1.text)
print(wedtime2.text, wedclass2, "with", wedinstructor2.text)
print(wedtime3.text, wedclass3, "with", wedinstructor3.text)
print(wedtime4.text, wedclass4, "with", wedinstructor4.text)
print(wedtime5.text, wedclass5, "with", wedinstructor5.text)
print(wedtime6.text, wedclass6, "with", wedinstructor6.text)
print(wedtime7.text, wedclass7, "with", wedinstructor7.text)
print(wedtime8.text, wedclass8, "with", wedinstructor8.text)
print(wedtime9.text, wedclass9, "with", wedinstructor9.text)
print(wedtime10.text, wedclass10, "with", wedinstructor10.text)
print(wedtime11.text, wedclass11, "with", wedinstructor11.text)
print(wedtime12.text, wedclass12, "with", wedinstructor12.text)
print(wedtime13.text, wedclass13, "with", wedinstructor13.text)
print(wedtime14.text, wedclass14, "with", wedinstructor14.text)
print(wedtime15.text, wedclass15, "with", wedinstructor15.text)


#CODE TO FIND ALL THURSDAY CLASSES, TIMES AND INSTRUCTOR
thuclass1 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[4]/table/tbody/tr[4]/td/ul/li[1]/div[1]').get_attribute('alt')
thuclass2 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[4]/table/tbody/tr[4]/td/ul/li[2]/img').get_attribute('alt')
thuclass3 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[4]/table/tbody/tr[4]/td/ul/li[3]/img').get_attribute('alt')
thuclass4 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[4]/table/tbody/tr[4]/td/ul/li[4]/img').get_attribute('alt')
thuclass5 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[4]/table/tbody/tr[4]/td/ul/li[5]/img').get_attribute('alt')
thuclass6 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[4]/table/tbody/tr[4]/td/ul/li[6]/img').get_attribute('alt')
thuclass7 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[4]/table/tbody/tr[4]/td/ul/li[7]/img').get_attribute('alt')
thuclass8 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[4]/table/tbody/tr[4]/td/ul/li[8]/img').get_attribute('alt')
thuclass9 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[4]/table/tbody/tr[4]/td/ul/li[9]/img').get_attribute('alt')
thuclass10 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[4]/table/tbody/tr[4]/td/ul/li[10]/img').get_attribute('alt')
thuclass11 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[4]/table/tbody/tr[4]/td/ul/li[11]/img').get_attribute('alt')
thuclass12 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[4]/table/tbody/tr[4]/td/ul/li[12]/img').get_attribute('alt')
thuclass13 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[4]/table/tbody/tr[4]/td/ul/li[13]/img').get_attribute('alt')
thuclass14 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[4]/table/tbody/tr[4]/td/ul/li[14]/img').get_attribute('alt')
thuclass15 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[4]/table/tbody/tr[4]/td/ul/li[15]/img').get_attribute('alt')
thuclass16 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[4]/table/tbody/tr[4]/td/ul/li[16]/img').get_attribute('alt')


thutime1 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[4]/table/tbody/tr[4]/td/ul/li[1]/div[1]')
thutime2 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[4]/table/tbody/tr[4]/td/ul/li[2]/div[1]')
thutime3 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[4]/table/tbody/tr[4]/td/ul/li[3]/div[1]')
thutime4 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[4]/table/tbody/tr[4]/td/ul/li[4]/div[1]')
thutime5 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[4]/table/tbody/tr[4]/td/ul/li[5]/div[1]')
thutime6 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[4]/table/tbody/tr[4]/td/ul/li[6]/div[1]')
thutime7 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[4]/table/tbody/tr[4]/td/ul/li[7]/div[1]')
thutime8 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[4]/table/tbody/tr[4]/td/ul/li[8]/div[1]')
thutime9 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[4]/table/tbody/tr[4]/td/ul/li[9]/div[1]')
thutime10 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[4]/table/tbody/tr[4]/td/ul/li[10]/div[1]')
thutime11 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[4]/table/tbody/tr[4]/td/ul/li[11]/div[1]')
thutime12 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[4]/table/tbody/tr[4]/td/ul/li[12]/div[1]')
thutime13 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[4]/table/tbody/tr[4]/td/ul/li[13]/div[1]')
thutime14 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[4]/table/tbody/tr[4]/td/ul/li[14]/div[1]')
thutime15 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[4]/table/tbody/tr[4]/td/ul/li[15]/div[1]')
thutime16 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[4]/table/tbody/tr[4]/td/ul/li[16]/div[1]')


thuinstructor1 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[4]/table/tbody/tr[4]/td/ul/li[1]/div[2]/table/tbody/tr/td')
thuinstructor2 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[4]/table/tbody/tr[4]/td/ul/li[2]/div[2]/table/tbody/tr/td')
thuinstructor3 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[4]/table/tbody/tr[4]/td/ul/li[3]/div[2]/table/tbody/tr/td')
thuinstructor4 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[4]/table/tbody/tr[4]/td/ul/li[4]/div[2]/table/tbody/tr/td')
thuinstructor5 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[4]/table/tbody/tr[4]/td/ul/li[5]/div[2]/table/tbody/tr/td')
thuinstructor6 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[4]/table/tbody/tr[4]/td/ul/li[6]/div[2]/table/tbody/tr/td')
thuinstructor7 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[4]/table/tbody/tr[4]/td/ul/li[7]/div[2]/table/tbody/tr/td')
thuinstructor8 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[4]/table/tbody/tr[4]/td/ul/li[8]/div[2]/table/tbody/tr/td')
thuinstructor9 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[4]/table/tbody/tr[4]/td/ul/li[9]/div[2]/table/tbody/tr/td')
thuinstructor10 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[4]/table/tbody/tr[4]/td/ul/li[10]/div[2]/table/tbody/tr/td')
thuinstructor11 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[4]/table/tbody/tr[4]/td/ul/li[11]/div[2]/table/tbody/tr/td')
thuinstructor12 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[4]/table/tbody/tr[4]/td/ul/li[12]/div[2]/table/tbody/tr/td')
thuinstructor13 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[4]/table/tbody/tr[4]/td/ul/li[13]/div[2]/table/tbody/tr/td')
thuinstructor14 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[4]/table/tbody/tr[4]/td/ul/li[14]/div[2]/table/tbody/tr/td')
thuinstructor15 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[4]/table/tbody/tr[4]/td/ul/li[15]/div[2]/table/tbody/tr/td')
thuinstructor16 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[4]/table/tbody/tr[4]/td/ul/li[16]/div[2]/table/tbody/tr/td')


print("\nTHURSDAY CLASSES\n")
print(thutime1.text, thuclass1, "with", thuinstructor1.text)
print(thutime2.text, thuclass2, "with", thuinstructor2.text)
print(thutime3.text, thuclass3, "with", thuinstructor3.text)
print(thutime4.text, thuclass4, "with", thuinstructor4.text)
print(thutime5.text, thuclass5, "with", thuinstructor5.text)
print(thutime6.text, thuclass6, "with", thuinstructor6.text)
print(thutime7.text, thuclass7, "with", thuinstructor7.text)
print(thutime8.text, thuclass8, "with", thuinstructor8.text)
print(thutime9.text, thuclass9, "with", thuinstructor9.text)
print(thutime10.text, thuclass10, "with", thuinstructor10.text)
print(thutime11.text, thuclass11, "with", thuinstructor11.text)
print(thutime12.text, thuclass12, "with", thuinstructor12.text)
print(thutime13.text, thuclass13, "with", thuinstructor13.text)
print(thutime14.text, thuclass14, "with", thuinstructor14.text)
print(thutime15.text, thuclass15, "with", thuinstructor15.text)
print(thutime16.text, thuclass16, "with", thuinstructor16.text)

#CODE TO FIND ALL FRIDAY CLASSES, TIMES AND INSTRUCTOR
friclass1 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[5]/table/tbody/tr[4]/td/ul/li[1]/img').get_attribute('alt')
friclass2 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[5]/table/tbody/tr[4]/td/ul/li[2]/img').get_attribute('alt')
friclass3 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[5]/table/tbody/tr[4]/td/ul/li[3]/img').get_attribute('alt')
friclass4 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[5]/table/tbody/tr[4]/td/ul/li[4]/img').get_attribute('alt')
friclass5 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[5]/table/tbody/tr[4]/td/ul/li[5]/img').get_attribute('alt')
friclass6 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[5]/table/tbody/tr[4]/td/ul/li[6]/img').get_attribute('alt')
friclass7 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[5]/table/tbody/tr[4]/td/ul/li[7]/img').get_attribute('alt')
friclass8 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[5]/table/tbody/tr[4]/td/ul/li[8]/img').get_attribute('alt')
friclass9 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[5]/table/tbody/tr[4]/td/ul/li[9]/img').get_attribute('alt')
friclass10 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[5]/table/tbody/tr[4]/td/ul/li[10]/img').get_attribute('alt')
friclass11 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[5]/table/tbody/tr[4]/td/ul/li[11]/img').get_attribute('alt')


fritime1 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[5]/table/tbody/tr[4]/td/ul/li[1]/div[1]')
fritime2 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[5]/table/tbody/tr[4]/td/ul/li[2]/div[1]')
fritime3 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[5]/table/tbody/tr[4]/td/ul/li[3]/div[1]')
fritime4 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[5]/table/tbody/tr[4]/td/ul/li[4]/div[1]')
fritime5 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[5]/table/tbody/tr[4]/td/ul/li[5]/div[1]')
fritime6 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[5]/table/tbody/tr[4]/td/ul/li[6]/div[1]')
fritime7 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[5]/table/tbody/tr[4]/td/ul/li[7]/div[1]')
fritime8 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[5]/table/tbody/tr[4]/td/ul/li[8]/div[1]')
fritime9 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[5]/table/tbody/tr[4]/td/ul/li[9]/div[1]')
fritime10 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[5]/table/tbody/tr[4]/td/ul/li[10]/div[1]')
fritime11 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[5]/table/tbody/tr[4]/td/ul/li[11]/div[1]')

friinstructor1 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[5]/table/tbody/tr[4]/td/ul/li[1]/div[2]/table/tbody/tr/td')
friinstructor2 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[5]/table/tbody/tr[4]/td/ul/li[2]/div[2]/table/tbody/tr/td')
friinstructor3 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[5]/table/tbody/tr[4]/td/ul/li[3]/div[2]/table/tbody/tr/td')
friinstructor4 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[5]/table/tbody/tr[4]/td/ul/li[4]/div[2]/table/tbody/tr/td')
friinstructor5 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[5]/table/tbody/tr[4]/td/ul/li[5]/div[2]/table/tbody/tr/td')
friinstructor6 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[5]/table/tbody/tr[4]/td/ul/li[6]/div[2]/table/tbody/tr/td')
friinstructor7 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[5]/table/tbody/tr[4]/td/ul/li[7]/div[2]/table/tbody/tr/td')
friinstructor8 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[5]/table/tbody/tr[4]/td/ul/li[8]/div[2]/table/tbody/tr/td')
friinstructor9 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[5]/table/tbody/tr[4]/td/ul/li[9]/div[2]/table/tbody/tr/td')
friinstructor10 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[5]/table/tbody/tr[4]/td/ul/li[10]/div[2]/table/tbody/tr/td')
friinstructor11 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[5]/table/tbody/tr[4]/td/ul/li[11]/div[2]/table/tbody/tr/td')
)

print("\nFRIDAY CLASSES\n")
print(fritime1.text, friclass1, "with", friinstructor1.text)
print(fritime2.text, friclass2, "with", friinstructor2.text)
print(fritime3.text, friclass3, "with", friinstructor3.text)
print(fritime4.text, friclass4, "with", friinstructor4.text)
print(fritime5.text, friclass5, "with", friinstructor5.text)
print(fritime6.text, friclass6, "with", friinstructor6.text)
print(fritime7.text, friclass7, "with", friinstructor7.text)
print(fritime8.text, friclass8, "with", friinstructor8.text)
print(fritime9.text, friclass9, "with", friinstructor9.text)
print(fritime10.text, friclass10, "with", friinstructor10.text)
print(fritime11.text, friclass11, "with", friinstructor11.text)

satclass1 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[6]/table/tbody/tr[4]/td/ul/li[1]/div[1]').get_attribute('alt')
satclass2 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[6]/table/tbody/tr[4]/td/ul/li[2]/img').get_attribute('alt')
satclass3 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[6]/table/tbody/tr[4]/td/ul/li[3]/img').get_attribute('alt')
satclass4 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[6]/table/tbody/tr[4]/td/ul/li[4]/img').get_attribute('alt')
satclass5 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[6]/table/tbody/tr[4]/td/ul/li[5]/img').get_attribute('alt')
satclass6 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[6]/table/tbody/tr[4]/td/ul/li[6]/img').get_attribute('alt')
satclass7 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[6]/table/tbody/tr[4]/td/ul/li[7]/img').get_attribute('alt')


sattime1 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[6]/table/tbody/tr[4]/td/ul/li[1]/div[1]')
sattime2 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[6]/table/tbody/tr[4]/td/ul/li[2]/div[1]')
sattime3 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[6]/table/tbody/tr[4]/td/ul/li[3]/div[1]')
sattime4 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[6]/table/tbody/tr[4]/td/ul/li[4]/div[1]')
sattime5 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[6]/table/tbody/tr[4]/td/ul/li[5]/div[1]')
sattime6 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[6]/table/tbody/tr[4]/td/ul/li[6]/div[1]')
sattime7 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[6]/table/tbody/tr[4]/td/ul/li[7]/div[1]')


satinstructor1 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[6]/table/tbody/tr[4]/td/ul/li[1]/div[2]/table/tbody/tr/td')
satinstructor2 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[6]/table/tbody/tr[4]/td/ul/li[2]/div[2]/table/tbody/tr/td')
satinstructor3 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[6]/table/tbody/tr[4]/td/ul/li[3]/div[2]/table/tbody/tr/td')
satinstructor4 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[6]/table/tbody/tr[4]/td/ul/li[4]/div[2]/table/tbody/tr/td')
satinstructor5 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[6]/table/tbody/tr[4]/td/ul/li[5]/div[2]/table/tbody/tr/td')
satinstructor6 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[6]/table/tbody/tr[4]/td/ul/li[6]/div[2]/table/tbody/tr/td')
satinstructor7 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[6]/table/tbody/tr[4]/td/ul/li[7]/div[2]/table/tbody/tr/td')


print("\nSATURDAY CLASSES\n")
print(sattime1.text, satclass1, "with", satinstructor1.text)
print(sattime2.text, satclass2, "with", satinstructor2.text)
print(sattime3.text, satclass3, "with", satinstructor3.text)
print(sattime4.text, satclass4, "with", satinstructor4.text)
print(sattime5.text, satclass5, "with", satinstructor5.text)
print(sattime6.text, satclass6, "with", satinstructor6.text)
print(sattime7.text, satclass7, "with", satinstructor7.text)

sunclass1 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[7]/table/tbody/tr[4]/td/ul/li[1]/div[1]').get_attribute('alt')
sunclass2 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[7]/table/tbody/tr[4]/td/ul/li[2]/img').get_attribute('alt')
sunclass3 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[7]/table/tbody/tr[4]/td/ul/li[3]/img').get_attribute('alt')
sunclass4 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[7]/table/tbody/tr[4]/td/ul/li[4]/img').get_attribute('alt')
sunclass5 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[7]/table/tbody/tr[4]/td/ul/li[5]/img').get_attribute('alt')
sunclass6 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[7]/table/tbody/tr[4]/td/ul/li[6]/img').get_attribute('alt')

suntime1 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[7]/table/tbody/tr[4]/td/ul/li[1]/div[1]')
suntime2 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[7]/table/tbody/tr[4]/td/ul/li[2]/div[1]')
suntime3 = driver.find_element(By.XPATH,
     '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[7]/table/tbody/tr[4]/td/ul/li[3]/div[1]')
suntime4 = driver.find_element(By.XPATH,
     '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[7]/table/tbody/tr[4]/td/ul/li[4]/div[1]')
suntime5 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[7]/table/tbody/tr[4]/td/ul/li[5]/div[1]')
suntime6 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[7]/table/tbody/tr[4]/td/ul/li[6]/div[1]')


suninstructor1 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[7]/table/tbody/tr[4]/td/ul/li[1]/div[2]/table/tbody/tr/td')
suninstructor2 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[7]/table/tbody/tr[4]/td/ul/li[2]/div[2]/table/tbody/tr/td')
suninstructor3 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[7]/table/tbody/tr[4]/td/ul/li[3]/div[2]/table/tbody/tr/td')
suninstructor4 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[7]/table/tbody/tr[4]/td/ul/li[4]/div[2]/table/tbody/tr/td')
suninstructor5 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[7]/table/tbody/tr[4]/td/ul/li[5]/div[2]/table/tbody/tr/td')
suninstructor6 = driver.find_element(By.XPATH,
    '//*[@id="divContent"]/table[2]/tbody/tr[1]/td[7]/table/tbody/tr[4]/td/ul/li[6]/div[2]/table/tbody/tr/td')

print("\nSUNDAY CLASSES\n")
print(suntime1.text, sunclass1, "with", suninstructor1.text)
print(suntime2.text, sunclass2, "with", suninstructor2.text)
print(suntime3.text, sunclass3, "with", suninstructor3.text)
print(suntime4.text, sunclass4, "with", suninstructor4.text)
print(suntime5.text, sunclass5, "with", suninstructor5.text)
print(suntime6.text, sunclass6, "with", suninstructor6.text)
