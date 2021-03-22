from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
path = "C:\chrome driver\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("http://test.fcubecinemas.com/")
driver.maximize_window()

time.sleep(5)
Time_select = driver.find_element_by_xpath("//span[contains(text(),'23')]")
Time_select.click()
time.sleep(4)

links = driver.find_elements(By.TAG_NAME, "a")
print(len(links))
for link in links:
    print(link.text)

Now_showing = driver.find_element_by_link_text("Vijay The Master (PG)")
Now_showing.click()
time.sleep(7)
driver.find_element_by_link_text("04:00 PM").click()

#Login

time.sleep(3)
Email = driver.find_element_by_xpath("//input[@id='UserName']").send_keys("motung")
time.sleep(2)
Password = driver.find_element_by_xpath("//input[@id='Password']").send_keys("Nirvana3")
time.sleep(2)
Go = driver.find_element_by_xpath("//button[contains(text(),'GO')]").click()
time.sleep(4)

#Selecting tickets
Ticket1 = driver.find_element_by_xpath("//button[@id='393']")
Ticket1.click()
time.sleep(3)
Ticket2 = driver.find_element_by_xpath("//button[@id='390']")
Ticket2.click()
time.sleep(3)
Ticket3 = driver.find_element_by_xpath("//button[@id='389']")
Ticket3.click()
time.sleep(3)
Ticket4 = driver.find_element_by_xpath("//button[@id='388']")
Ticket4.click()
time.sleep(3)
Ticket5 = driver.find_element_by_xpath("//button[@id='358']")
Ticket5.click()
time.sleep(3)
#diselecting a seat
driver.find_element_by_xpath("//button[@id='358']").click()

#Reserving tickets
time.sleep(3)
Reserve = driver.find_element_by_xpath("//button[@id='btn-reserve']")
Reserve.click()
time.sleep(4)
driver.find_element_by_xpath("//button[@id='btn-continue-reserve']").click()
time.sleep(7)
driver.find_element_by_xpath("//body/div[@id='confirmationMessage']/div[3]/button[1]").click()

#My account page
time.sleep(5)
Collaps_btn = driver.find_element_by_tag_name("button")
Collaps_btn.click()
time.sleep(3)
Cancel_btn = driver.find_element_by_xpath("//button[contains(text(),'Cancel Selected')]")
Cancel_btn.click()
time.sleep(5)
Yes = driver.find_element_by_xpath("//div[contains(text(),'Yes')]")
Yes.click()
time.sleep(5)
Popup_cose = driver.find_element_by_xpath("//div[@id='popupMessage']//button[@id='btn-close']")
Popup_cose.click()
time.sleep(5)
driver.close()