import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Initialising driver

driver = webdriver.Chrome()

try:
    driver.get("https://tileman.io/")

    body_element = driver.find_element(By.TAG_NAME, "body")
    nickname_element = driver.find_element(By.ID, "nick")

    # setting nickname to assert dominance

    nickname_element.clear()
    nickname_element.send_keys("tldr")

    # starting the game

    body_element.send_keys(Keys.ENTER)

    # waiting 2 sec buffer (hopefully no ads idk)

    time.sleep(2)

    # control start from here

    body_element.send_keys(Keys.ARROW_UP)

    time.sleep(10)
finally:
    # quit driver to close

    driver.quit()