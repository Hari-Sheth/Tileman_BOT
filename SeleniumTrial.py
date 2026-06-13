# Imports 
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.color import Color
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import random
import mss
import cv2
import numpy as np

class Bot:
    def __init__(self, name, body_element, after_element, sct):
        self.name = name
        self.controller = body_element
        self.after = after_element
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
        return self.after.value_of_css_property("display") == "block"

    def run(self):
        pass

class RandomBot(Bot):
    def __init__(self, name, body_element, after_element, sct):
        super().__init__(name, body_element, after_element, sct)
    
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
                break
                # self.controller.send_keys(Keys.RETURN)
                # self.controller.send_keys(Keys.RETURN)

class EyeBot(Bot):
    def __init__(self, name, body_element, after_element, sct):
        super().__init__(name, body_element, after_element, sct)
    
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
                break
                # self.controller.send_keys(Keys.RETURN)
                # self.controller.send_keys(Keys.RETURN)

#Initialising driver
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--remote-debugging-pipe")
chrome_options.binary_location = "/usr/bin/google-chrome"
service = Service(executable_path='/usr/bin/chromedriver')
driver = webdriver.Chrome(service=service, options=chrome_options)
# driver = webdriver.Chrome()
driver.maximize_window()

try:
    driver.get("https://tileman.io/")
    print("Starting sleep...")
    time.sleep(5)
    number_of_turns = 3
    print("good morning sleepy heads")
    try:
        consent_element = driver.find_element(By.CLASS_NAME,"fc-consent-root")
        print("consent_element found!")
        consent_button = driver.find_element(By.CLASS_NAME,"fc-button.fc-cta-do-not-consent.fc-secondary-button")
        print("consent_button found!")
        consent_button.click()
        print("consent_button clicked!")
    except Exception as e:
        print("Something went wrong with consent element?")
        # print(str(e))
    finally:
        print("Time to actually do something!")
        intro_element = driver.find_element(By.ID, "intro")
        server_east_asia_button = driver.find_element(By.ID,"rgasia")
        server_east_asia_button.click()
        mode_extreme_speed_button = driver.find_element(By.ID, "mofast4x")
        mode_extreme_speed_button.click()
        overlay_element = driver.find_element(By.ID, "overlay")
        game_element = driver.find_element(By.ID, "game")
        after_element = driver.find_element(By.ID, "after")
        body_element = driver.find_element(By.TAG_NAME, "body")
        nickname_element = driver.find_element(By.ID, "nick")
    
        while number_of_turns: 
            try:
                consent_element = driver.find_element(By.CLASS_NAME,"fc-consent-root")
                print("consent_element found!")
                consent_button = driver.find_element(By.CLASS_NAME,"fc-button.fc-cta-do-not-consent.fc-secondary-button")
                print("consent_button found!")
                consent_button.click()
                print("consent_button clicked!")
            except Exception as e:
                print("Something went wrong with consent element? maybe I clicked it already")
                # print(str(e))
            finally:
                nickname = "ooooo"

                # setting nickname to assert dominance

                nickname_element.clear()
                nickname_element.send_keys(nickname)

                # starting the game

                body_element.send_keys(Keys.ENTER)
                
                print("time to start playing this thing!")
                with mss.MSS() as sct:
                    # Setting for screen capture
                    monitor = {
                        "top": 220,
                        "left": 0,
                        "width": 1920,
                        "height": 850
                    }
                    bot = RandomBot(nickname, body_element, after_element, sct)

                    # waiting 2 sec buffer (hopefully no ads idk)
                    time.sleep(2) 

                    while game_element.value_of_css_property("display") != "block":
                        print("waiting")
                    # control start from here
                    while game_element.value_of_css_property("display") == "block" and after_element.value_of_css_property("display") == "none":
                        bot.run()
                    if after_element.value_of_css_property("display") == "block":
                        try:
                            continue_button = driver.find_element(By.ID, "conti")
                            continue_button.click()
                        except Exception as e:
                            print(str(e))
                    print(f"I think we're done, {number_of_turns-1} turns left")
                number_of_turns -= 1
        time.sleep(10)
finally:
    # quit driver to close

    driver.quit()