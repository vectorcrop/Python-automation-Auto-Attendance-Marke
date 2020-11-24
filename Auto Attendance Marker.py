from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://sfqelectronics.gnomio.com/')

time.sleep(2)

loginbtn1 = driver.find_element_by_xpath("/html/body/header/nav/div/ul/li[1]/div/a")
loginbtn1.click()

time.sleep(2)

username = driver.find_element_by_name("username")

username.send_keys("Enter your email or username here!!!")  # <<------------------------------- Enter your email or username here.

password = driver.find_element_by_name("password")

password.send_keys("Enter your password here")  # <<------------------------------------------- Enter your password here.

loginbtn2 = driver.find_element_by_xpath("//*[@id='loginbtn']")
loginbtn2.click()


time.sleep(2)

driver.get('https://sfqelectronics.gnomio.com/mod/attendance/view.php?id=80')


time.sleep(5)

loginbtn6 = driver.find_element_by_xpath("//*[@id='region-main-campus']/div[1]/table[1]/tbody/tr[9]/td[3]/a")
loginbtn6.click()

time.sleep(2)

driver.get('https://sfqelectronics.gnomio.com/mod/attendance/view.php?id=80')


time.sleep(4)

loginbtn7 = driver.find_element_by_xpath("//*[@id='region-main-campus']/div[1]/table[1]/tbody/tr[9]/td[3]/a")
loginbtn7.click()

time.sleep(4)

loginbtn8 = driver.find_element_by_xpath("//*[@id='id_status_45']")
loginbtn8.click()

time.sleep(4)

loginbtn8 = driver.find_element_by_xpath("//*[@id='id_submitbutton']")
loginbtn8.click()

time.sleep(2)

driver.quit()











