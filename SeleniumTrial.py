import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random

#Initialising driver

driver = webdriver.Chrome()

class Bot:
    def __init__(self, name, body_element, overlay_element):
        self.name = name
        self.controller = body_element
        self.overlay = overlay_element

    def up(self):
        self.controller.send_keys(Keys.ARROW_UP)

    def down(self):
        self.controller.send_keys(Keys.ARROW_DOWN)

    def left(self):
        self.controller.send_keys(Keys.ARROW_LEFT)

    def right(self):
        self.controller.send_keys(Keys.ARROW_RIGHT)

    def check_lose(self):
        return self.overlay.get_dom_attribute("style") == "display: block;"

    def run(self):
        pass

class RandomBot(Bot):
    def __init__(self, name, body_element, overlay_element):
        super().__init__(name, body_element, overlay_element)
    
    def run(self):
        while True:
            c = random.randint(1, 4)

            if c == 1:
                self.up()
            elif c == 2:
                self.down()
            elif c == 3:
                self.left()
            else:
                self.right()

            if self.check_lose():
                self.controller.send_keys(Keys.RETURN)
                self.controller.send_keys(Keys.RETURN)

try:
    driver.get("https://tileman.io/")

    body_element = driver.find_element(By.TAG_NAME, "body")
    overlay_element = driver.find_element(By.ID, "overlay")
    nickname_element = driver.find_element(By.ID, "nick")
    nickname = "Bhiku"

    # setting nickname to assert dominance

    nickname_element.clear()
    nickname_element.send_keys(nickname)

    # starting the game

    body_element.send_keys(Keys.ENTER)

    bot = RandomBot(nickname, body_element, overlay_element)

    # waiting 2 sec buffer (hopefully no ads idk)

    time.sleep(2)

    # control start from here
    bot.run()

    time.sleep(5)
finally:
    # quit driver to close

    driver.quit()