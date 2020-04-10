#coding=utf-8  
import re   #Author:斯文
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains


#config
# x = '' 获得百度出发时间的xpath，不同时间，xpth路径不同，需手动获取



chrome_option = Options()

# chrome_option.add_argument('blink-settings=imagesEnabled=false') #不加载图片, 提升速度
chrome_option.add_argument('--headless') #浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
chrome_option.add_experimental_option('excludeSwitches', ['enable-logging'])#关闭控制台日志，看着太乱

driver=webdriver.Chrome(options=chrome_option)
driver.set_page_load_timeout(5000) 




def normal(tenement,sum):
    tongqin_time = time_text()      #获得居住人的未转化为分钟的通勤时间
    a = tongqin(tenement,tongqin_time)      #获得居住人转化为分钟的通勤时间
    sum.append(a)  #将本次获得的通勤时间加入到sum数组
    return sum
def time_text():  #解决3种情况，1：正常获得通勤时间  2：获取超长时间的通勤时间   3：未获得x到x的通勤时间，百度地图没算出来

    try:
# 13 7 20  
        # driver.find_element_by_xpath('//*[@id="bs_start_time"]').click()  #点击时间选项，因为不同的时间段，获得通勤时间结果不同
        # time.sleep(1)
        # driver.find_element_by_xpath('/html/body/div[{}]/ul/li[20]'.format(x)).click()      #7 8 9 10 11 12   #每次设置一次会增加1的xpath

        # driver.find_element_by_xpath('/html/body/div[{}]/ul/li[20]/ul/li[1]'.format(x)).click()  #设置为每天上午8点00分
        # time.sleep(3)
        tongqin_time = driver.find_element_by_xpath('//*[@id="scheme_0"]/div[1]/span[1]').text   #获得通勤时间
        print(tongqin_time)
        if len(tongqin_time) <= 1:
            time.sleep(3)
            tongqin_time = driver.find_element_by_xpath('//*[@id="scheme_0"]/div[1]/span[1]').text  #如果没获得，再次获得通勤时间
        print("【1-1】正常获得通勤时间")
    except:
        try:
            tongqin_time = driver.find_element_by_xpath('//*[@id="route_content_walk"]/div[1]/div[2]/div/div/div[1]/p[1]/span[1]').text
            if len(tongqin_time) <= 1:
                time.sleep(3)
                tongqin_time = driver.find_element_by_xpath('//*[@id="route_content_walk"]/div[1]/div[2]/div/div/div[1]/p[1]/span[1]').text
            print("【1-2】获得超长通勤时间")
        except:
            tongqin_time = driver.find_element_by_xpath('//*[@id="nav_container"]/div/p').text
            print("【1-3】未计算出x到x的通勤时间")
            # if "未能计算出" in v:
            #     age = 20 
            #     print("未计算出时间1，一般为地点过近，设置时间为20分钟")
            #     print("         前往{}需{}分钟".format(add,age))
            #     time.sleep(3)
            #     return age
    return tongqin_time

def tongqin(add,tongqin_time):

    guanjian = (u'小时')
    print("获取的通勤时间"+tongqin_time)
    if guanjian in tongqin_time:
        hou = int(tongqin_time[0])
        lp = tongqin_time[3:5]
        try:
            min = int(lp.replace("分",""))
        except:
            min = 0
            pass
        ti = hou * 60
        age = ti + min
    else:
        if "未能计算出" in tongqin_time:
            age = 20 
        #age = int(tongqin_time.replace("分钟",""))
        else:
            age = int(tongqin_time.replace("分钟",""))
        # print("未超过1小时")
    print("         前往{}需{}分钟".format(add,age))
    return age



def click_locxy(dr, x, y, left_click=True):
    '''
    dr:浏览器
    x:页面x坐标
    y:页面y坐标
    left_click:True为鼠标左键点击，否则为右键点击
    '''
    if left_click:
        ActionChains(dr).move_by_offset(x, y).click().perform()
    else:
        ActionChains(dr).move_by_offset(x, y).context_click().perform()
    ActionChains(dr).move_by_offset(-x, -y).perform()  # 将鼠标位置恢复到移动前

def start(terminus):
    print('——正在使用百度地图计算通勤时间,速度较慢，请耐心等待，预计时间以小时为单位'+'\n')
    print('[+ 正在后台打开浏览器，请稍等...')
        
    with open('house_info.txt','r',encoding='utf-8') as l:
        line = l.readlines()

        for fields in line:

            fields=fields.strip()
            fields=fields.strip("[]")
            fields=fields.split(",")

            price = fields[0]
            start_add = fields[1]
            big = fields[2]
            tar_url = fields[3]

            driver.get("https://map.baidu.com/@12959238.56,4825347.47,12z")      #浏览器打开百度地图，定位地点为北京，其他城市自行更换
            driver.find_element_by_xpath('//*[@id="sole-searchbox-content"]/div[2]').click()  #点击路线按钮
            driver.find_element_by_xpath('//*[@id="route-searchbox-content"]/div[2]/div/div[2]/div[1]/input').send_keys(start_add)   #输入起点小区名称
            print('开始计算{}小区的通勤距离'.format(start_add))
            time.sleep(1)
            click_locxy(driver,95,158,0)   #鼠标点击输入起点后百度的提示位置
            time.sleep(2)
            sum = []
            x = 7
            for tenement in terminus:
                driver.find_element_by_xpath('//*[@id="route-searchbox-content"]/div[2]/div/div[2]/div[2]/input').send_keys(tenement)  #输入目的地，从文件中读取的小区名字
                time.sleep(1)
                click_locxy(driver,95,158,0)   #鼠标点击输入终点后百度的提示位置
                driver.find_element_by_xpath('//*[@id="search-button"]').click()  #点击搜索按钮
                time.sleep(3)
                try:
                    normal(tenement,sum)  #获得通勤时间添加到数组sum
                    x+=1
                    time.sleep(2)
                    driver.find_element_by_xpath('//*[@id="route-searchbox-content"]/div[2]/div/div[2]/div[2]/div[2]').click()  #点击删除键

                except:#输入目的地后有4种情况
            #     第一种，起点不明确，需要点击`设为起点`按钮，获得结果
            #     第二种，起点不明确，需要点击`设为起点`按钮，终点不明确，需要点击`设为终点`按钮，获得结果
            #     第三种，终点不明确，需要点击`设为终点`按钮，获得结果
            #     第四种，起点在多个城市，需要点击`北京市`按钮，获得结果
                    try:
                        try:#先解决第三种终点不明确，需要点击`设为终点`按钮，获得结果
                            driver.find_element_by_xpath('//*[@id="RA_ResItem_1"]/table/tbody/tr[1]/td[2]/div').click()  #点击设为终点
                            time.sleep(2)
                            normal(tenement,sum)   #获得通勤时间添加到数组sum
                            x+=1
                            time.sleep(2)
                            driver.find_element_by_xpath('//*[@id="route-searchbox-content"]/div[2]/div/div[2]/div[2]/div[2]').click()  #点击删除键
                            print("【2-3】 点击了`设为终点`按钮")
                        except:#解决剩余两种情况
                            try:#解决第一种起点不明确，需要点击`设为起点`按钮，获得结果
                                driver.find_element_by_xpath('//*[@id="RA_ResItem_0"]/table/tbody/tr[1]/td[2]/div').click()  #点击设为起点
                                time.sleep(2)
                                normal(tenement,sum)   #获得通勤时间添加到数组sum
                                x+=1
                                time.sleep(2)
                                driver.find_element_by_xpath('//*[@id="route-searchbox-content"]/div[2]/div/div[2]/div[2]/div[2]').click()  #点击删除键
                                print("【2-1】 点击了`设为起点`按钮")
                            except:#解决第二种起点不明确，需要点击`设为起点`按钮，终点不明确，需要点击`设为终点`按钮，获得结果
                                driver.find_element_by_xpath('//*[@id="RA_ResItem_0"]/table/tbody/tr[1]/td[2]/div').click()  #点击设为起点
                                time.sleep(2)
                                driver.find_element_by_xpath('//*[@id="RA_ResItem_1"]/table/tbody/tr[1]/td[2]/div').click()  #点击设为终点
                                time.sleep(2)
                                normal(tenement,sum)   #获得通勤时间添加到数组sum
                                x+=1
                                time.sleep(2)
                                driver.find_element_by_xpath('//*[@id="route-searchbox-content"]/div[2]/div/div[2]/div[2]/div[2]').click()  #点击删除键
                                print("【2-1】 点击了`设为起点`和`设为终点`按钮")
                    except:#解决第四种情况，起点小区名称在各城市都有，需要点击估算最大的按钮
                        print('小区名称存在于多个城市，导致运行失败，请自行进入百度地图获得xpath路径粘贴到178行代码处')
                        driver.find_element_by_xpath('//*[@id="DIV_CityList0"]/div[2]/table/tbody/tr[1]/td[1]/a').click()
                        time.sleep(2)
                        driver.find_element_by_xpath('//*[@id="RA_ResItem_0"]/table/tbody/tr[1]').click()  #点击设为起点
                        time.sleep(2)
                        driver.find_element_by_xpath('//*[@id="RA_ResItem_0"]/table/tbody/tr[1]/td[2]/div').click()  #点击设为起点
                        time.sleep(2)
                        normal(tenement,sum)   #获得通勤时间添加到数组sum
                        x+=1
                        time.sleep(2)
                        driver.find_element_by_xpath('//*[@id="route-searchbox-content"]/div[2]/div/div[2]/div[2]/div[2]').click()  #点击删除键
                        print('【3-1】点击了北京市按钮和设为起点按钮')
                        

            time_sum = 0
            for s in sum:
                time_sum = time_sum + s   #获得居住人的通勤时间总和
    
            with open('house_result.txt','a',encoding='utf-8') as ai:
                ai.write('['+str(price)+','+str(start_add)+','+str(big)+','+str(tar_url)+','+str(time_sum)+']'+'\n')
                print("[+ {}小区到各上班地点通勤总时长为{}分钟,已写入result.txt\n".format(start_add,time_sum))
        print("所有小区通勤时间计算完毕！ very cool~")
