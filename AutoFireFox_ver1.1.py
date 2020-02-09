from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.firefox.options import Options
options = Options()
options.headless = True
driver = webdriver.Firefox(options=options, executable_path=r'C:\Users\Ashutosh Charchi\PycharmProjects\Python\geckodriver.exe')
#driver = webdriver.Firefox(executable_path=r'C:\Users\Ashutosh Charchi\PycharmProjects\Python\geckodriver.exe')
driver.get("https://www.google.com/")
print ("Headless Firefox Initialized")
print(driver.title)
driver.quit()