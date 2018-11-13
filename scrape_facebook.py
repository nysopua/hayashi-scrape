import time
import bs4

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

def getMembers():
  options = Options()
  options.add_argument('--headless')
  driver = webdriver.Chrome(options=options)

  driver.get('https://www.facebook.com/login/?next=https%3A%2F%2Fwww.facebook.com%2Fgroups%2F151277795688730%2Fmembers%2F')

  id = driver.find_element_by_id("email")
  id.send_keys('[Email]')
  password = driver.find_element_by_id("pass")
  password.send_keys('[Pass]')

  time.sleep(1)

  login_button = driver.find_element_by_name("login")
  login_button.click()

  soup = bs4.BeautifulSoup(driver.page_source, "html.parser")
  
  members = soup.select('span._grt')[0].text

  driver.quit()
  return f'【BM stadiumのメンバー数】{members}'
