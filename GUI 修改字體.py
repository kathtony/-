#!/usr/bin/env python
# coding: utf-8

# In[44]:


def gui_departdict(entry_x):
    place_dict = {"上海":"港澳大陸,中國,上海","上海浦東":"港澳大陸,中國,上海浦東機場",
        "上海虹橋":"港澳大陸,中國,上海虹橋機場","北京":"港澳大陸,中國,北京",
        "香港":"港澳大陸,香港,香港","澳門":"港澳大陸,澳門,澳門",
        "東京":"東北亞,日本,東京（成田/羽田）機場","東京成田":"東北亞,日本,東京成田機場",
        "東京羽田":"東北亞,日本,東京羽田機場","大阪":"東北亞,日本,大阪",
        "沖繩":"東北亞,日本,琉球（沖繩）","福岡":"東北亞,日本,福岡",
        "名古屋":"東北亞,日本,名古屋","札幌":"東北亞,日本,札幌",
        "函館":"東北亞,日本,函館","仙台":"東北亞,日本,仙台",
        "岡山":"東北亞,日本,岡山","小松":"東北亞,日本,小松",
        "首爾":"東北亞,韓國,首爾","首爾仁川":"東北亞,韓國,首爾仁川機場",
        "首爾金浦":"東北亞,韓國,首爾金浦機場","釜山":"東北亞,韓國,釜山",
        "濟州":"東北亞,韓國,濟州","大邱":"東北亞,韓國,大邱",
        "務安":"東北亞,韓國,務安","清州":"東北亞,韓國,清州",
        "曼谷":"東南亞,泰國,曼谷","普吉島":"東南亞,泰國,普吉島",
        "清邁":"東南亞,泰國,清邁","合艾":"東南亞,泰國,合艾",
        "喀比":"東南亞,泰國,喀比","素叻府":"東南亞,泰國,素叻府",
        "新加坡":"東南亞,新加坡,新加坡",
        "吉隆坡":"東南亞,馬來西亞,吉隆坡","亞庇":"東南亞,馬來西亞,亞庇",
        "檳城":"東南亞,馬來西亞,檳城","蘭卡威":"東南亞,馬來西亞,蘭卡威",
        "古晉":"東南亞,馬來西亞,古晉","關丹":"東南亞,馬來西亞,關丹",
        "哥打巴魯":"東南亞,馬來西亞,哥打巴魯","納閩":"東南亞,馬來西亞,納閩",
        "詩巫":"東南亞,馬來西亞,詩巫","山打根":"東南亞,馬來西亞,山打根",
        "登嘉樓":"東南亞,馬來西亞,登嘉樓","斗湖":"東南亞,馬來西亞,斗湖",
        "雅加達":"東南亞,印尼,雅加達","巴里島":"東南亞,印尼,巴里島",
        "泗水":"東南亞,印尼,泗水","萬隆":"東南亞,印尼,萬隆",
        "日惹":"東南亞,印尼,日惹","龍目島":"東南亞,印尼,龍目島",
        "巨港":"東南亞,印尼,巨港","棉蘭":"東南亞,印尼,棉蘭",
        "坤緬":"東南亞,印尼,坤緬","梭羅":"東南亞,印尼,梭羅",
        "三寶壟":"東南亞,印尼,三寶壟","佩坎巴魯":"東南亞,印尼,佩坎巴魯",
        "馬尼拉":"東南亞,菲律賓,馬尼拉","宿霧":"東南亞,菲律賓,宿霧",
        "長灘島":"東南亞,菲律賓,長灘島","巴拉望":"東南亞,菲律賓,巴拉望",
        "薄荷島":"東南亞,菲律賓,薄荷島","克拉克":"東南亞,菲律賓,克拉克",
        "科隆":"東南亞,菲律賓,科隆","卡提克蘭":"東南亞,菲律賓,卡提克蘭",
        "達沃城":"東南亞,菲律賓,達沃城",
        "暹粒":"東南亞,柬埔寨,暹粒","金邊":"東南亞,柬埔寨,金邊",
        "西哈努克":"東南亞,柬埔寨,西哈努克",
        "胡志明市":"東南亞,越南,胡志明市","河內":"東南亞,越南,河內",
        "峴港":"東南亞,越南,峴港","芽莊":"東南亞,越南,芽莊",
        "芹苴":"東南亞,越南,芹苴（肯特）","金蘭市":"東南亞,越南,金蘭市",
        "斯里巴加灣":"東南亞,汶萊,斯里巴加灣","仰光":"東南亞,緬甸,仰光",
        "永珍":"東南亞,寮國,永珍","龍坡邦":"東南亞,寮國,龍坡邦",
        "柏林":"歐洲,德國,柏林",
        "雅典":"歐洲,希臘,雅典",
        "雪梨":"紐澳,澳洲,雪梨","墨爾本":"紐澳,澳洲,墨爾本",
        "黃金海岸":"紐澳,澳洲,黃金海岸","伯斯":"紐澳,澳洲,伯斯",
        "凱恩斯":"紐澳,澳洲,凱恩斯","達爾文":"紐澳,澳洲,達爾文",
        "奧克蘭":"紐澳,紐西蘭,奧克蘭",
        "關島":"太平洋島嶼,關島,關島",
        "塞班":"太平洋島嶼,塞班,塞班",
        "加爾各答":"南亞中東,印度,加爾各答","孟買":"南亞中東,印度,孟買",
        "科欽":"南亞中東,印度,科欽","齋普爾":"南亞中東,印度,齋普爾",
        "清奈":"南亞中東,印度,清奈","蒂魯吉拉伯利":"南亞中東,印度,蒂魯吉拉伯利",
        "勒克瑙":"南亞中東,印度,勒克瑙","阿姆利則":"南亞中東,印度,阿姆利則",
        "海得拉巴":"南亞中東,印度,海得拉巴","班加羅爾":"南亞中東,印度,班加羅爾",
        "馬列":"南亞中東,馬爾地夫,馬列",  
        "杜拜":"南亞中東,阿拉伯聯合大公國,杜拜",
        "吉達":"南亞中東,阿拉伯聯合大公國,吉達",
        "加德滿都":"南亞中東,尼泊爾,加德滿都",
        "德黑蘭":"南亞中東,伊朗,德黑蘭",
        "達卡":"南亞中東,孟加拉,達卡"}
    entry_y = place_dict[entry_x]
    return entry_y


# In[45]:


# 第一部分定義式
def http_build(line1):
    import datetime

    # 來回、單程、不同點進出
    way_type = {'來回':'ROU','單程':'ONE','不同點進出':'ROUD'}

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
    city['札幌'] = 'SPK'
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
        if way == '單程':
            back_date = departure_date
        else:
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
            if preferred_time[prefer_departime_time] == 'none' and preferred_time[prefer_back_time] == 'none':
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
            if preferred_time[prefer_departime_time] == 'none' and preferred_time[prefer_back_time] == 'none':
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
    return final_data, way, url, airline




# In[46]:

# 第二部分定義式
# 資料整理函式 用在67行
def goback_data(list_x,date1, date2,logo):
    plane = list_x[0] + "-" + list_x[1]
    go1, gototal, go2 = list_x[2].split(" ")
    go_time = go1 + "-" + go2
    go_airport = list_x[3].split(' ')
    go_airport = "-".join(go_airport)
    back1, backtotal, back2 = list_x[4].split(" ")
    back_time = back1 + "-" + back2
    back_airport = list_x[5].split(' ')
    back_airport = "-".join(back_airport)
    nothing, price = list_x[6].split("$")
    result = [plane, go_airport, back_airport, date1, date2, price, logo, go_time ,back_time, gototal, backtotal]
    return result

def go_data(list_x,date,logo):
    plane = list_x[0] 
    go1, gototal, go2 = list_x[1].split(" ")
    go_time = go1 + "-" + go2
    go_airport= list_x[2].split(' ')
    go_airport = "-".join(go_airport)
    nothing, price = list_x[3].split("$")
    result = [plane, go_airport, date, price, logo, go_time , gototal]
    return result
# 主要爬取函式
def main_scrapy(http_list, way):
    from selenium import webdriver
    import time
    # from selenium.webdriver.chrome.options import Options
    logo_dict = {"https://www.funtime.com.tw/airline/images/airline/D7.png":"亞洲航空",
                 "https://www.funtime.com.tw/airline/images/airline/GK.png":"捷星航空",
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
                 "https://www.funtime.com.tw/airline/images/airline/7C.png":"濟州航空", 
                 "https://www.funtime.com.tw/airline/images/airline/TW.png":"德威航空", 
                 "https://www.funtime.com.tw/airline/images/airline/ZE.png":"易斯達航空"}
    
    driver_location = "C:\\Users\\User\\Desktop\\chromedriver.exe"
    # 無痕模式
    #chromeoptions=Options()
    #chromeoptions.add_argument('--headless')
    #driver = webdriver.Chrome(driver_location,chrome_options=chromeoptions)
    driver = webdriver.Chrome(driver_location)
    air_set ={"TSA", "TPA", "RMQ", "KHH"}
# 網址資料處理(產出網址、日期1、日期2、直飛與否
    count1 = 0
    count2 = 0
    if way == "單程":
        scrapy_data = [["飛機代號", "去程飛機機場", "出發日期", "機票價格", "航空公司", "去程時間", "花費時間"]]
    
    else:
        scrapy_data = [["飛機代號", "去程飛機機場", "回程飛機機場", "出發日期", "回來日期", "機票價格", "航空公司", "去程時間", "回程時間",               "花費時間"]]
    while len(http_list) != 0:
        if count1 + count2 > 30:
            break
        http = http_list[0][0]
        if way == "單程":
            date = http_list[0][1]
            non_stop = http_list[0][2]
        else:
            date1 = http_list[0][1]
            date2 = http_list[0][2]
            non_stop = http_list[0][3]
    # 啟動虛擬瀏覽器  
        driver.get(http)
        driver.implicitly_wait(40)
        alldata_list = driver.find_element_by_id("result_area").text.split("\n")
        while alldata_list[0][0:4] == '正在搜尋' or alldata_list[0][0:3] in air_set:
            count1 += 1
            time.sleep(3)
            alldata_list = driver.find_element_by_id("result_area").text.split("\n")
            #print(alldata_list)
    # 萬一搜尋不到結果
        #print(alldata_list)
        if alldata_list[0][0:4] == 'Oops':
            count2 += 1
            ans_list ='Error'
            
        else:
            if way == "單程":  # 單程爬蟲
                logo = "div.fly_airline.clearfix > div > div.flight_row.GO.top > div > img"
                logo = driver.find_element_by_css_selector(logo).get_attribute("src")
                #print(logo)
                logo = logo_dict[logo]
                ans_list = go_data(alldata_list,date,logo)
            else:
                logo_1 = "div.fly_airline.clearfix > div > div.flight_row.GO.top > div > img"
                logo_2 = "div.fly_airline.clearfix > div > div.flight_row.BACK.top > div > img"
                logo_1 = driver.find_element_by_css_selector(logo_1).get_attribute("src")
                logo_2 = driver.find_element_by_css_selector(logo_2).get_attribute("src")
                #print(logo_1, logo_2)
                logo = logo_dict[logo_1] + "-" + logo_dict[logo_2]
                ans_list = goback_data(alldata_list,date1, date2,logo)
        del http_list[0]
        scrapy_data.append(ans_list)
        
    driver.quit()       
    return scrapy_data


# In[2]:


# coding=utf-8

def bunseki(info):
    import datetime

    info_ticket = list()
    for i in range(1, len(info)):
        if info[i] != "Error":
            if "," in info[i][5]:
                info[i][5] = int(info[i][5].replace(",", ""))  # 去除價格千分位分隔符號並轉成整數
            else:
                info[i][5] = int(info[i][5])  # 若價格無千分位分隔符號則直接轉成整數

            index_hour1 = info[i][9].find("時")
            index_hour2 = info[i][10].find("時")
            flight_time1 = datetime.timedelta(hours = int(info[i][9][:index_hour1 - 1]), minutes = int(info[i][9][index_hour1 + 1:len(info[i][9])-2]))  # 出發飛行時間
            flight_time2 = datetime.timedelta(hours = int(info[i][10][:index_hour2 - 1]), minutes = int(info[i][10][index_hour2 + 1:len(info[i][10])-2]))  # 回程飛行時間
            travel_time = datetime.datetime(2000, 1, 1, 0, 0, 0) + flight_time1 + flight_time2  # 以固定日期為基準加上總飛行時間以利後續排序
            info[i].append(travel_time)  # 將每張機票資訊加入總飛行時間
            info_ticket.append(info[i])  # 將去除標題列之資訊加入清單
            
    info_ticket.sort(key=lambda info_ticket: [info_ticket[5], info_ticket[11]])  # 將機票依價格、總飛行時間之層級排序

    return info_ticket

def kuroowaa(url, info_ticket, airline):
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import time
    if len(info_ticket) == 0:
        pass
    elif len(info_ticket) == 1:
        info_ticket = [info_ticket[0]]
    elif len(info_ticket) == 2:
        info_ticket = [info_ticket[0], info_ticket[1]]
    elif len(info_ticket) == 3:
        info_ticket = [info_ticket[0], info_ticket[1], info_ticket[2]]
    elif len(info_ticket) == 4:
        info_ticket = [info_ticket[0], info_ticket[1], info_ticket[2], info_ticket[3]]
    elif len(info_ticket) >= 5:
        info_ticket = [info_ticket[0], info_ticket[1], info_ticket[2], info_ticket[3], info_ticket[4]]
    else:
        pass

    url_lt = []
    #打開瀏覽器,確保chromedriver在目錄下
    driver_location = "C:\\Users\\User\\Desktop\\chromedriver.exe"
    browser=webdriver.Chrome(driver_location)
    #print(info_ticket)
    for info in info_ticket:
        url_tmpt = url
        departure = info[3]
        backdate = info[4]
        air_go = airline[info[6].split("-")[0]]
        air_back = airline[info[6].split("-")[1]]
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

        link = browser.find_element_by_css_selector("a[href][class][data-show_type]")
        url_lt.append(link.get_attribute("href"))
        time.sleep(3)
        
    browser.quit()
    return info_ticket, url_lt

import webbrowser
from functools import partial
def callback(url):
    webbrowser.open_new(url)

def result(info_ticket, url_lt):
    import tkinter as tk
    len_info_ticket = len(info_ticket)
    window = tk.Tk()

    window.title("result")
    window.geometry("1280x720")

    airplane = tk.Label(window, text = "航空公司", font=('Times new roman', 12))
    airplane.grid(row = 1, column = 1)

    price = tk.Label(window, text = "票券價格", font=('Times new roman', 12), width = 30, height = 2)
    price.grid(row = 1, column = 2)

    departure = tk.Label(window, text = "出國日期", font=('Times new roman', 12), width = 30, height = 2)
    departure.grid(row = 1, column = 3)

    backdate = tk.Label(window, text = "返國日期", font=('Times new roman', 12), width = 30, height = 2)
    backdate.grid(row = 1, column = 4)

    cart = tk.Label(window, text = "點我連結", font=('Times new roman', 12), width = 30, height = 2)
    cart.grid(row = 1, column = 5)

    if len_info_ticket == 0:
        airplane.grid_forget()
        price.grid_forget()
        departure.grid_forget()
        backdate.grid_forget()
        cart.grid_forget()
        text1 = "很抱歉，查無航班資訊，請重新輸入一次"       
        airplane = tk.Label(window, text = text1, font=('微軟正黑體', 24), foreground = 'Crimson')
        airplane.pack()
    
    elif len_info_ticket == 1:
        airplane = tk.Label(window, text = info_ticket[0][6], font=('Times new roman', 12))
        airplane.grid(row = 2, column = 1)

        price = tk.Label(window, text = "$" + str(format(info_ticket[0][5], ',')), font=('Times new roman', 12), width = 30, height = 2)
        price.grid(row = 2, column = 2)

        departure = tk.Label(window, text = info_ticket[0][3], font=('Times new roman', 12), width = 30, height = 2)
        departure.grid(row = 2, column = 3)

        backdate = tk.Label(window, text = info_ticket[0][4], font=('Times new roman', 12), width = 30, height = 2)
        backdate.grid(row = 2, column = 4)

        b = tk.Button(window, text='點我連結', font=('Arial', 12), width=30, height=2, command = partial(callback, url_lt[0]))
        b.grid(row = 2, column = 5)

    elif len_info_ticket == 2:
        airplane = tk.Label(window, text = info_ticket[0][6], font=('Times new roman', 12))
        airplane.grid(row = 2, column = 1)

        price = tk.Label(window, text = "$" + str(format(info_ticket[0][5], ',')), font=('Times new roman', 12), width = 30, height = 2)
        price.grid(row = 2, column = 2)

        departure = tk.Label(window, text = info_ticket[0][3], font=('Times new roman', 12), width = 30, height = 2)
        departure.grid(row = 2, column = 3)

        backdate = tk.Label(window, text = info_ticket[0][4], font=('Times new roman', 12), width = 30, height = 2)
        backdate.grid(row = 2, column = 4)

        b = tk.Button(window, text='點我連結', font=('Arial', 12), width=30, height=2, command = partial(callback, url_lt[0]))
        b.grid(row = 2, column = 5)


        airplane = tk.Label(window, text = info_ticket[1][6], font=('Times new roman', 12))
        airplane.grid(row = 3, column = 1)

        price = tk.Label(window, text = "$" + str(format(info_ticket[1][5], ',')), font=('Times new roman', 12), width = 30, height = 2)
        price.grid(row = 3, column = 2)

        departure = tk.Label(window, text = info_ticket[1][3], font=('Times new roman', 12), width = 30, height = 2)
        departure.grid(row = 3, column = 3)

        backdate = tk.Label(window, text = info_ticket[1][4], font=('Times new roman', 12), width = 30, height = 2)
        backdate.grid(row = 3, column = 4)

        b = tk.Button(window, text='點我連結', font=('Arial', 12), width=30, height=2, command = partial(callback, url_lt[1]))
        b.grid(row = 3, column = 5)

    elif len_info_ticket == 3:
        airplane = tk.Label(window, text = info_ticket[0][6], font=('Times new roman', 12))
        airplane.grid(row = 2, column = 1)

        price = tk.Label(window, text = "$" + str(format(info_ticket[0][5], ',')), font=('Times new roman', 12), width = 30, height = 2)
        price.grid(row = 2, column = 2)

        departure = tk.Label(window, text = info_ticket[0][3], font=('Times new roman', 12), width = 30, height = 2)
        departure.grid(row = 2, column = 3)

        backdate = tk.Label(window, text = info_ticket[0][4], font=('Times new roman', 12), width = 30, height = 2)
        backdate.grid(row = 2, column = 4)

        b = tk.Button(window, text='點我連結', font=('Arial', 12), width=30, height=2, command = partial(callback, url_lt[0]))
        b.grid(row = 2, column = 5)


        airplane = tk.Label(window, text = info_ticket[1][6], font=('Times new roman', 12))
        airplane.grid(row = 3, column = 1)

        price = tk.Label(window, text = "$" + str(format(info_ticket[1][5], ',')), font=('Times new roman', 12), width = 30, height = 2)
        price.grid(row = 3, column = 2)

        departure = tk.Label(window, text = info_ticket[1][3], font=('Times new roman', 12), width = 30, height = 2)
        departure.grid(row = 3, column = 3)

        backdate = tk.Label(window, text = info_ticket[1][4], font=('Times new roman', 12), width = 30, height = 2)
        backdate.grid(row = 3, column = 4)

        b = tk.Button(window, text='點我連結', font=('Arial', 12), width=30, height=2, command = partial(callback, url_lt[1]))
        b.grid(row = 3, column = 5)

        airplane = tk.Label(window, text = info_ticket[2][6], font=('Times new roman', 12))
        airplane.grid(row = 4, column = 1)

        price = tk.Label(window, text = "$" + str(format(info_ticket[2][5], ',')), font=('Times new roman', 12), width = 30, height = 2)
        price.grid(row = 4, column = 2)

        departure = tk.Label(window, text = info_ticket[2][3], font=('Times new roman', 12), width = 30, height = 2)
        departure.grid(row = 4, column = 3)

        backdate = tk.Label(window, text = info_ticket[2][4], font=('Times new roman', 12), width = 30, height = 2)
        backdate.grid(row = 4, column = 4)

        b = tk.Button(window, text='點我連結', font=('Arial', 12), width=30, height=2, command = partial(callback, url_lt[2]))
        b.grid(row = 4, column = 5)

    elif len_info_ticket == 4:
        airplane = tk.Label(window, text = info_ticket[0][6], font=('Times new roman', 12))
        airplane.grid(row = 2, column = 1)

        price = tk.Label(window, text = "$" + str(format(info_ticket[0][5], ',')), font=('Times new roman', 12), width = 30, height = 2)
        price.grid(row = 2, column = 2)

        departure = tk.Label(window, text = info_ticket[0][3], font=('Times new roman', 12), width = 30, height = 2)
        departure.grid(row = 2, column = 3)

        backdate = tk.Label(window, text = info_ticket[0][4], font=('Times new roman', 12), width = 30, height = 2)
        backdate.grid(row = 2, column = 4)

        b = tk.Button(window, text='點我連結', font=('Arial', 12), width=30, height=2, command = partial(callback, url_lt[0]))
        b.grid(row = 2, column = 5)


        airplane = tk.Label(window, text = info_ticket[1][6], font=('Times new roman', 12))
        airplane.grid(row = 3, column = 1)

        price = tk.Label(window, text = "$" + str(format(info_ticket[1][5], ',')), font=('Times new roman', 12), width = 30, height = 2)
        price.grid(row = 3, column = 2)

        departure = tk.Label(window, text = info_ticket[1][3], font=('Times new roman', 12), width = 30, height = 2)
        departure.grid(row = 3, column = 3)

        backdate = tk.Label(window, text = info_ticket[1][4], font=('Times new roman', 12), width = 30, height = 2)
        backdate.grid(row = 3, column = 4)

        b = tk.Button(window, text='點我連結', font=('Arial', 12), width=30, height=2, command = partial(callback, url_lt[1]))
        b.grid(row = 3, column = 5)

        airplane = tk.Label(window, text = info_ticket[2][6], font=('Times new roman', 12))
        airplane.grid(row = 4, column = 1)

        price = tk.Label(window, text = "$" + str(format(info_ticket[2][5], ',')), font=('Times new roman', 12), width = 30, height = 2)
        price.grid(row = 4, column = 2)

        departure = tk.Label(window, text = info_ticket[2][3], font=('Times new roman', 12), width = 30, height = 2)
        departure.grid(row = 4, column = 3)

        backdate = tk.Label(window, text = info_ticket[2][4], font=('Times new roman', 12), width = 30, height = 2)
        backdate.grid(row = 4, column = 4)

        b = tk.Button(window, text='點我連結', font=('Arial', 12), width=30, height=2, command = partial(callback, url_lt[2]))
        b.grid(row = 4, column = 5)

        airplane = tk.Label(window, text = info_ticket[3][6], font=('Times new roman', 12))
        airplane.grid(row = 5, column = 1)

        price = tk.Label(window, text = "$" + str(format(info_ticket[3][5], ',')), font=('Times new roman', 12), width = 30, height = 2)
        price.grid(row = 5, column = 2)

        departure = tk.Label(window, text = info_ticket[3][3], font=('Times new roman', 12), width = 30, height = 2)
        departure.grid(row = 5, column = 3)

        backdate = tk.Label(window, text = info_ticket[3][4], font=('Times new roman', 12), width = 30, height = 2)
        backdate.grid(row = 5, column = 4)

        b = tk.Button(window, text='點我連結', font=('Arial', 12), width=30, height=2, command = partial(callback, url_lt[2]))
        b.grid(row = 5, column = 5)

    elif len_info_ticket >= 5:
        airplane = tk.Label(window, text = info_ticket[0][6], font=('Times new roman', 12))
        airplane.grid(row = 2, column = 1)

        price = tk.Label(window, text = "$" + str(format(info_ticket[0][5], ',')), font=('Times new roman', 12), width = 30, height = 2)
        price.grid(row = 2, column = 2)

        departure = tk.Label(window, text = info_ticket[0][3], font=('Times new roman', 12), width = 30, height = 2)
        departure.grid(row = 2, column = 3)

        backdate = tk.Label(window, text = info_ticket[0][4], font=('Times new roman', 12), width = 30, height = 2)
        backdate.grid(row = 2, column = 4)

        b = tk.Button(window, text='點我連結', font=('Arial', 12), width=30, height=2, command = partial(callback, url_lt[0]))
        b.grid(row = 2, column = 5)


        airplane = tk.Label(window, text = info_ticket[1][6], font=('Times new roman', 12))
        airplane.grid(row = 3, column = 1)

        price = tk.Label(window, text = "$" + str(format(info_ticket[1][5], ',')), font=('Times new roman', 12), width = 30, height = 2)
        price.grid(row = 3, column = 2)

        departure = tk.Label(window, text = info_ticket[1][3], font=('Times new roman', 12), width = 30, height = 2)
        departure.grid(row = 3, column = 3)

        backdate = tk.Label(window, text = info_ticket[1][4], font=('Times new roman', 12), width = 30, height = 2)
        backdate.grid(row = 3, column = 4)

        b = tk.Button(window, text='點我連結', font=('Arial', 12), width=30, height=2, command = partial(callback, url_lt[1]))
        b.grid(row = 3, column = 5)

        airplane = tk.Label(window, text = info_ticket[2][6], font=('Times new roman', 12))
        airplane.grid(row = 4, column = 1)

        price = tk.Label(window, text = "$" + str(format(info_ticket[2][5], ',')), font=('Times new roman', 12), width = 30, height = 2)
        price.grid(row = 4, column = 2)

        departure = tk.Label(window, text = info_ticket[2][3], font=('Times new roman', 12), width = 30, height = 2)
        departure.grid(row = 4, column = 3)

        backdate = tk.Label(window, text = info_ticket[2][4], font=('Times new roman', 12), width = 30, height = 2)
        backdate.grid(row = 4, column = 4)

        b = tk.Button(window, text='點我連結', font=('Arial', 12), width=30, height=2, command = partial(callback, url_lt[2]))
        b.grid(row = 4, column = 5)

        airplane = tk.Label(window, text = info_ticket[3][6], font=('Times new roman', 12))
        airplane.grid(row = 5, column = 1)

        price = tk.Label(window, text = "$" + str(format(info_ticket[3][5], ',')), font=('Times new roman', 12), width = 30, height = 2)
        price.grid(row = 5, column = 2)

        departure = tk.Label(window, text = info_ticket[3][3], font=('Times new roman', 12), width = 30, height = 2)
        departure.grid(row = 5, column = 3)

        backdate = tk.Label(window, text = info_ticket[3][4], font=('Times new roman', 12), width = 30, height = 2)
        backdate.grid(row = 5, column = 4)

        b = tk.Button(window, text='點我連結', font=('Arial', 12), width=30, height=2, command = partial(callback, url_lt[2]))
        b.grid(row = 5, column = 5)

        airplane = tk.Label(window, text = info_ticket[4][6], font=('Times new roman', 12))
        airplane.grid(row = 6, column = 1)

        price = tk.Label(window, text = "$" + str(format(info_ticket[4][5], ',')), font=('Times new roman', 12), width = 30, height = 2)
        price.grid(row = 6, column = 2)

        departure = tk.Label(window, text = info_ticket[4][3], font=('Times new roman', 12), width = 30, height = 2)
        departure.grid(row = 6, column = 3)

        backdate = tk.Label(window, text = info_ticket[4][4], font=('Times new roman', 12), width = 30, height = 2)
        backdate.grid(row = 6, column = 4)

        b = tk.Button(window, text='點我連結', font=('Arial', 12), width=30, height=2, command = partial(callback, url_lt[2]))
        b.grid(row = 6, column = 5)

    else:
        pass

    window.mainloop()

# GUI部分
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
class Window(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.create_widgets()
        self.create_borders()
    # 基本元件建立
    def create_borders(self):
        # 邊界
        GC = tkFont.Font(size=12, weight=tkFont.BOLD, underline=1)
        GB = tkFont.Font(size=12)
        self.blb_1 = tk.Label(self, height=1, width=2, text="", font=GB)
        self.blb_2 = tk.Label(self, height=1, width=10, text="", font=GB)
        self.blb_1_1 = tk.Label(self, height=1, width=1, text="")
        self.blb_1_2 = tk.Label(self, height=1, width=1,text="", font=GB)
        self.blb_1_3 = tk.Label(self, height=1, width=5, text="", font=GB)

        self.blb_1.grid(row=1, column=1,rowspan=200)
        self.blb_1_1.grid(row=1, column=3,rowspan=200)
        self.blb_1_2.grid(row=1, column=5,rowspan=200)
        self.blb_1_3.grid(row=1, column=7,rowspan=200)

        self.blb_2.grid(row=1, column=2)
      
    def create_widgets(self):
        #Build Object/建立物件
        #label物件
        fonts = 10
        width_set = 50
        anchors ="w"
        anchors_en = "center"
        GD = tkFont.Font(size=12, weight=tkFont.BOLD)
    
        GC = tkFont.Font(size=12, weight=tkFont.BOLD, underline=1)
        GB = tkFont.Font(size=12)
        GB_1 = tkFont.Font(size=12)
        self.lb_1 = tk.Label(self, height=1, width=15, text="出發地", font = GD)
        self.lb_2 = tk.Label(self, height=1, width=15, text="目的地(例:大阪)", font = GD)
        self.lb_3 = tk.Label(self, height=1, width=15, text="時間(例:2020/6)", font = GD)
        self.lb_4 = tk.Label(self, height=1, width=15, text="天數(例:5)", font = GD)
        input_text1 = "預設條件：來回票、基本票(不含行李)、1位成人"
        input_text2 = "不限直飛與轉機、不限時段、不限價格"

        self.lb_s1 = tk.Label(self, width=45, text=input_text1, font = GD)
        self.lb_s2 = tk.Label(self, width=45, text=input_text2, font = GD)

        self.c1 = tk.Label(self, height=1, width=width_set, text="目的地", font = GC, anchor=anchors)
        self.NE = tk.Label(self, height=1, width=width_set, text="東北亞", font = GC, anchor=anchors)
        self.c7 = tk.Label(self, height=1, width=width_set, text="日本：東京、東京成田、東京羽田", font = GB_1, anchor=anchors)
        self.c8 = tk.Label(self, height=1, width=width_set, text="沖繩、福岡、名古屋、札幌、函館、仙台、岡山、小松", font = GB_1, anchor=anchors)
        self.c9 = tk.Label(self, height=1, width=width_set, text="韓國：首爾、首爾仁川、首爾金浦、釜山", font = GB_1, anchor=anchors)
        self.c10 = tk.Label(self, height=1, width=width_set, text="濟州、大邱、務安、清州", font = GB_1, anchor=anchors)
        self.GC = tk.Label(self, height=1, width= width_set, text='港澳大陸',font = GC, anchor=anchors)
        self.lb_China = tk.Label(self, height=1, width= width_set, text='中國：上海、上海浦東、上海虹橋、北京、香港、澳門', font = GB_1, anchor=anchors)
        self.lb_SE = tk.Label(self, height=1, width= width_set, text='東南亞', font = GC, anchor=anchors)
        self.lb_Thailand = tk.Label(self, height=1, width= width_set, text='泰國：曼谷、普吉島、清邁、合艾', font = GB_1, anchor=anchors)
        self.lb_singapore = tk.Label(self, height=1, width= width_set, text='新加坡', font = GB_1, anchor=anchors)
        self.lb_Malaysia = tk.Label(self, height=1, width= width_set, text='馬來西亞：吉隆坡、亞庇、檳城、蘭卡威', font = GB_1, anchor=anchors)
        self.lb_Indonesia = tk.Label(self, height=1, width= width_set, text='印尼：雅加達、巴里島、泗水、萬隆', font = GB_1, anchor=anchors)
        self.lb_Philippines = tk.Label(self, height=1, width= width_set, text='菲律賓：馬尼拉、宿霧、長灘島、巴拉望', font = GB_1, anchor=anchors)
        self.lb_Vietnam = tk.Label(self, height=1, width= width_set, text='越南：胡志明市、河內、峴港、芽莊', font = GB_1, anchor=anchors) 
        self.eu = tk.Label(self, height=1, width=width_set, text="歐美", font = GC, anchor=anchors)
        self.c11 = tk.Label(self, height=1, width=width_set, text="德國：柏林", font = GB_1, anchor=anchors)
        self.c12 = tk.Label(self, height=1, width=width_set, text="希臘：雅典", font = GB_1, anchor=anchors)
        self.c13 = tk.Label(self, height=1, width=width_set, text="澳洲：雪梨、墨爾本、黃金海岸、伯斯、凱恩斯、達爾文", font = GB_1, anchor=anchors)
        self.c14 = tk.Label(self, height=1, width=width_set, text="紐西蘭：奧克蘭", font = GB_1, anchor=anchors)
        self.c15 = tk.Label(self, height=1, width=width_set, text="關島", font = GB_1, anchor=anchors)
        self.SA = tk.Label(self, height=1, width=width_set, text="南亞",font = GC, anchor=anchors)
        self.c16 = tk.Label(self, height=1, width=width_set, text="印度：加爾各答、孟買、清奈、海得拉巴、班加羅爾", font = GB_1, anchor=anchors)
        self.c17 = tk.Label(self, height=1, width=width_set, text="馬爾地夫：馬列", font = GB_1, anchor=anchors)
        self.c18 = tk.Label(self, height=1, width=width_set, text="尼泊爾：加德滿都", font = GB_1, anchor=anchors)
        self.c19 = tk.Label(self, height=1, width=width_set, text="孟加拉：達卡", font = GB_1, anchor=anchors)
        self.ME = tk.Label(self, height=1, width=width_set, text="中東",font = GC, anchor=anchors)
        self.c20 = tk.Label(self, height=1, width=width_set, text="阿拉伯聯合大公國：杜拜", font = GB_1, anchor=anchors)
        self.c21 = tk.Label(self, height=1, width=width_set, text="沙烏地阿拉伯：吉達", font = GB_1, anchor=anchors)
        self.c22 = tk.Label(self, height=1, width=width_set, text="伊朗：德黑蘭", font = GB_1, anchor=anchors)


        #Assign Position/指定位置
        column_num = 8
        column_sapn = 30
        self.c1.grid(row=2, column=column_num, columnspan=column_sapn)
        self.NE.grid(row=3, column=column_num, columnspan=column_sapn)
        self.c7.grid(row=4, column=column_num, columnspan=column_sapn) 
        self.c8.grid(row=5, column=column_num, columnspan=column_sapn) 
        self.c9.grid(row=6, column=column_num, columnspan=column_sapn) 
        self.c10.grid(row=7, column=column_num, columnspan=column_sapn)
        self.GC.grid(row=8, column=column_num, columnspan=column_sapn)
        self.lb_China.grid(row=9, column=column_num, columnspan=column_sapn)
        self.lb_SE.grid(row=10, column=column_num, columnspan=column_sapn)        
        self.lb_Thailand.grid(row=11, column=column_num, columnspan=column_sapn)
        self.lb_singapore.grid(row=12, column=column_num, columnspan=column_sapn) 
        self.lb_Malaysia.grid(row=13, column=column_num, columnspan=column_sapn)
        self.lb_Indonesia.grid(row=14, column=column_num, columnspan=column_sapn) 
        self.lb_Philippines.grid(row=15, column=column_num, columnspan=column_sapn) 
        self.lb_Vietnam.grid(row=16, column=column_num, columnspan=column_sapn)
        self.eu.grid(row=17, column=column_num, columnspan=column_sapn)    
        self.c11.grid(row=18, column=column_num, columnspan=column_sapn) 
        self.c12.grid(row=19, column=column_num, columnspan=column_sapn)
        self.c13.grid(row=20, column=column_num, columnspan=column_sapn) 
        self.c14.grid(row=21, column=column_num, columnspan=column_sapn) 
        self.c15.grid(row=22, column=column_num, columnspan=column_sapn)
        self.SA.grid(row=22, column=column_num, columnspan=column_sapn)         
        self.c16.grid(row=23, column=column_num, columnspan=column_sapn) 
        self.c17.grid(row=24, column=column_num, columnspan=column_sapn) 
        self.c18.grid(row=25, column=column_num, columnspan=column_sapn) 
        self.c19.grid(row=26, column=column_num, columnspan=column_sapn)
        self.ME.grid(row=27, column=column_num, columnspan=column_sapn)
        self.c20.grid(row=28, column=column_num, columnspan=column_sapn)
        self.c21.grid(row=29, column=column_num, columnspan=column_sapn)
        self.c22.grid(row=30, column=column_num, columnspan=column_sapn)    
        #entry物件(空白輸入)
        
        self.en_0 = tk.Entry(self, width = 15, textvariable=tk.StringVar(value="來回"), font = GB)
        self.en_1 = ttk.Combobox(self, width = 15, values=["桃園", "松山", "台中", "高雄"], font = GB)
        self.en_2 = tk.Entry(self, width = 15, textvariable=tk.StringVar(value="大阪"), font = GB)
        self.en_3 = tk.Entry(self, width = 15, textvariable=tk.StringVar(value="2020/1"), font = GB)
        self.en_4 = tk.Entry(self, width = 5, textvariable=tk.StringVar(value="5"), font = GB)
        self.en_5 = tk.Entry(self, width = 15, textvariable=tk.StringVar(value="1/0/0"), font = GB)
        self.en_6 = tk.Entry(self, width = 15, textvariable=tk.StringVar(value="不限"), font = GB)
        self.en_7 = tk.Entry(self, width = 15, textvariable=tk.StringVar(value="不限"), font = GB)
        self.en_8 = tk.Entry(self, width = 15, textvariable=tk.StringVar(value="不限"), font = GB)
        self.en_9 = tk.Entry(self, width = 15, textvariable=tk.StringVar(value="0,0"), font = GB)
        #button物件
        self.var1 = tk.IntVar()
        self.btn = tk.Button(self, height=1, width=10, text="搜尋",command =self.main_program, font = GC)
        self.spchb = tk.Checkbutton(self, text="特殊條件",variable=self.var1, onvalue=1, offvalue=0,command =self.create_special, font="微軟正黑體 13")
        #物件指定位置(基本介面：出發/到達/日期/天數/搜尋)
        self.lb_1.grid(row=2, column=2)
        self.en_1.grid(row=3, column=2)
        self.lb_2.grid(row=2, column=4)
        self.en_2.grid(row=3, column=4)
        self.lb_3.grid(row=4, column=2)
        self.en_3.grid(row=5, column=2)
        self.lb_4.grid(row=4, column=4)
        self.en_4.grid(row=5, column=4)
        self.btn.grid(row=4, column=6)
        self.spchb.grid(row=6, column=2)
        self.lb_s1.grid(row=7, column=2,columnspan=5)
        self.lb_s2.grid(row=8, column=2,columnspan=5)
        


    # 製作特殊按鍵，打勾:出現，不打勾:取消
    def create_special(self):
        if self.var1.get() == 1:
            self.lb_s1.grid_forget()
            self.lb_s2.grid_forget()
            GB = tkFont.Font(size=12)
            GD = tkFont.Font(size=12, weight=tkFont.BOLD)
            GC = tkFont.Font(size=12, weight=tkFont.BOLD, underline=1)
            self.lb_0 = tk.Label(self, height=1, width=15, text="票種", font=GD)
            self.lb_5 = tk.Label(self, height=1, width=15, text="人數(大人/小孩/嬰兒)", font=GD)
            self.lb_6 = tk.Label(self, height=1, width=15, text="直飛與轉機", font=GD)
            self.lb_7 = tk.Label(self, height=1, width=15, text="去程時段", font=GD)
            self.lb_8 = tk.Label(self, height=1, width=15, text="回程時段", font=GD)
            self.lb_9 = tk.Label(self, height=1, width=15, text="票價(上限2萬,例:0,10000)", font=GD)
            self.en_0 = ttk.Combobox(self, width = 15, values=["來回", "單程", "不同點進出"], font=GD)
            self.en_6 = ttk.Combobox(self, width = 15, values=["不限", "直飛", "轉機"], font=GD)
            self.en_7 = ttk.Combobox(self, width = 15, values=["不限", "早", "午", "晚"], font=GD)
            self.en_8 = ttk.Combobox(self, width = 15, values=["不限", "早", "午", "晚"], font=GD)

            
            self.lb_0.grid(row=7, column=2)
            self.lb_5.grid(row=7, column=4)
            self.lb_6.grid(row=9, column=2)
            self.lb_7.grid(row=11, column=2)
            self.lb_8.grid(row=11, column=4)
            self.lb_9.grid(row=13, column=2, columnspan=2)

            self.en_0.grid(row=8, column=2)
            self.en_5.grid(row=8, column=4)
            self.en_6.grid(row=10, column=2)
            self.en_7.grid(row=12, column=2)
            self.en_8.grid(row=12, column=4)
            self.en_9.grid(row=14, column=2)
        else:
            self.lb_0.grid_forget() 
            self.lb_5.grid_forget()
            self.lb_6.grid_forget()
            self.lb_7.grid_forget()
            self.lb_8.grid_forget()
            self.lb_9.grid_forget()
            
            self.en_0.grid_forget()
            self.en_5.grid_forget()
            self.en_6.grid_forget()
            self.en_7.grid_forget()
            self.en_8.grid_forget()
            self.en_9.grid_forget()

    # 主程式        
    def main_program(self):
        import time
        time.sleep(3)
        way = self.en_0.get()
        bfrom = self.en_1.get()
        depart = gui_departdict(self.en_2.get())
        time = self.en_3.get().split("/")
        time = ",".join(time)
        day = self.en_4.get()
        people = self.en_5.get().split("/")
        people = ",".join(people)
        constant = "基本票"
        forward = self.en_6.get()
        constant_1 = "不限,不限"
        prefer_departime_time = self.en_7.get()
        prefer_back_time  = self.en_8.get()
        price_range = self.en_9.get()
        input_list = [way, bfrom, depart, time, day, people,constant,forward, constant_1, prefer_departime_time,
                      prefer_back_time, price_range]
        input_list = ",".join(input_list)
        http_list, way, url, airline = http_build(input_list)
        scrapy_data = main_scrapy(http_list, way)
        info_ticket, url_lt = kuroowaa(url, bunseki(scrapy_data), airline)
        result(info_ticket, url_lt)

myprogram = Window()

myprogram.master.geometry("1400x1200")  # 寬x高
myprogram.master.title("my window")  # 程式標題
myprogram.mainloop()