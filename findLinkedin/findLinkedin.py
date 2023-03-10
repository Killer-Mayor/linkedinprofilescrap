import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
ser = Service("/Users/shreyanish/Dev/pythonXmentorrelations/findLinkedin/chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

driver.get("https://github.com/shreyanish")

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("findLinkedin/creds.json", scope)
client = gspread.authorize(creds)

sheet = client.open("pytest").sheet1

