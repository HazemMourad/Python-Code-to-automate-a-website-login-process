from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc 

options = uc.ChromeOptions() 
options.add_argument("--start-maximized")
driver = uc.Chrome(use_subprocess=True, options=options) 
driver.get("https://secure.sahibinden.com/giris?fbclid=IwAR2X8DgZ0tm7F-ap0-cV5-jIeqZUGmWg1E_r9YXPoCz4sfIvATLd9mGD3hg")
divCook = driver.find_element(By.XPATH, "//*[@id='onetrust-banner-sdk']/div/div[1]")
if divCook.is_displayed():
        driver.find_element(By.XPATH, "//*[@id='onetrust-accept-btn-handler']").click()
email_field = driver.find_element(By.XPATH, "//*[@id='loginSelectionPageEmail']")
email_field.send_keys("hazemmgaber3110@gmail.com")
email_field.send_keys(Keys.ENTER)
password_field = driver.find_element(By.XPATH, "//*[@id='password']")
password_field.send_keys("Roadstar1988")
password_field.send_keys(Keys.ENTER)
wait = WebDriverWait(driver, 180)
