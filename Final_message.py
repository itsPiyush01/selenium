from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from time import sleep
import re
from os import remove
from os import environ
from dotenv import load_dotenv
import math, random
import time
# Run Chrome Headless
#chrome_options = Options()
#chrome_options.add_argument("--headless")
#chrome_options.add_argument('--window-size=1920x1080')
globals()
isEmailSend=False
def generateOTP():
    # Declare a digits variable
    # which stores all digits
    digits = "0123456789"
    OTP = ""
    # length of password can be chaged
    # by changing value in range
    for i in range(4):
        OTP += digits[math.floor(random.random() * 10)]

    return OTP


# Driver code
if __name__ == "__main__":
    OPTCode=generateOTP()
#chrome_options = Options()b
#chrome_options.add_argument("--headless")
#chrome_options.add_argument("--window-size=1920x1080")
try:
    # driver = webdriver.Chrome(executable_path=r'C:\Users\Ashutosh Charchi\PycharmProjects\Python\chromedriver.exe',options=chrome_options)
    driver = webdriver.Chrome(executable_path=r'C:\Users\Ashutosh Charchi\PycharmProjects\Python\chromedriver.exe')
    driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
    email=driver.find_element_by_xpath('//*[@id="login1"]')
    email.send_keys("alumni.space")
    passtext=open("password.text",'r')
    password=driver.find_element_by_xpath('//*[@id="password"]')
    password.send_keys(passtext.read())
    keep_me_signIn_bt=driver.find_element_by_xpath('//*[@id="remember"]')
    keep_me_signIn_bt.click()
    login_bt=driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div[1]/div/form/div[2]/div[6]/div[1]/input')
    login_bt.click()
    writeMail_box=driver.find_element_by_xpath('//*[@id="boxscroll"]/li[1]/a')
    writeMail_box.click()
    time.sleep(15)
    To_send_email=driver.find_element_by_xpath('//*[@id="TO_IDcmp2"]')
    To_send_email.send_keys("piyushranjan1402@gmail.com")
    subject_box=driver.find_element_by_xpath('//*[@id="rd_compose_cmp2"]/ul/li[4]/input')
    subject_box.send_keys(("OTP for email verification is  "),(OPTCode),(" Please don't reply "))
    #time.sleep(1)
    #print("check 0")
    #past_bt=driver.find_element_by_css_selector(".cke_button__paste_icon")
    #past_bt.click()
    #print("check 1")
    #Main_email_context=driver.find_element_by_class_name('.cke_editable')
    #print("check 2 ")
    #Main_email_context.clear()
    #print("check 3")
    #Main_email_context.send_keys("Dear Piyush it's test it ")
    time.sleep(1)
    send_mail_bt=driver.find_element_by_xpath('//*[@id="rd_compose_cmp2"]/div[1]/a[1]')
    send_mail_bt.click()
    globals()
    isEmailSend=True
    time.sleep(5)
    logout_bt=driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div[2]/a[2]')
    logout_bt.click()
    time.sleep(5)


finally:
    if isEmailSend==True:
        print("Email is Successfully send :)  ")
    else:
        print("Email is not send :(")
    driver.close()