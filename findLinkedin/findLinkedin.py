import gspread
from google.oauth2 import service_account 

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
import time

#what is scope
#scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

#authorisation
credentials = service_account.Credentials.from_service_account_file("findLinkedin/creds.json")
client = gspread.authorize(credentials=credentials)

scoped_credentials = credentials.with_scopes(['https://www.googleapis.com/auth/cloud-platform'])

#getting the sheet
sheet = client.open("pytest").sheet1

#playing with the sheet

#row = sheet.row_values(3)
#col = sheet.col_values(2)
#cell = sheet.cell(2,2).value
#sheet.insert_row(row, 3)
#sheet.delete_row(3) 
#can do the same with columns
#sheet.update_cell(2,2, "anish")


#search

driver_path = "/Users/shreyanish/Dev/pythonXmentorrelations/findLinkedin/chromedriver_mac64.zip"
brave_path = "/Applications/Brave Browser.app"


options = ChromeOptions()
options.binary_location = brave_path
driver = webdriver.Chrome(executable_path=driver_path, chrome_options=options)
driver.get("https://www.linkedin.com/")

email = "storieape420@gmail.com"
password = "StorieApe@19818525"

driver.find_element_by_id("session_key").send_keys(email)
driver.find_element_by_id("session_password").send_keys(password)
driver.find_element_by_class_name("sign-in-form__submit-button").click()

search_term = "kunal shah cred"
driver.find_element_by_xpath("//input[contains(@class,'search-global-typeahead__input')]").send_keys(search_term)
driver.find_element_by_xpath("//button[contains(@class,'search-global-typeahead__button')]").click()

time.sleep(3) # Wait for the page to load
search_results = driver.find_elements_by_xpath("//li[contains(@class,'search-result__occluded-item')]")
first_result = search_results[0]
profile_link = first_result.find_element_by_xpath(".//a").get_attribute("href")

print(profile_link)

driver.quit()