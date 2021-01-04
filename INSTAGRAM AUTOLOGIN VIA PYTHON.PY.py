###        _______________________________________________________
###        <AUTOMATE THE INSTAGRAM ON CHROME DRIVER FOR AUTO-LOGIN>
###        -------------------------------------------------------
###                      \   ^__^
###                        \  (oo)\_______
###                          (__)\       )\/\/\
###                              ||----w |
###                              ||     ||


########### OPEN TERMINAL OR CMD AND TYPE: "pip install selenium" ##########

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

########### #ADD YOUR CHROMEDRIVER.EXE LOCATION ##########

chromedr = r"C:\Users\KIIT\Documents\programming\chromedriver.exe"
driver = webdriver.Chrome(chromedr)
driver.get("https://instagram.com/")
time.sleep(2)

########## INSPECT THE USERNAME BLANK SPACE COPY SELECTOR AND PASTE  ##########

username = driver.find_element_by_css_selector("#loginForm > div > div:nth-child(1) > div > label > input")
username.clear()
username.send_keys("ENTER USERNAME HERE")
time.sleep(1)

########## INSPECT THE PASSWORD BLANK SPACE COPY SELECTOR AND PASTE  ##########

username.send_keys(Keys.TAB)
psw = driver.find_element_by_css_selector("#loginForm > div > div:nth-child(2) > div > label > input")
psw.clear()
psw.send_keys("ENTER PASSWORD HERE")
psw.send_keys(Keys.RETURN)
time.sleep(3)

########## INSPECT THE NOTNOW BUTTON COPY SELECTOR AND PASTE  ##########

not_now1= driver.find_element_by_css_selector("#react-root > section > main > div > div > div > div > button")
not_now1.click()
time.sleep(3)

########## INSPECT THE NOTNOW BUTTON COPY SELECTOR AND PASTE  ##########

not_now2= driver.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm")
not_now2.click()
