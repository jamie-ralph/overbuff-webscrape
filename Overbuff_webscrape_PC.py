### Overbuff webscraper [PC Only] ###

# Import modules
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
import datetime
import re

now = datetime.datetime.now()

# Fancy chrome stuff  - ad block
path_to_extension = r'C:/Users/james/OneDrive/Desktop/4.12.0_0'
chrome_options = Options()
chrome_options.add_argument('load-extension=' + path_to_extension)

# Define URL

url = "https://www.overbuff.com/heroes"

browser = webdriver.Chrome("C:/Users/james/OneDrive/Desktop.chromedriver.exe",
            chrome_options=chrome_options)

browser.create_options()

browser.get(url)

time.sleep(2)


# Change to a week view

this_week = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div/div[2]/div/div[1]/div/div[1]/div[1]")

this_week.click()


# ALL

hero = []
role = []
pick = []
win = []
tie = []
fire = []



for i in range(1, 31):
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
    
    f = browser.find_element_by_xpath(xpath_fire).text,
    
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
        'Rank': "All",
        'Date': str(now)
        })

# BRONZE

bronze_button = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/div/div[1]/div/div[5]/div[2]")

bronze_button.click()

hero = []
role = []
pick = []
win = []
tie = []
fire = []



for i in range(1, 31):
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
    
    f = browser.find_element_by_xpath(xpath_fire).text,
    
    hero.append(h)
    role.append(r)
    pick.append(p)
    win.append(w)
    tie.append(t)
    fire.append(f)
    
    time.sleep(2)

Bronze = pd.DataFrame({
        'Hero': hero,
        'Role': role,
        'Pick_rate': pick,
        'Win_rate': win,
        'Tie_Rate': tie,
        'On_fire': fire,
        'Platform': "PC",
        'Rank': "Bronze",
        'Date': str(now)
        })
    
# SILVER

silver_button = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/div/div[1]/div/div[5]/div[3]")

silver_button.click()

hero = []
role = []
pick = []
win = []
tie = []
fire = []



for i in range(1, 31):
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
    
    f = browser.find_element_by_xpath(xpath_fire).text,
    
    hero.append(h)
    role.append(r)
    pick.append(p)
    win.append(w)
    tie.append(t)
    fire.append(f)
    
    time.sleep(2)

Silver = pd.DataFrame({
        'Hero': hero,
        'Role': role,
        'Pick_rate': pick,
        'Win_rate': win,
        'Tie_Rate': tie,
        'On_fire': fire,
        'Platform': "PC",
        'Rank': "Silver",
        'Date': str(now)
        })

# GOLD
    
gold_button = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/div/div[1]/div/div[5]/div[4]")

gold_button.click()

hero = []
role = []
pick = []
win = []
tie = []
fire = []



for i in range(1, 31):
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
    
    f = browser.find_element_by_xpath(xpath_fire).text,
    
    hero.append(h)
    role.append(r)
    pick.append(p)
    win.append(w)
    tie.append(t)
    fire.append(f)
    
    time.sleep(2)

Gold = pd.DataFrame({
        'Hero': hero,
        'Role': role,
        'Pick_rate': pick,
        'Win_rate': win,
        'Tie_Rate': tie,
        'On_fire': fire,
        'Platform': "PC",
        'Rank': "Gold",
        'Date': str(now)
        })

browser.close()

# %% Next: Plat to GM

# Set up and CLICK WEEK PLEASE REMEMBER TO CLICK WEEK

# Fancy chrome stuff  - ad block
path_to_extension = r'C:/Users/james/OneDrive/Desktop/3.41.0_0'
chrome_options = Options()
chrome_options.add_argument('load-extension=' + path_to_extension)

url = "https://www.overbuff.com/heroes"
browser = webdriver.Chrome("C:/Users/james/drivers/chromedriver.exe", chrome_options=chrome_options)

browser.create_options()

browser.get(url)

time.sleep(2)

this_week = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div/div[2]/div/div[1]/div/div[1]/div[1]")

this_week.click()

time.sleep(2)

# PLATINUM

plat_button = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/div/div[1]/div/div[5]/div[5]")

plat_button.click()

time.sleep(3)

hero = []
role = []
pick = []
win = []
tie = []
fire = []

for i in range(1, 31):
    xpath_hero = '/html/body/div[1]/div[3]/div/div/div/div[2]/table/tbody/tr[' + str(i) + ']/td[2]/span/a'
    
    xpath_role = '/html/body/div[1]/div[3]/div/div/div/div[2]/table/tbody/tr[' + str(i) + ']/td[2]/span/small'
    
    xpath_pick = '/html/body/div[1]/div[3]/div/div[2]/div/div[2]/table/tbody/tr[' + str(i) + ']/td[3]/span'
    
    xpath_win = '/html/body/div[1]/div[3]/div/div/div/div[2]/table/tbody/tr[' + str(i) + ']/td[4]/span'
    
    xpath_tie = '/html/body/div[1]/div[3]/div/div/div/div[2]/table/tbody/tr[' + str(i) + ']/td[5]/span'
    
    xpath_fire = '/html/body/div[1]/div[3]/div/div/div/div[2]/table/tbody/tr[' + str(i) + ']/td[6]/span'
    
    h = browser.find_element_by_xpath(xpath_hero).text
    
    r = browser.find_element_by_xpath(xpath_role).text
    
    p = browser.find_element_by_xpath(xpath_pick).text
    
    w = browser.find_element_by_xpath(xpath_win).text
    
    t = browser.find_element_by_xpath(xpath_tie).text
    
    f = browser.find_element_by_xpath(xpath_fire).text,
    
    hero.append(h)
    role.append(r)
    pick.append(p)
    win.append(w)
    tie.append(t)
    fire.append(f)
    
    time.sleep(2)

Plat = pd.DataFrame({
        'Hero': hero,
        'Role': role,
        'Pick_rate': pick,
        'Win_rate': win,
        'Tie_Rate': tie,
        'On_fire': fire,
        'Platform': "PC",
        'Rank': "Platinum",
        'Date': str(now)
        })

browser.close()

# %% Diamond
path_to_extension = r'C:/Users/james/OneDrive/Desktop/3.41.0_0'
chrome_options = Options()
chrome_options.add_argument('load-extension=' + path_to_extension)

url = "https://www.overbuff.com/heroes"
browser = webdriver.Chrome("C:/Users/james/drivers/chromedriver.exe", chrome_options=chrome_options)

browser.create_options()

browser.get(url)

  # Change to a week view

this_week = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div/div[2]/div/div[1]/div/div[1]/div[1]")

this_week.click()

time.sleep(1)  
    
# Diamond
    
diamond_button = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/div/div[1]/div/div[5]/div[6]")

diamond_button.click()

hero = []
role = []
pick = []
win = []
tie = []
fire = []



for i in range(1, 31):
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
    
    f = browser.find_element_by_xpath(xpath_fire).text,
    
    hero.append(h)
    role.append(r)
    pick.append(p)
    win.append(w)
    tie.append(t)
    fire.append(f)
    
    time.sleep(2)

Diamond = pd.DataFrame({
        'Hero': hero,
        'Role': role,
        'Pick_rate': pick,
        'Win_rate': win,
        'Tie_Rate': tie,
        'On_fire': fire,
        'Platform': "PC",
        'Rank': "Diamond",
        'Date': str(now)
        })
browser.close()
# %% Master

path_to_extension = r'C:/Users/james/OneDrive/Desktop/3.41.0_0'
chrome_options = Options()
chrome_options.add_argument('load-extension=' + path_to_extension)

url = "https://www.overbuff.com/heroes"
browser = webdriver.Chrome("C:/Users/james/drivers/chromedriver.exe", chrome_options=chrome_options)

browser.create_options()

browser.get(url)

  # Change to a week view

this_week = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div/div[2]/div/div[1]/div/div[1]/div[1]")

this_week.click()

time.sleep(1)  
    
master_button = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/div/div[1]/div/div[5]/div[7]")

master_button.click()

time.sleep(3)

hero = []
role = []
pick = []
win = []
tie = []
fire = []



for i in range(1, 31):
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
    
    f = browser.find_element_by_xpath(xpath_fire).text,
    
    hero.append(h)
    role.append(r)
    pick.append(p)
    win.append(w)
    tie.append(t)
    fire.append(f)
    
    time.sleep(2)

Master = pd.DataFrame({
        'Hero': hero,
        'Role': role,
        'Pick_rate': pick,
        'Win_rate': win,
        'Tie_Rate': tie,
        'On_fire': fire,
        'Platform': "PC",
        'Rank': "Master",
        'Date': str(now)
        })
    
# Grandmaster

gm_button = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/div/div[1]/div/div[5]/div[8]")

gm_button.click()

time.sleep(5)

hero = []
role = []
pick = []
win = []
tie = []
fire = []



for i in range(1, 31):
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
    
    f = browser.find_element_by_xpath(xpath_fire).text,
    
    hero.append(h)
    role.append(r)
    pick.append(p)
    win.append(w)
    tie.append(t)
    fire.append(f)
    
    time.sleep(2)

Grandmaster = pd.DataFrame({
        'Hero': hero,
        'Role': role,
        'Pick_rate': pick,
        'Win_rate': win,
        'Tie_Rate': tie,
        'On_fire': fire,
        'Platform': "PC",
        'Rank': "Grandmaster",
        'Date': str(now)
        })

browser.close()

# %% Data merge and cleanse
files = [All, Bronze, Silver, Gold, Plat, Diamond, Master, Grandmaster]

Overbuff_data = pd.concat(files)

if len(Overbuff_data) == 240:
    print("Expected rows returned")
else:
    print("Error in row numbers")

Overbuff_data['Tie_Rate'] = Overbuff_data['Tie_Rate'].apply(lambda x: re.search( r'\d+\.*\d*', x).group(0))

Overbuff_data['Pick_rate'] = Overbuff_data['Pick_rate'].apply(lambda x: re.search( r'\d+\.*\d*', x).group(0))

Overbuff_data['Win_rate'] = Overbuff_data['Win_rate'].apply(lambda x: re.search( r'\d+\.*\d*', x).group(0))

Overbuff_data['On_fire'] = Overbuff_data['On_fire'].apply(lambda x: re.search( r'\d+\.*\d*', str(x)).group(0))

# %% Write to csv

filename = "Overbuff_scraped_" + datetime.datetime.today().strftime('%Y-%m-%d') + "_PC.csv"

Overbuff_data.to_csv(filename)