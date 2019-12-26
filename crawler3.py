from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import win32clipboard
import win32con

# coding=utf-8

import datetime

info = [['飛機代號', '飛機機場', '出發日期', '回來日期', '機票價格', '航空公司', '去程時間', '回程時間', '出發飛行時間', '回程飛行時間'], ['IT210-IT211', '桃園機場-大阪關西機場', '2020-06-01', '2020-06-05', '5,969', '台灣虎航-台灣虎航', '03:40-10:25', '11:15-13:10', '6小時45分鐘', '2小時55分鐘'], ['IT210-IT211', '桃園機場-大阪關西機場', '2020-06-01', '2020-06-05', '5,969', '台灣虎航-台灣虎航', '04:40-10:25', '14:00-15:55', '5小時45分鐘', '2小時55分鐘'], ['IT210-IT211', '桃園機場-大阪關西機場', '2020-06-01', '2020-06-05', '5,569', '台灣虎航-台灣虎航', '05:40-10:25', '11:15-13:10', '4小時45分鐘', '2小時55分鐘'], ['IT210-IT211', '桃園機場-大阪關西機場', '2020-06-01', '2020-06-05', '5,569', '台灣虎航-台灣虎航', '06:40-10:25', '14:00-15:55', '3小時45分鐘', '2小時55分鐘'], ['IT210-IT211', '桃園機場-大阪關西機場', '2020-06-01', '2020-06-05', '5,769', '台灣虎航-台灣虎航', '07:40-10:25', '11:15-13:10', '2小時45分鐘', '2小時55分鐘']]

info_ticket = list()
for i in range(1, len(info)):
	if "," in info[i][4]:
		info[i][4] = int(info[i][4].replace(",", ""))  # 去除價格千分位分隔符號並轉成整數
	else:
		info[i][4] = int(info[i][4])  # 若價格無千分位分隔符號則直接轉成整數

	index_hour1 = info[i][8].find("時")
	index_hour2 = info[i][9].find("時")
	flight_time1 = datetime.timedelta(hours = int(info[i][8][:index_hour1 - 1]), minutes = int(info[i][8][index_hour1 + 1:len(info[i][8])-2]))  # 出發飛行時間
	flight_time2 = datetime.timedelta(hours = int(info[i][9][:index_hour2 - 1]), minutes = int(info[i][9][index_hour2 + 1:len(info[i][9])-2]))  # 回程飛行時間
	travel_time = datetime.datetime(2000, 1, 1, 0, 0, 0) + flight_time1 + flight_time2  # 以固定日期為基準加上總飛行時間以利後續排序
	info[i].append(travel_time)  # 將每張機票資訊加入總飛行時間
	info_ticket.append(info[i])  # 將去除標題列之資訊加入清單
	
info_ticket.sort(key=lambda info_ticket: [info_ticket[4], info_ticket[10]])  # 將機票依價格、總飛行時間之層級排序

for info in info_ticket:
    money = info[4]
    bfrom_city = 'TY'
    departure = info[2]
    backdate = info[3]
    region = 'RE_ASIA_N'
    country = 'CN_JAPAN'
    city = 'OSA'
    url = 'https://www.funtime.com.tw/airline/result.php?bfrom_city=' + bfrom_city + '&departure=' + departure + '&backdate=' + backdate + '&region=' + region + '&country=' + country + '&city=' + city + '&type=ROU&adt=1&chd=0&inf=0&fair_type=TYPE1'

    #打開瀏覽器,確保你已經有chromedriver在你的目錄下
    browser=webdriver.Chrome('./chromedriver')
    #在瀏覽器打上網址連入
    browser.get(url) 
    sleep(3)

    #這時候就可以分析網頁裡面的元素
    men_menu = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='result_area']/div[3]/div[1]/div[5]")))
    ActionChains(browser).move_to_element(men_menu).perform()
    sleep(3)

    men_menu = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='result_area']/div[3]/div[1]/div[5]/div/div/div/div[1]/div")))
    ActionChains(browser).click(men_menu).perform()
    sleep(3)
    
    win32clipboard.OpenClipboard() 
    text = win32clipboard.GetClipboardData(win32con.CF_TEXT) 
    win32clipboard.CloseClipboard() 
    print(text)

    browser.close()
    sleep(3)
