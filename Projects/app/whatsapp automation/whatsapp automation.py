from selenium import webdriver
from selenium.webdriver.common.keys import Keys

path = 'C:\chromedriver.exe' # whichever directory your chromedriver.exe is saved

driver = webdriver.Chrome(path)
driver.get('https://web.whatsapp.com/') # whatsapp web url

name = input('Enter the exact name of user or group: ') 
msg = input('Enter your message : ')
count = int(input("Enter the count: "))

input("Enter anything after scanning QR code")

user = driver.find_element_by_css_selector('span[title = "{}"]'.format(name))

user.click()

msg_box = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]") #to get element path in developer tools, select element=> right click => copy with path.


for i in range(count):
    msg_box.send_keys(msg)
    msg_box.send_keys(Keys.RETURN)