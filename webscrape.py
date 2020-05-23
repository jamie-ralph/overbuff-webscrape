#%%
### Overbuff webscraper [PC Only] ###
# Import modules
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
import datetime
import re

# Fancy chrome stuff  - ad block
path_to_extension = r'C:/Users/james/OneDrive/Desktop/4.12.0_0'
chrome_options = Options()
chrome_options.add_argument('load-extension=' + path_to_extension)

# Define URL and webdriver
url = "https://www.overbuff.com/heroes"
browser = webdriver.Chrome("C:/Users/james/OneDrive/Desktop/chromedriver.exe",
            chrome_options=chrome_options)

# Open the browser, install adblock, and navigate to www.overbuff.com
browser.create_options()
browser.get(url)
time.sleep(5)

# Now to turn this bloody code into a function

this_week_button = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div/div[2]/div/div[1]/div/div[1]/div[1]")

this_week_button.click()

def scrape_overbuff(rank):
    hero = []
    role = []
    pick = []
    win = []
    tie = []
    fire = []


    for i in range(1, 32):
        xpath_hero = '/html/body/div[1]/div[3]/div/div/div/div[2]/table/tbody/tr[' + str(i) + ']/td[2]/span/a'
        xpath_role = '/html/body/div[1]/div[3]/div/div[2]/div/div[2]/table/tbody/tr[' + str(i) + ']/td[2]/span/small'
        
        xpath_pick = '/html/body/div[1]/div[3]/div/div[2]/div/div[2]/table/tbody/tr[' + str(i) + ']/td[3]/span'
        
        xpath_win = '/html/body/div[1]/div[3]/div/div[2]/div/div[2]/table/tbody/tr[' + str(i) + ']/td[4]/span'
        
        xpath_tie = '/html/body/div[1]/div[3]/div/div/div/div[2]/table/tbody/tr[' + str(i) + ']/td[5]/span'
        
        xpath_fire = '/html/body/div[1]/div[3]/div/div/div/div[2]/table/tbody/tr[' + str(i) + ']/td[6]/span'
        
        h = browser.find_element_by_xpath(xpath_hero).text
        
        r = browser.find_element_by_xpath(xpath_role).text
        
        p = browser.find_element_by_xpath(xpath_pick).text
        
        w = browser.find_element_by_xpath(xpath_win).text
        
        t = browser.find_element_by_xpath(xpath_tie).text
        
        f = browser.find_element_by_xpath(xpath_fire).text
        
        hero.append(h)
        role.append(r)
        pick.append(p)
        win.append(w)
        tie.append(t)
        fire.append(f)
        
        time.sleep(2)

    All = pd.DataFrame({
            'Hero': hero,
            'Role': role,
            'Pick_rate': pick,
            'Win_rate': win,
            'Tie_Rate': tie,
            'On_fire': fire,
            'Platform': "PC",
            'Rank': rank,
            'Date': str(now)
            })
    
    print("Done")

    time.sleep(2)

    return All

# Get All PC

All = scrape_overbuff('All')

# Bronze

bronze_button = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/div/div[1]/div/div[5]/div[2]")
bronze_button.click()
Bronze = scrape_overbuff('Bronze')

# Silver

silver_button = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/div/div[1]/div/div[5]/div[3]")
silver_button.click()
Silver = scrape_overbuff('Silver')

# Gold

gold_button = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/div/div[1]/div/div[5]/div[4]")
gold_button.click()
Gold = scrape_overbuff('Gold')

# Platinum

plat_button = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/div/div[1]/div/div[5]/div[5]")
plat_button.click()
Platinum = scrape_overbuff('Platinum')

# Diamond

diamond_button = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/div/div[1]/div/div[5]/div[6]")
diamond_button.click()
Diamond = scrape_overbuff('Diamond')

# Master

master_button = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/div/div[1]/div/div[5]/div[7]")
master_button.click()
Master = scrape_overbuff('Master')

# Grandmaster

gm_button = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/div/div[1]/div/div[5]/div[8]")
gm_button.click()
Grandmaster = scrape_overbuff('Grandmaster')
# %%

df_overbuff_pc = pd.concat([All, Bronze, Silver, Gold, Platinum, Diamond, Master, Grandmaster])

# %%
df_overbuff_pc.to_csv("df_overbuff_pc.csv")

# %%
