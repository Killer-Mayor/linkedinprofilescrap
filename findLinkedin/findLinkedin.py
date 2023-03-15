import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

import csv

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time

from bs4 import BeautifulSoup


#connecting google sheets
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("findLinkedin/creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open("pytest").sheet1

#initianting web driver
ser = Service("/Users/shreyanish/Dev/pythonXmentorrelations/findLinkedin/chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)
wait = WebDriverWait(driver, 30)

#signing into linkedin

def signin_linkedin():
    driver.get("https://www.linkedin.com/")

    username_input = driver.find_element("id", "session_key")
    username_input.send_keys("storieape420@gmail.com")
    username_input.submit()
    time.sleep(1)

    password_input = driver.find_element("id", "session_password")
    password_input.send_keys("StorieApe@19818525")
    password_input.submit()
    time.sleep(10)

def search_profile(name, company, i):

    search_term = "site:linkedin.com/in/ and {Name} {Company} people".format(Name = name, Company = company)

    search_bar = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="tsf"]/div[1]/div[1]/div[2]/div/div[2]/input'))
    )
    search_bar.clear()
    search_bar.send_keys(search_term)
    search_bar.send_keys(Keys.ENTER)
    

    print(search_term)
    
    
    profile_div = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="rso"]/div[1]/div/div/div[1]/div/a'))
    )
    profile_url = profile_div.get_attribute('href')
    pprint(profile_url)

    sheet.update_cell(i,5,profile_url)
    
    

with open("findLinkedin/cxosfinal copy.csv", "r") as file:
    csvreader = csv.DictReader(file)

    #signin_linkedin()

    driver.get("https://www.google.com/search?q=conquest+bits+pilani&oq=conquest+bits+pilani&aqs=chrome..69i57j0i390.4657j0j7&sourceid=chrome&ie=UTF-8")
    rowcount = 2
    
    for row in csvreader:
        name = row['Name']
        print(name)
        company = row['Company']
        print(company)
        time.sleep(5)
        try:
            search_profile(name = name, company = company, i=rowcount)
        except:
            continue

        rowcount = rowcount + 1
        
    

    
