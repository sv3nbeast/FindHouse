#coding=utf-8

import requests   #Author:斯文
import re



from lxml import etree


#config：配置项，需要手动填写

# wscckey = '8d10daf6a4f851fd_1586075472'          #我爱我家的机制，需要手动获取网页，找到源代码中的wscckey密钥  
#target_url = 'https://bj.5i5j.com/zufang/subway/sl10/r4u1w2'#四室       #我爱我家手动去网页配置好搜索配置，然后点击搜索后，将url输在此处，只需要输入最后\此符号的前面的链接即可




header={
    

    'Connection': 'close',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
    'Sec-Fetch-Dest': 'document',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9'

    }
# chrome_option = Options()

# chrome_option.add_argument('blink-settings=imagesEnabled=false') #不加载图片, 提升速度
# chrome_option.add_argument('--headless') #浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
# chrome_option.add_experimental_option('excludeSwitches', ['enable-logging'])#关闭控制台日志，看着太乱

# driver=webdriver.Chrome(options=chrome_option)
# driver.set_page_load_timeout(5000)



def page_up(html):
    patt_name = re.compile(u'.html">(.*?)</a>')
    patt_price = re.compile(u'<strong>(.*?)</strong>')
    patt_big = re.compile(u'·  (.*?)  平米')
    patt_url = re.compile(u'href="/zufang/(.*?).html" target="_blank">')
    # with open ('html.txt','w',encoding='utf-8') as y:
    #     y.write(html)  
    nam = re.findall(patt_name,html)
    pri = re.findall(patt_price,html)
    big = re.findall(patt_big,html)
    url = re.findall(patt_url,html)

    ref = len(pri)
    yi = 0
    for e in range(ref):
        with open('house_info.txt','a',encoding='utf-8') as h:
            h.write('['+pri[yi]+','+nam[yi]+','+big[yi]+','+'https://bj.5i5j.com/zufang/'+url[yi]+'.html'+']'+'\n')
def rel_url(num,target_url):
    print('[+ 正在爬取第{}页，请稍等'.format(num))

    r = requests.get('{}n{}/'.format(target_url,num))
    if len(r.text) > 200:
        url_html = r.text
    else:
        url = key(r.text,target_url)
        r1 = requests.get(url,headers=header)
        url_html = r1.text
    return url_html


def key(html,target_url):
    k = html.replace("<HTML><HEAD><script>window.location.href='{}?wscckey=".format(target_url),'')
    wscckey = k.replace("';</script></HEAD><BODY>",'')
    url1 = target_url+'?wscckey='+wscckey

    return url1
def start(target_url,state):
    if state == True:
        pass
    else:
        return False
    print('——我爱我家已启动'+'\n')
    if 'wscckey' in target_url:

        target_url = target_url[:-36]

    r = requests.get(target_url,headers=header,timeout=10)

    if 'location' in r.text:
        ur = key(r.text,target_url)

        w = requests.get(ur,headers=header,timeout=10)
        ht = w.text

    else:
        ht = r.text

    if 'clientIP' in ht:
        print('我爱我家未能成功获得信息，请更换ip'+'\n')
        return False
    # for i in range(0,100):
        
    #     html = r.text
    #     if len(html) < 200:
    #         break

    # k = html.replace("<HTML><HEAD><script>window.location.href='{}?wscckey=".format(target_url),'')
    # wscckey = k.replace("';</script></HEAD><BODY>",'')
    # url1 = target_url+'?wscckey='+wscckey
  
    # r = requests.get(url1,headers=header,timeout=10)


    tree = etree.HTML(ht)
    user = tree.xpath('/html/body/div[5]/div[1]/div[1]/div/span')
    # for i in user.text():
    page = user[0].text
    e = int(page) // 30 + 1
    print("[+ 搜索结果共{}条，{}页，获得第一页数据中".format(page,e))
    html = ht

    patt_name = re.compile(u'.html">(.*?)</a>')
    patt_price = re.compile(u'<p class="redC"><strong>(.*?)</strong>')
    patt_big = re.compile(u'·  (.*?)  平米')
    patt_url = re.compile(u'href="/zufang/(.*?).html" target="_blank">')


    nam = re.findall(patt_name,html)
    pri = re.findall(patt_price,html)
    big = re.findall(patt_big,html)
    url = re.findall(patt_url,html)
    i = 0
    mnk = len(pri)
    for m in range(mnk):
        with open('house_info.txt','a',encoding='utf-8') as h:
            h.write('['+pri[i]+','+nam[i]+','+big[i]+','+'https://bj.5i5j.com/zufang/'+url[i]+'.html'+']'+'\n')
            # h.write('--price--'+pri[i]+'--address--'+nam[i]+'--big--'+big[i]+'--big'+'\n')
        i = i + 1
    x = 2
    while True:
        if x <= e:
            yuan = rel_url(x,target_url)
            page_up(yuan)
            x = x + 1
        else:
            print("[+ 爬取完毕!"+'\n')
            break




    



