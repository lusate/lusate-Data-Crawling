from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
import bs4

driver=webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
driver.get("https://www.airport.co.kr/www/index.do")

driver.find_element_by_class_name('loca_search').click()

time.sleep(2)
driver.find_element_by_xpath('//*[@id="header"]/header/div[3]/div/button').click()

time.sleep(2)
driver.find_element_by_xpath('//*[@id="header"]/header/div[3]/div/div/ul/li[1]/a').click()

time.sleep(2)
driver.find_element_by_xpath('//*[@id="header"]/header/div[3]/div/div/ul/li[2]/a').click()

time.sleep(2)
driver.find_element_by_xpath('//*[@id="header"]/header/div[3]/div/div/ul/li[3]/a').click()

time.sleep(2)
driver.find_element_by_xpath('//*[@id="header"]/header/div[3]/div/div/ul/li[4]/a').click()

time.sleep(2)
driver.find_element_by_xpath('//*[@id="header"]/header/div[3]/div/div/ul/li[5]/a').click()

time.sleep(2)
driver.find_element_by_xpath('//*[@id="header"]/header/div[3]/div/div/ul/li[6]/a').click()

time.sleep(2)
driver.find_element_by_xpath('//*[@id="header"]/header/div[3]/div/div/ul/li[7]/a').click()

time.sleep(2)
driver.find_element_by_xpath('//*[@id="header"]/header/div[3]/div/div/ul/li[8]/a').click()

time.sleep(2)
driver.find_element_by_xpath('//*[@id="header"]/header/div[3]/div/div/ul/li[9]/a').click()

time.sleep(2)
driver.find_element_by_xpath('//*[@id="header"]/header/div[3]/div/div/ul/li[10]/a').click()

time.sleep(2)
driver.find_element_by_xpath('//*[@id="header"]/header/div[3]/div/div/ul/li[11]/a').click()

time.sleep(2)
driver.find_element_by_xpath('//*[@id="header"]/header/div[3]/div/div/ul/li[12]/a').click()

time.sleep(2)
driver.find_element_by_xpath('//*[@id="header"]/header/div[3]/div/div/ul/li[13]/a').click()

time.sleep(2)
driver.find_element_by_xpath('//*[@id="header"]/header/div[3]/div/div/ul/li[14]/a').click()

time.sleep(2)
airports = bs4.BeautifulSoup(driver.page_source, 'lxml')

airports_list = airports.find_all('p', class_='result_details')
airports_address_list = []

for airports in airports_list:
    airports_address_list.append(airports.text)

driver.close()
print(airports_address_list)


