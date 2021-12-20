from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
import time


driver=webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
driver.get("https://www.airport.co.kr/www/cms/frFlightStatsCon/airLineStats.do?MENU_ID=1250#none")

try:
    driver.find_element_by_xpath('//*[@id="ST_YY"]/option[text() = "2021"]').click() #시작연도
    driver.find_element_by_xpath('//*[@id="EN_YY"]/option[text() = "2021"]').click() #종료연도
    driver.find_element_by_xpath('//*[@id="ST_MM"]/option[text() = "1"]').click() #시작 월
    driver.find_element_by_xpath('//*[@id="EN_MM"]/option[text() = "12"]').click() #종료 월
    driver.find_element_by_xpath('//*[@id="statisForm"]/div[2]/fieldset[1]/button[1]/span').click() #검색 버튼
    driver.find_element_by_xpath('//*[@id="statisForm"]/div[2]/fieldset[1]/button[2]/span').click() #상세검색
    

    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')
    temp=soup.find_all('table')
    p=parser.make2d(temp[1])
    data=pd.DataFrame(p[2:], columns=p[0])

    #각 데이터 합치기
    df = pd.concat([df, data])

except:
    print('error')
