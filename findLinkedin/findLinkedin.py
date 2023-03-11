import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time

ser = Service("/Users/shreyanish/Dev/pythonXmentorrelations/findLinkedin/chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

driver.get("https://linkedin.com")

username_input = driver.find_element("id", "session_key")
username_input.send_keys("storieape420@gmail.com")
username_input.submit()

password_input = driver.find_element("id", "session_password")
password_input.send_keys("StorieApe@19818525")
password_input.submit()

signin_button = driver.find_element("type", "submit")  
signin_button.click()


'''try:
    search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS,  "search-global-typeahead__input"))
    )
    search.send_keys("shrey anish")
    search.submit()

except:
    driver.quit()'''


scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("findLinkedin/creds.json", scope)
client = gspread.authorize(creds)

sheet = client.open("pytest").sheet1
