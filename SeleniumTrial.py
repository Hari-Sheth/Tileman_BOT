import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import mss
import cv2
import numpy as np

#Initialising driver
driver = webdriver.Chrome()
driver.maximize_window()

class Bot:
    def __init__(self, name, body_element, overlay_element, sct):
        self.name = name
        self.controller = body_element
        self.overlay = overlay_element
        self.sct = sct

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
    def __init__(self, name, body_element, overlay_element, sct):
        super().__init__(name, body_element, overlay_element, sct)
    
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

class EyeBot(Bot):
    def __init__(self, name, body_element, overlay_element, sct):
        super().__init__(name, body_element, overlay_element, sct)
    
    def run(self):
        while "Screen capturing":
            # for fps calculation
            last_time = time.time()

            # Get raw pixels from the screen, save it to a Numpy array
            # Each element img[x][y] is an rgba array
            # Example: img[0][0] = [12, 12, 12, 255]
            # Use this for logic
            img = np.array(sct.grab(monitor))

            # Display the picture
            cv2.imshow("OpenCV/Numpy normal", img)

            # Show fps
            print(f"fps: {1 / (time.time() - last_time)}")

            # Press "q" to quit (Works only on the display window)
            if cv2.waitKey(25) & 0xFF == ord("q"):
                cv2.destroyAllWindows()
                break

            if self.check_lose():
                self.controller.send_keys(Keys.RETURN)
                self.controller.send_keys(Keys.RETURN)

try:
    # Initialising website and elements
    driver.get("https://tileman.io/")

    body_element = driver.find_element(By.TAG_NAME, "body")
    overlay_element = driver.find_element(By.ID, "overlay")
    nickname_element = driver.find_element(By.ID, "nick")

    # setting nickname to assert dominance
    nickname = "ICanSee"
    nickname_element.clear()
    nickname_element.send_keys(nickname)

    # starting the game
    body_element.send_keys(Keys.ENTER)

    with mss.MSS() as sct:
        # Setting for screen capture
        monitor = {
            "top": 220,
            "left": 0,
            "width": 1920,
            "height": 850
        }

        # Initialising the bot
        bot = EyeBot(nickname, body_element, overlay_element, sct)

        # waiting 2 sec buffer (hopefully no ads idk)
        time.sleep(2)

        # control start from here
        bot.run()

finally:
    # quit driver to close
    driver.quit()
