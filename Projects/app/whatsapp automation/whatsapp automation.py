from selenium import webdriver

path = 'C:\Program Files (x86)\chromedriver.exe'

driver = webdriver.Chrome(path)
driver.get('https://web.whatsapp.com/')

name = input('Enter the name of user or group: ')
msg = input('Enter your message : ')
count = int(input("Enter the count: "))

input("Enter anything after scanning QR code")

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))

user.click()

msg_box = driver.find_element_by_class_name('_3F6QL._2WovP') #_3F6QL._2WovP

for i in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_35EW6')
    button.click()