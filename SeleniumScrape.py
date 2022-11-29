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