#coding=utf-8
import requests   #Author:斯文
import re




#config：配置项，需要手动填写

target = 'https://bj.lianjia.com/ditiezufang/li651/rt200600000001l3brp12000erp16000/?showMore=1'      #手动配置好房屋要求后，取链接放入此处

# target_url = 'https://bj.lianjia.com/ditiezufang/li651/'+'pg{}'+url  #三室10号线整租业主直租，8000-12000




def rel_url(num,a_url):

    print('[+ 正在爬取第{}页，请稍等'.format(num))  
    rel = Url(a_url)
    r = requests.get('https://bj.lianjia.com/ditiezufang/li651/pg{}{}'.format(num,rel))

    url_html = r.text

    return url_html

def page_up(html):
    patt_name = re.compile(u'</a>-<a title="(.*?)" href="/zufang/')
    patt_price = re.compile(u'rice"><em>(.*?)</em>')
    patt_big = re.compile(u'''<i>/</i>
            (.*?)㎡
            <i>''')
    patt_url = re.compile(u'''<p class="content__list--item--title twoline">
            <a target="_blank" href="(.*?)">''')
    # with open ('html.txt','w',encoding='utf-8') as y:
    #     y.write(html)  
    nam = re.findall(patt_name,html)
    pri = re.findall(patt_price,html)
    big = re.findall(patt_big,html)
    url = re.findall(patt_url,html)

    ref = len(pri)
    try:
        for yi in range(ref):
            with open('house_info.txt','a',encoding='utf-8') as h:
                h.write('['+pri[yi]+','+nam[yi]+','+big[yi]+','+'https://bj.lianjia.com'+url[yi]+']'+'\n')
    except:
        print("[+ 爬取完毕!")
        exit()

def Url(url):

    patt_url = re.compile(u'https://bj.lianjia.com/ditiezufang/li651/(.*?)/')
    rel = re.findall(patt_url,url)

    return rel


header={
    'User-agent' : 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0;'

    }
def start(target,state):
    if state == True:
        pass
    else:
        return False
    print('——链家已启动'+'\n')
    r = requests.get(target,headers=header,timeout=10)


    patt_name = re.compile(u'</a>-<a title="(.*?)" href="/zufang/')
    patt_price = re.compile(u'rice"><em>(.*?)</em>')
    patt_big = re.compile(u'''
        (.*?)㎡
        ''')
    patt_url = re.compile(u'''class="content__list--item--aside" target="_blank"      href="(.*?)"''')
    patt_page = re.compile(u'<span class="content__title--hl">(.*?)</span>')

    nam = re.findall(patt_name,r.text)
    pri = re.findall(patt_price,r.text)
    big = re.findall(patt_big,r.text)
    url = re.findall(patt_url,r.text)
    page = re.findall(patt_page,r.text)


    e = int(page[0]) // 30 + 1
    print('[+ 搜索结果共{}条,{}页,正在爬取第1页，请稍等'.format(page[0],e))
    i = 0
    mnk = len(pri)

    for m in range(mnk):
        with open('house_info.txt','a',encoding='utf-8') as h:

            h.write('['+pri[i]+','+nam[i]+','+big[i]+','+'https://bj.lianjia.com'+url[i]+']'+'\n')
            # h.write('--price--'+pri[i]+'--address--'+nam[i]+'--big--'+big[i]+'--big'+'\n')
        i = i + 1
    x = 2
    while True:
        if x <= e:
            yuan = rel_url(x,target)
            page_up(yuan)
            x = x + 1
        else:
            print("[+ 爬取完毕!"+'\n')

            break