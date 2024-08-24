
##Install required libraries
#pip install selenium

#Import libraries
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.Exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options


states= ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut',
          'Delaware', 'Florida', 'Georgia', 'Idaho','Illinois', 'Indiana', 'Iowa', 'Kansas',
          'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota',
          'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire','New Jersey', 
          'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma',
          'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee',
          'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'West Virginia',
          'Wisconsin', 'Wyoming']

# URL
temprature_url= "https://www.ncei.noaa.gov/cag/county/mapping/1/tavg/202207/7/value"

##Set the driver for chrome browser
browser = webdriver.Chrome()
browser.get(temprature_url)

##Get states from NCEI website 
state_element= browser.find_element('id', 'location')
state_select= Select(state_element)

#Loop through each state and download the corresponding .csv file
for state in states:
    state_select.select_by_visible_text(state)
    browser.implicitly_wait(10)
    browser.find_element('id', "submit").click();
    browser.implicitly_wait(15)
    browser.find_element('id', 'csv-download').click()