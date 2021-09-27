import os

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pyfiglet
from time import sleep
from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '16675686'
API_KEY = 'zVxKtmF1mjjWO5m9oTrqkHlv'
SECRET_KEY = 'tWZgTGiGGkUBxzaDWYY5g9OltwNRZXLD'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

def ocr(n,chrome):
    n += 1
    filePath = is_captcha(chrome)
    if n <= 5:
        if filePath:
            """ 调用通用文字识别（高精度版） """
            result = client.basicAccurate(get_file_content(filePath))
            words_result = result['words_result'][0]['words']
            sleep(2)
            chrome.find_element_by_xpath('//*[@id="main"]/form/div/div/div/input').send_keys(words_result)
            sleep(1)
            chrome.find_element_by_xpath('//*[@id="main"]/form/div/div/div/div/button').click()

            ocr(n, chrome)

    else:
        print('验证码验证失败！')

def loop1(driver):
    global i
    sleep(10)
    try:
        driver.find_element_by_xpath("//*[@id=\"main\"]/div/div[4]/div/button").click()
    except:
        print("You didn't solve the captcha yet. Need to refresh to avoid endless loop.")
        driver.refresh()
        loop1(driver)
    try:
        sleep(2)
        driver.find_element_by_xpath("//*[@id=\"sid4\"]/div/form/div/input").send_keys(vidUrl)
        sleep(1)
        driver.find_element_by_xpath("//*[@id=\"sid4\"]/div/form/div/div/button").click()
        sleep(2)
        driver.find_element_by_xpath("//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9V\"]/div[1]/div/form/button").click()
        sleep(10)
        driver.refresh()
        i += 1
        total = i * 500
        print("Views success delivered! Total", total,"views")
        sleep(360)
        loop1(driver)
    except:
        print("A generic error occurred. Now will retry again")
        driver.refresh()
        sleep(20)
        loop1(driver)

def loop2(driver):
    sleep(10)
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[2]/div/button").click()
    except:
        print("You didn't solve the captcha yet. Need to refresh to avoid endless loop.")
        driver.refresh()
        loop2(driver)
    try:
        sleep(2)
        driver.find_element_by_xpath("/html/body/div[4]/div[3]/div/form/div/input").send_keys(vidUrl)
        sleep(1)
        driver.find_element_by_xpath("/html/body/div[4]/div[3]/div/form/div/div/button").click()
        sleep(10)
        driver.find_element_by_xpath("/html/body/div[4]/div[3]/div/div/div[1]/div/form/button").click()
        sleep(10)
        hearts = driver.find_element_by_xpath('//*[@id="c2VuZE9nb2xsb3dlcnNfdGlrdG9r"]/span').text
        sleep(55)
        print(hearts," Success delivered! Thank me with a $ 1 donation on GitHub")
        sleep(100)
        driver.refresh()
        sleep(200)
        loop2(driver)
    except:
        print("A generic error occurred. Now will retry again")
        driver.refresh()
        sleep(355)
        loop2(driver)

def loop3(driver):
    sleep(10)
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[3]/div/button").click()
    except:
        print("You didn't solve the captcha yet. Need to refresh to avoid endless loop.")
        driver.refresh()
        loop2(driver)
    try:
        sleep(2)
        driver.find_element_by_xpath("/html/body/div[4]/div[4]/div/form/div/input").send_keys(vidUrl)
        sleep(1)
        driver.find_element_by_xpath("/html/body/div[4]/div[4]/div/form/div/div/button").click()
        sleep(5)
        driver.find_element_by_xpath("/html/body/div[4]/div[4]/div/div/div/div/div[1]/div/form/button").click()
        sleep(5)
        driver.find_element_by_xpath("/html/body/div[4]/div[4]/div/div/div/div/form/ul/li/div/button").click()
        sleep(47)
        driver.refresh()
        print("Success delivered! Thank me with a $ 1 donation on GitHub")
        loop3(driver)
    except:
        print("A generic error occurred. Now will retry again")
        driver.refresh()
        sleep(50)
        loop3(driver)

def loop4(driver):
    sleep(20)
    wait_time = 660 #11 minutes
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[1]/div/button").click() #Followers
    except:
        print("You didn't solve the captcha yet. Need to refresh to avoid endless loop.")
        driver.refresh()
        loop4(driver)
    try:
        sleep(20)
        driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div/div/form/div/input").send_keys(vidUrl) #Write
        sleep(2)
        driver.find_element_by_xpath("//*[@id=\"sid\"]/div/div/div/form/div/div/button").click() #Search
        sleep(20)
        driver.find_element_by_xpath("//*[@id=\"c2VuZF9mb2xsb3dlcnNfdGlrdG9r\"]/div[1]/div/form/button").click() #AddFollowers
        sleep(wait_time/3)
        print("Success delivered! Thank me with a $ 1 donation on GitHub")
        sleep(wait_time/3)
        driver.refresh()
        sleep(wait_time/3)
        loop4(driver)
    except:
        print("A generic error occurred. Now will retry again")
        driver.refresh()
        sleep(wait_time)
        loop4(driver)

def loop5(driver):
    sleep(20)
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[5]/div/button").click()
    except:
        print("You didn't solve the captcha yet. Need to refresh to avoid endless loop.")
        driver.refresh()
        loop5(driver)
    try:
        sleep(2000)
        driver.find_element_by_xpath("/html/body/div[4]/div[6]/div/form/div/input").send_keys(vidUrl) # Write
        sleep(2)
        driver.find_element_by_xpath("/html/body/div[4]/div[6]/div/form/div/div/button").click() # Search
        sleep(20)
        driver.find_element_by_xpath("/html/body/div[4]/div[6]/div/div/div/div/div[1]/div/form/button").click() # AddShares
        sleep(60)
        print("Shares sent! Thank me with a $ 1 donation on GitHub")
        sleep(1700)
    except:
        print("A generic error occurred. Now will retry again")
        driver.refresh()
        sleep(300)
        loop5(driver)

def loop6(driver):
    sleep(1000)
    driver.refresh()
    print("Reload")
    loop5(driver)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def creat_chrome():
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(executable_path=r'D:\Program Files (x86)\chromedriver_win32\chromedriver.exe',chrome_options=chrome_options) #Change it
    return driver

def bot_number(bot,chrome):
    if bot == 1:
        loop1(chrome)
    elif bot == 2:
        loop2(chrome)
    elif bot == 3:
        loop3(chrome)
    elif bot == 4:
        loop4(chrome)
    elif bot == 5:
        loop5(chrome)
    elif bot == 6:
        loop5(chrome)
    else:
        print("You can insert just 1, 2, 3, 4, 5 or 6")

def is_captcha(chrome):
    try:
        ele = chrome.find_element_by_xpath('//*[@id="main"]/form/div/div/img')
        dirs = os.getcwd().replace('\\','/') +  '/Captcha.jpg'
        ele.screenshot(dirs)
        return dirs
    except:
        return 0



vidUrl = "https://www.tiktok.com/@luceae_home/video/7002160874664365317" #TikTok视频链接

bot = int(input("What do you want to do?\n1 - Auto views(500)\n2 - Auto hearts\n3 - Auto (FIRST) comments heart\n4 - Auto followers\n5 - Auto Share\n6 - Simple reload\n"))
i = 0

def run_tiktok():
    chrome = creat_chrome()
    chrome.get("https://vipto.de/")
    n = 0
    ocr(n,chrome)
    bot_number(bot,chrome)

if __name__ == "__main__":
    run_tiktok()