# 載入套件
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datetime
import time

# 測試資料：
# 來回,桃園,東北亞,日本,東京（成田/羽田）機場,2020,6,5,1,0,0,基本票,不限,不限,不限,早,午,0,20000 
# 來回,桃園,東北亞,日本,大阪,2020,6,5,1,0,0,基本票,不限,不限,不限,早,午,0,20000

# 來回、單程、不同點進出
way_type = {'來回':'ROU','單程':'ONE','不同點進出':'ROUND'}

# 建立出發地dictionary
from_city = {'桃園':'TY','松山':'TP','台中':'TC','高雄':'HS'}

# 建立目的地區dictionary
region = {'東北亞':'RE_ASIA','港澳大陸':'RE_CHINA','東南亞':'RE_ASIA','歐洲':'RE_EUROPE','紐奧':'RE_OCEANIA','太平洋島嶼':'RE_PACIFIC','南亞中東':'RE_ASIA'}

#建立目的國家dictionary
country = dict()
country['中國'] = 'CN_CHINA'
country['香港'] = 'CN_Hong+Kong'
country['澳門'] = 'CN_Macau'
country['日本'] = 'CN_JAPAN'
country['韓國'] = 'CN_KOREA'
country['泰國'] = 'CN_THAILAND'
country['新加坡'] = 'CN_SINGAPORE'
country['馬來西亞'] = 'CN_MALAYSIA'
country['印尼'] = 'CN_INDONESIA'
country['菲律賓'] = 'CN_PHILIPPINES'
country['柬埔寨'] = 'CN_CAMBODIA'
country['越南'] = 'CN_VIETNAM'
country['汶萊'] = 'CN_BRUNEI'
country['緬甸'] = 'CN_MYANMAR'
country['寮國'] = 'CN_LAOS'
country['德國'] = 'CN_GERMANY'
country['希臘'] = 'CN_GREECE'
country['澳洲'] = 'CN_AUSTRALIA'
country['紐西蘭'] = 'CN_NEW+ZEALAND'
country['關島'] = 'CN_GUAM'
country['塞班'] = 'CN_SAIPAN'
country['印度'] = 'CN_INDIA'
country['馬爾地夫'] = 'CN_MALDIVES'
country['阿拉伯聯合大公國'] = 'CN_UNITED+ARAB+EMIRATES'
country['尼泊爾'] = 'CN_NEPAL'
country['伊朗'] = 'CN_IRAN'
country['孟加拉'] = 'CN_BENGAL'

# 建立目的城市dictionary
city = dict()
city['上海'] = 'SHA'
city['上海浦東機場'] = 'SHA_PVG'
city['上海虹橋機場'] = 'SHA_SHA'
city['北京'] = 'BJS'
city['廣州'] = 'CAN'
city['石家莊'] = 'SJW'
city['汕頭'] = 'SWA'
city['深圳'] = 'SZX'
city['香港'] = 'HKG'
city['澳門'] = 'MFM'
city['東京（成田/羽田）機場'] = 'TYO'
city['東京成田機場'] = 'TYO_NRT'
city['東京羽田機場'] = 'TYO_HND'
city['大阪'] = 'OSA'
city['琉球（沖繩）'] = 'OKA'
city['福岡'] = 'FUK'
city['名古屋'] = 'NGO'
city['札榥'] = 'SPK'
city['函館'] = 'HKD'
city['仙台'] = 'SDJ'
city['岡山'] = 'OKJ'
city['小松'] = 'KMQ'
city['首爾'] = 'SEL'
city['首爾仁川機場'] = 'SEL_ICN'
city['首爾金浦機場'] = 'SEL_GMP'
city['釜山'] = 'PUS'
city['濟州'] = 'CJU'
city['大邱'] = 'TAE'
city['務安'] = 'MWX'
city['清州'] = 'CJJ'
city['曼谷'] = 'BKK'
city['普吉島'] = 'HKT'
city['清邁'] = 'CNX'
city['合艾'] = 'HDY'
city['喀比'] = 'KBV'
city['素叻府'] = 'URT'
city['新加坡'] = 'SIN'
city['吉隆坡'] = 'KUL'
city['亞庇'] = 'BKI'
city['檳城'] = 'PEN'
city['蘭卡威'] = 'LGK'
city['古晉'] = 'KCH'
city['關丹'] = 'KUA'
city['哥打巴魯'] = 'KBR'
city['納閩'] = 'LBU'
city['詩巫'] = 'SBW'
city['山打根'] = 'SDK'
city['登嘉樓'] = 'TGG'
city['斗湖'] = 'TWU'
city['雅加達'] = 'JKT'
city['巴里島'] = 'DPS'
city['泗水'] = 'DPS'
city['萬隆'] = 'BDO'
city['日惹'] = 'JOG'
city['龍目島'] = 'LOP'
city['巨港'] = 'PLM'
city['棉蘭'] = 'MES'
city['坤緬'] = 'PNK'
city['梭羅'] = 'SOC'
city['三寶壟'] = 'SRG'
city['佩坎巴魯'] = 'PKU'
city['馬尼拉'] = 'MNL' # 菲律賓
city['宿霧'] = 'CEB'
city['長灘島'] = 'KLO'
city['巴拉望'] = 'PPS'
city['薄荷島'] = 'TAG'
city['克拉克'] = 'CRK'
city['科隆'] = 'USU'
city['卡提克蘭'] = 'MPH'
city['達沃城'] = 'DVO'
city['暹粒'] = 'REP' # 柬埔寨
city['金邊'] = 'PNH'
city['西哈努克'] = 'KOS'
city['胡志明市'] = 'SGN' # 越南
city['河內'] = 'HAN'
city['峴港'] = 'DAD'
city['芽莊'] = 'NHK'
city['芹苴（肯特）'] = 'VCA'
city['金蘭市'] = 'CXR'
city['斯里巴加灣'] = 'BWN' # 汶萊
city['仰光'] = 'RGN' # 緬甸
city['永珍'] = 'VTE' # 寮
city['龍坡邦'] = 'LPQ'
city['柏林'] = 'BER'
city['雅典'] = 'ATH'
city['雪梨'] = 'SYD'
city['墨爾本'] = 'MEL'
city['黃金海岸'] = 'OOL'
city['伯斯'] = 'PER'
city['凱恩斯'] = 'CNS'
city['達爾文'] = 'DRW'
city['奧克蘭'] = 'AKL'
city['關島'] = 'GUM'
city['塞班'] = 'SPN'
city['加爾各答'] = 'CCU'
city['孟買'] = 'BOM'
city['科欽'] = 'COK'
city['齋普爾'] = 'JAI'
city['清奈'] = 'MAA'
city['蒂魯吉拉伯利'] = 'TRZ'
city['勒克瑙'] = 'LKO'
city['阿姆利則'] = 'ATQ'
city['海得拉巴'] = 'HYD'
city['班加羅爾'] = 'BLR'
city['馬列'] = 'MLE' # 馬爾地夫
city['杜拜'] = 'DXB'
city['吉達'] = 'JED'
city['加德滿都'] = 'KTM'
city['德黑蘭'] = 'THR'
city['達卡'] = 'DAC'

# 建立fair_type dictionary
ticket_type = {'基本票':'TYPE1','含托運行李':'TYPE2'}

# 建立是否轉機dictionary
stop_or_not = {'不限': 'none', '直飛': 'NSTOP', '轉機': 'STOP'}

# 偏好時間dictionary
preferred_time = {'不限': 'none', '早': '241-660', '午': '661-1020', '晚': '1021-240'}

# 航空公司
airline = dict()
airline['不限'] = 'none'
airline['台灣虎航'] = 'tigerair'
airline['亞洲航空'] = 'airasia'
airline['酷航航空'] = 'scoot'
airline['捷星航空'] = 'jetstar'
airline['越捷航空'] = 'vietjetair'
airline['宿霧太平洋航空'] = 'cebupacificair'
airline['易斯達航空'] = 'eastarjet'
airline['濟州航空'] = 'jejuair'
airline['真航空'] = 'jinair'
airline['泰國獅子航空'] = 'lionair'
airline['酷鳥航空'] = 'nokscoot'
airline['樂桃航空'] = 'flypeach'
airline['香草航空'] = 'flypeach' #兩家公司已合併
'''
使用者輸入
way(_type)來回、單程，出發地，目的地地區，目的地國家，目的地城市，年，月，去幾天，成人數，兒童數，嬰兒數，ticket(_type)是否基本票，去程航空，回程航空，forward(stop or not)是否轉機，去程偏好時段，回程偏好時段,開始價,結束價
共19項
# 來回,桃園,東北亞,日本,大阪,2020,6,10,1,0,0,基本票,不限,不限,不限,早,早,1,20000
way(_type)不同點進出，出發地，目的地地區，目的地國家，目的地城市，年，月，去幾天，成人數，兒童數，嬰兒數，ticket(_type)是否基本票，回程目的地，回程出發地區，回程出發國家，回程出發城市，去程航空，回程航空，去程偏好時段，回程偏好時段,開始價,結束價
共23項
'''
line1 = input() # 以逗號間隔
list1 = line1.split(',')
print(list1)
way = list1[0]
year = int(list1[5])
month = int(list1[6])
days = int(list1[7])
month_dict = dict()
final_data = []
if (year % 4) == 0 and (year % 100) !=0 or (year % 400) == 0:
    month_dict= {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
else:
    month_dict= {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
for i in range(month_dict[month]):
    departure_date = datetime.datetime(year,month,i+1)
    diff = datetime.timedelta(days = days)
    back_date = departure_date + diff
    if back_date >= datetime.datetime(year,month+1,1):
        break
    if way == '不同點進出':
        departure_spot = list1[1]
        arrive_region = list1[2]
        arrive_country = list1[3]
        arrive_city = list1[4]
        adt = int(list1[8])
        chd = int(list1[9])
        inf = int(list1[10])
        ticket = list1[11]
        back_spot = list1[12]            # 回程目的地
        back_depart_region = list1[13]   # 回程出發地區
        back_depart_country = list1[14]  # 回程出發國家
        back_depart_city = list1[15]     # 回程出發城市
        forward = list1[16]
        air_go = list1[17]
        air_back = list1[18]
        prefer_departime_time = list1[19]
        prefer_back_time = list1[20]
        startprice = list1[21]
        endprice = list1[22]
    
		# 輸出網址
        url = 'https://www.funtime.com.tw/airline/result.php?'
        url += 'bfrom_city=' + from_city[departure_spot] + '&'
        url += 'departure=' + departure_date.strftime('%Y-%m-%d') + '&'
        url += 'backdate='+ back_date.strftime('%Y-%m-%d') + '&'
        url += 'region=' + region[arrive_region] + '&'
        url += 'country=' + country[arrive_country] + '&'
        url += 'city=' + city[arrive_city] + '&'
        url += 'type=' + way_type[way] + '&'
        url += 'sort=price&'
        url += 'order=up&'
        url += 'adt=' + str(adt) + '&'
        url += 'chd=' + str(chd) + '&'
        url += 'inf=' + str(inf) + '&'
        url += 'fair_type' + ticket_type[ticket] + '&'
        url += 'bfrom_city_back=' + from_city[back_spot] + '&' # 回程目的地
        url += 'region_back=' + region[back_depart_region]+ '&'# 回程出發地區
        url += 'country_back=' + country[back_depart_country] + '&'# 回程出發國家
        url += 'city_back=' + city[back_depart_city] + '&'# 回程出發城市
        url += 'air_go[]=' + airline[air_go] + '&'
        url += 'air_back[]=' + airline[air_back] + '&'
        url += 'source[]=none&'
        url += 'forward[]=' + stop_or_not[forward] + '&'
        if prefer_departime_time == 'none' and prefer_back_time == 'none':
            url += 'depart_time_go[]=none&'
        else:
            url += 'depart_time_go[]=' + preferred_time[prefer_departime_time] + '-' + preferred_time[prefer_back_time] + '&'
        if startprice == '0' and endprice == '0':
            url +='price=none&'
        else:
            url += 'price=' + startprice + '-' + endprice + '&'
    else:
        departure_spot = list1[1]
        arrive_region = list1[2]
        arrive_country = list1[3]
        arrive_city = list1[4]
        adt = int(list1[8])
        chd = int(list1[9])
        inf = int(list1[10])
        ticket = list1[11]
        forward = list1[12]
        air_go = list1[13]
        air_back = list1[14]
        prefer_departime_time = list1[15]
        prefer_back_time = list1[16]
        startprice = list1[17]
        endprice = list1[18]

		# 輸出網址
        url = 'https://www.funtime.com.tw/airline/result.php?'
        url += 'bfrom_city=' + from_city[departure_spot] + '&'
        url += 'departure=' + departure_date.strftime('%Y-%m-%d') + '&'
        url += 'backdate='+ back_date.strftime('%Y-%m-%d') + '&'
        url += 'region=' + region[arrive_region] + '&'
        url += 'country=' + country[arrive_country] + '&'
        url += 'city=' + city[arrive_city] + '&'
        url += 'type=' + way_type[way] + '&'
        url += 'sort=price&'
        url += 'order=up&'
        url += 'adt=' + str(adt) + '&'
        url += 'chd=' + str(chd) + '&'
        url += 'inf=' + str(inf) + '&'
        url += 'fair_type' + ticket_type[ticket] + '&'
        url += 'air_go[]=' + airline[air_go] + '&'
        url += 'air_back[]=' + airline[air_back] + '&'
        url += 'source[]=none&'
        url += 'forward[]=' + stop_or_not[forward] + '&'
        if prefer_departime_time == 'none' and prefer_back_time == 'none':
            url += 'depart_time_go[]=none&'
        else:
            url += 'depart_time_go[]=' + preferred_time[prefer_departime_time] + '-' + preferred_time[prefer_back_time] + '&'
        if startprice == '0' and endprice == '0':
            url +='price=none&'
        else:
            url += 'price=' + startprice + '-' + endprice + '&'
    forward_type = 0
    if forward == '不限':
        forward_type = 0
    elif forward == '直飛':
        forward_type = 1   
    else:
        forward_type = 2
    departure_date = departure_date.strftime('%Y-%m-%d')
    back_date = back_date.strftime('%Y-%m-%d')
    output_data = []
    output_data.append(url)
    output_data.append(departure_date)
    output_data.append(back_date)
    output_data.append(forward_type)
    final_data.append(output_data)
print(final_data)
            
#!/usr/bin/env python
# coding: utf-8
# 航空公司字典
logo_dict = {"https://www.funtime.com.tw/airline/images/airline/D7.png":"亞洲航空",
             "https://www.funtime.com.tw/airline/images/airline/3K.png":"捷星航空",
             "https://www.funtime.com.tw/airline/images/airline/IT.png":"台灣虎航",
             "https://www.funtime.com.tw/airline/images/airline/MM.png":"樂桃航空",
             "https://www.funtime.com.tw/airline/images/airline/TR.png":"酷航航空",
             "https://www.funtime.com.tw/airline/images/airline/LJ.png":"真航空",
             "https://www.funtime.com.tw/airline/images/airline/VJ.png":"越捷航空",
             "https://www.funtime.com.tw/airline/images/airline/Z2.png":"亞洲航空",
             "https://www.funtime.com.tw/airline/images/airline/SL.png":"泰國獅子航空",
             "https://www.funtime.com.tw/airline/images/airline/XW.png":"酷鳥航空"}

# 爬蟲主函數
def data_work(list_x,date1, date2,logo):
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

# 繼承網址處理資料
data_list = final_data
# 
scrapy_data = [["飛機代號", "飛機機場", "出發日期", "回來日期", "機票價格", "航空公司", "去程時間", "回程時間",\
               "花費時間"]]
# chromedriver路徑設定
driver_location = "./chromedriver"
driver = webdriver.Chrome(driver_location)
count_1 = 0
e_count = 0

# 網址資料處理(產出網址、日期1、日期2、直飛與否
while len(data_list) != 0:
    http = data_list[0][0]
    date1 = data_list[0][1]
    date2 = data_list[0][2]
    non_stop = data_list[0][3]
    
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
        e_count += 1
        if e_count == 10:
            print("查無資料")
            break
    else:
        logo_1 = "div.fly_airline.clearfix > div > div.flight_row.GO.top > div > img"
        logo_2 = "div.fly_airline.clearfix > div > div.flight_row.BACK.top > div > img"
        logo_1 = driver.find_element_by_css_selector(logo_1).get_attribute("src")
        logo_2 = driver.find_element_by_css_selector(logo_2).get_attribute("src")
        logo = logo_dict[logo_1] + "-" + logo_dict[logo_2]
        ans_list = data_work(alldata_list,date1, date2,logo)
    del data_list[0]
    scrapy_data.append(ans_list)
print(scrapy_data)
driver.quit()

# coding=utf-8
info = scrapy_data

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

#打開瀏覽器,確保chromedriver在目錄下
browser=webdriver.Chrome('./chromedriver')
for info in info_ticket:
    url_tmpt = url
    departure = info[2]
    backdate = info[3]
    air_go = airline[info[5].split("-")[0]]
    air_back = airline[info[5].split("-")[1]]
    tmpt = url_tmpt.split("&")
    tmpt[1] = "departure=" + departure
    tmpt[2] = "backdate=" + backdate
    tmpt[13] = "air_go[]=" + air_go
    tmpt[14] = "air_back[]=" + air_back
    url_tmpt = "&".join(tmpt)
    
    #在瀏覽器打上網址連入
    browser.get(url_tmpt)
    wait = WebDriverWait(browser, 50)
    time.sleep(3)

    #分析網頁裡面的元素
    browser.find_element_by_class_name("fly_btn").click()
    time.sleep(3)

    #輸出連結讓使用者進入購物車頁面
    link = browser.find_element_by_css_selector("a[href][class][data-show_type]")
    print(link.get_attribute("href"))
    time.sleep(3)
    
browser.quit()
