import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")

opt.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,  # disabling/enabling camera and shit manually
    "profile.default_content_setting_values.geolocation": 2,
    "profile.default_content_setting_values.notifications": 2
})

browser = webdriver.Chrome(options=opt, executable_path=r'C:\Users\Shaun\Downloads\chromedriver_win32'
                                                        r'\chromedriver.exe')


def joinclass(meetcode, username, pswd):
    browser.get('https://meet.google.com/landing?authuser=1')

    time.sleep(3)

    browser.find_element_by_id('identifierId').send_keys(username)  # entering username
    browser.find_element_by_class_name('VfPpkd-RLmnJb').click()

    time.sleep(3)

    browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(pswd)  # entering password
    browser.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]').click()

    time.sleep(4)

    browser.find_element_by_class_name('cmvVG').click()
    browser.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/span/div/div[2]/div[1]/div[1]/input').send_keys(
        meetcode)  # entering meeting code

    time.sleep(3)

    browser.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/span/div/div[4]/div[2]/div/span/span').click()

    time.sleep(5)

    pyautogui.hotkey('ctrl', 'd')  # cam off

    time.sleep(2)

    pyautogui.hotkey('ctrl', 'e')  # mic off

    time.sleep(2)

    browser.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[6]/div[3]/div/div/div[2]/div/div[1]/div['
                                  '2]/div/div[2]/div/div[1]/div[1]/span/span').click()


def leaveclass():
    browser.quit()
