# %%
from linkedin_scraper import actions
import selenium
import pandas
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


# %%
#set the driver
driver = webdriver.Chrome()

# %%
#query college of interest and clean up for proper structure
uni = input('Name of organization').upper()
uni = uni.replace(' ', '%20')
#navigate to webpage
driver.get('https://www.linkedin.com/search/results/people/?keywords=' + uni + '&origin=SWITCH_SEARCH_VERTICAL&sid=Wkf')
time.sleep(3)

user = ''
password = ''

actions.login(driver, user, password)
driver.get('https://www.linkedin.com/search/results/people/?keywords=' + uni + '&origin=SWITCH_SEARCH_VERTICAL&sid=Wkf')
time.sleep(3)

# %%
names = []
pidx = 1
while pidx <= 100:
    idx = 1
    while idx <= 11:
        time.sleep(0.5)
        name_element = driver.find_elements(By.XPATH, f"//div/ul/li[{idx}]/div/div/div/div[2]/div[1]/div[1]/div/span[1]/span/a/span/span[1]")
        print(name_element[0].text)
        names.append(name_element[0].text)
        if idx == 2:
            idx += 2
        else:
            idx += 1
        if idx == 11:
            break

    if pidx == 1:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        next_elem = driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div[2]/div/div[1]/main/div/div/div[5]/div/div/button[2]")
        time.sleep(2)
        next_elem.click()
        time.sleep(2)
        pidx += 1
    else: 
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        next_elem = driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div[2]/div/div[1]/main/div/div/div[2]/div/div[2]/div/button[2]")
        time.sleep(2)
        next_elem.click()
        time.sleep(2)
        pidx += 1


