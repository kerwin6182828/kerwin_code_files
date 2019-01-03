from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


browser = webdriver.Chrome()
try:
    # for i in range(1, 1000):
        # browser.get("https://upassport.lianjia.com/freshCaptch?t=1542016511868")
        # browser.save_screenshot("./code_img/t%s.jpg"%i)

    browser.get("https://upassport.lianjia.com/freshCaptch?t=1542016511868")
    # browser.save_screenshot("xx63.jpg")
    # img = browser.find_element_by_css_selector("img")
    # location = img.location
    # print(location)
    # size = img.size
    # print(size)
    # top, bottom, left, right = location["y"], location["y"]+size["height"], location["x"], location["x"]+size["width"]
    # screenshot = browser.get_screenshot()
    # captcha = screenshot.crop((left, top, right, bottom))
    # print(captcha)
    #
    #


    login_btn = browser.find_element_by_css_selector(".btn-login.bounceIn.actLoginBtn")
    login_btn.send_keys(Keys.ENTER)
    wait = WebDriverWait(browser, 10)
    time.sleep(5)
    # wait.until(EC.presence_of_element_located((BY.ID, "content_left")))
finally:
    browser.close()
print(3)



# <span class="reg">登录</span>
# body > header > div > div > div.fr.nav > div.fr.login > div > div.login-panel.typeUserInfo > div > span > a.btn-login.bounceIn.actLoginBtn > span
