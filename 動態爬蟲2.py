#!/usr/bin/env python
# coding: utf-8
# 資料整理函式 用在67行
def show_data(list_x,date1, date2,logo):
    plane = list_x[0] + "-" + list_x[1]
    go1, gototal, go2 = list_x[2].split(" ")
    go_time = go1 + "-" + go2
    go_airport= list_x[3].split(' ')
    go_airport = "-".join(go_airport)
    back1, backtotal, back2 = list_x[4].split(" ")
    back_time = back1 + "-" + back2
    back_airport = list_x[5]
    nothing, price = list_x[6].split("$")
    result = [plane, go_airport, date1, date2, price, logo, go_time ,back_time,gototal, backtotal]
    return result




# 主要爬取函式
def main_scrapy(http_list):
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import time
    logo_dict = {"https://www.funtime.com.tw/airline/images/airline/D7.png":"亞洲航空",
                 "https://www.funtime.com.tw/airline/images/airline/3K.png":"捷星航空",
                 "https://www.funtime.com.tw/airline/images/airline/IT.png":"台灣虎航",
                 "https://www.funtime.com.tw/airline/images/airline/MM.png":"樂桃航空",
                 "https://www.funtime.com.tw/airline/images/airline/TR.png":"酷航航空",
                 "https://www.funtime.com.tw/airline/images/airline/LJ.png":"真航空",
                 "https://www.funtime.com.tw/airline/images/airline/VJ.png":"越捷航空",
                 "https://www.funtime.com.tw/airline/images/airline/Z2.png":"亞洲航空",
                 "https://www.funtime.com.tw/airline/images/airline/SL.png":"泰國獅子航空",
                 "https://www.funtime.com.tw/airline/images/airline/XW.png":"酷鳥航空",
                 "https://www.funtime.com.tw/airline/images/airline/UO.png":"香港快捷航空",
                 "https://www.funtime.com.tw/airline/images/airline/9C.png":"春秋航空",
                 "https://www.funtime.com.tw/airline/images/airline/7C.png":"濟州航空"}
    scrapy_data = [["飛機代號", "飛機機場", "出發日期", "回來日期", "機票價格", "航空公司", "去程時間", "回程時間",\
               "花費時間"]]
    driver_location = "C:\\Users\\user\\chromedriver\\chromedriver.exe"
    driver = webdriver.Chrome(driver_location)
    count_1 = 0
    e_count = 0
# 網址資料處理(產出網址、日期1、日期2、直飛與否
    while len(http_list) != 0:
        http = http_list[0][0]
        date1 = http_list[0][1]
        date2 = http_list[0][2]
        non_stop = http_list[0][3]
    # 啟動虛擬瀏覽器  
        driver.get(http)
        wait = WebDriverWait(driver, 50)
        wait.until(EC.presence_of_element_located((By.ID,"result_area")),message="")
        alldata_list = driver.find_element_by_id("result_area").text.split("\n")
    # 等待搜尋結束
        while alldata_list[0][0:4] == '正在搜尋':
            time.sleep(3)
            alldata_list = driver.find_element_by_id("result_area").text.split("\n")
        if alldata_list[0][0:4] == 'Oops':
            ans_list ='Error'
                break
        else:
            logo_1 = "div.fly_airline.clearfix > div > div.flight_row.GO.top > div > img"
            logo_2 = "div.fly_airline.clearfix > div > div.flight_row.BACK.top > div > img"
            logo_1 = driver.find_element_by_css_selector(logo_1).get_attribute("src")
            logo_2 = driver.find_element_by_css_selector(logo_2).get_attribute("src")
            logo = logo_dict[logo_1] + "-" + logo_dict[logo_2]
            ans_list = show_data(alldata_list,date1, date2,logo)
            del http_list[0]
            scrapy_data.append(ans_list)
    driver.quit()       
    return scrapy_data
scrapy_data = main_scrapy(final_data)
driver.quit()
