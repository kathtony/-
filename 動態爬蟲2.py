#!/usr/bin/env python
# coding: utf-8

# In[53]:


import requests as rq
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import csv


# In[2]:


# 網站資料
# 出發地點-到達地點
bc = "桃園"
region = "RE_ASIA"
country = "CN_JAPAN"
city = "OSA"
# 出發時間-回程時間
date1 = "2020-01-01" 
date2 = "2020-01-10"
# 機票類型
ticket_type = "ROU" # 以來回票為範例
# 票種:基本或攜帶行李
luggage = "TYPE1" # 
# 人數
adult = '1' # 成人
child = '0' # 小孩
baby = '0' # 嬰兒
time_range = "563-1100-563-1100"

tw_site = {"桃園":"TY",
           "松山":"TP",
           "高雄":"HS",
           "台中":"TC"}
start_site = tw_site[bc]

start_site = "bfrom_city="+ tw_site[bc]
start_time = "departure=" + date1
back_time = "backdate=" + date2
region = "region=" + region
country = "country=" + country
city = "city=" + city
ticket_type = "type=" + ticket_type
adult = "adt=" + adult
child = "chd=" + child
baby = "inf=" + baby
luggage = "fair_type=" + luggage
time_range =  "depart_time_go[]=" + time_range
http = "https://www.funtime.com.tw/airline/result.php?" + start_site +       "&" + start_time + "&" + back_time +        "&" + region + "&" + country + "&" + city +        "&" + ticket_type +        "&sort=price&order=up&" +        adult + "&" + child + "&" + baby + "&" +        luggage + "&air_go[]=none&air_back[]=none&source[]=none&forward[]=none&" +        time_range + "&price=none&"
logo_dict = {"https://www.funtime.com.tw/airline/images/airline/D7.png":"亞洲航空", "https://www.funtime.com.tw/airline/images/airline/3K.png":"捷星航空","https://www.funtime.com.tw/airline/images/airline/IT.png":"台灣虎航", "https://www.funtime.com.tw/airline/images/airline/MM.png":"樂桃航空"}


# In[52]:


list_1 = url_list
logo_dict = {"https://www.funtime.com.tw/airline/images/airline/D7.png":"亞洲航空", "https://www.funtime.com.tw/airline/images/airline/3K.png":"捷星航空","https://www.funtime.com.tw/airline/images/airline/IT.png":"台灣虎航", "https://www.funtime.com.tw/airline/images/airline/MM.png":"樂桃航空"}
date1 ="2020-06-01"
date2 ="2020-06-05"

def data_show(list_x):
    list_y = []
    for i in range(len(list_x)//2 + 1):
        i_x =  i*2 - 1
        x = list_x[i]
        if i_x == -1:
            nothing, price = x.split("$")
            list_y.append(price)
        else:
            x = list_x[i_x]
            y = list_x[i_x + 1]
            result = x + "-" + y
            list_y.append(result)
    return list_y

# 啟動虛擬瀏覽器  
driver_location = "C:\\Users\\user\\chromedriver\\chromedriver.exe"
driver = webdriver.Chrome(driver_location)
result_list = [["飛機代號", "飛機機場", "出發日期", "回來日期", "機票價格", "航空公司", "去程時間", "回程時間",               "花費時間"]]
for i in range(len(list_1)):
    https = list_1[i]
    driver.get(https)
    time.sleep(10)
# 將網站解繹
    doc = pq(driver.page_source)
    doc1  = doc('#result_area > div > div > div > div > div > div:nth-child(1)')
    string2 = doc1.text().strip().split(" ")
# 處理string2
    while '' in string2:
        string2.remove("")
    plane1 = string2[0]
    plane2 = string2[1]
    airport1 = string2[3]
    airport2 = string2[5]
# 爬蟲資料爬取結構
    string3 = plane1 + chr(92) +"@" + plane2
    selector = "#result_area > div.result_box."+string3+".price_flag > div.fly_box > "
    price = selector + "div.fly_right > div.fly_price"
    go_t1 = selector + "div.fly_content > div > div.flight_row.GO.top > div.flight_cell.from"
    go_t2 = selector + "div.fly_content > div > div.flight_row.GO.top > div.flight_cell.to"
    go_total = selector + "div.fly_content > div > div.flight_row.GO.top > div.flight_cell.arrow"
    back_t1 = selector + "div.fly_content > div > div.flight_row.BACK.top > div.flight_cell.from"
    back_t2 = selector +"div.fly_content > div > div.flight_row.BACK.top > div.flight_cell.to"
    back_total = selector + "div.fly_content > div > div.flight_row.BACK.top > div.flight_cell.arrow"
    logo_1 = "div.fly_airline.clearfix > div > div.flight_row.GO.top > div > img"
    logo_2 = "div.fly_airline.clearfix > div > div.flight_row.BACK.top > div > img"
    selector_list = [price, logo_1, logo_2, go_t1, go_t2, back_t1, back_t2, go_total, back_total]
    
    ans_list = [plane1 + "-" + plane2, airport1 + "-" + airport2, date1, date2]
    count = 0
    test_list = []
    for select in selector_list:
        test = driver.find_element_by_css_selector(select)
        if count == 1 or count == 2:
            test = logo_dict[test.get_attribute("src")]
        else:
            test = test.text
        test_list.append(test)
        count += 1
    test_list = data_show(test_list)
    ans_list += test_list
    result_list.append(ans_list)

print(result_list)


# In[57]:


with open("機票資料.csv","w",newline="") as fOut:
        csvOut = csv.writer(fOut)
        for i in range(len(result_list)):
            csvOut.writerows(result_list[i])


# In[51]:


driver.close()


# In[50]:


result_list





# In[22]:





# In[23]:


url_list


# In[ ]:





# In[20]:



driver.close()


# In[13]:


from fake_useragent import UserAgent
from selenium.webdriver import ChromeOptions 
from selenium.webdriver.chrome.options import Options


# In[18]:



preferred_time[prefer_back_time]


# In[19]:


'depart_time_go[]=' + preferred_time[prefer_departime_time] + '-' + preferred_time[prefer_back_time]


# In[69]:


http = "https://www.google.com/"
driver_location = "C:\\Users\\user\\chromedriver\\chromedriver.exe"
ua = UserAgent()
ua = ua.chrome

option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.add_argument("user-agent={}".format(ua))
driver=webdriver.Chrome(driver_location, options=option)
driver.implicitly_wait(5)
driver.get(http)
time.sleep(5)


# In[70]:


search = "#tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input"
driver.find_element_by_css_selector(search).send_keys("skyscanner")
click = "#tsf > div:nth-child(2) > div.A8SBwf.emcav > div.UUbT9 > div.aajZCb > div.tfB0Bf > center > input.gNO89b"
driver.find_element_by_css_selector(click).click()


# In[71]:


http = "#rso > div:nth-child(1) > div > div > div > div > div.r > a > h3"
click = driver.find_element_by_css_selector(http)
click.click()


# In[ ]:





# In[23]:


botton_1 = "#fsc-destination-search"
test_1 = driver.find_element_by_css_selector(botton_1)
test_1.send_keys(" 大阪")


# In[24]:


touch = "#modal-autosuggest > header > nav > button"
test = driver.find_element_by_css_selector(touch)
test.click()


# In[25]:


touch = "#flights-search-controls-root > div > div > form > div:nth-child(3) > button"
test = driver.find_element_by_css_selector(touch)
test.click()


# In[ ]:




