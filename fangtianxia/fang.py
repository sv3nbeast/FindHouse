#coding=utf-8
import requests   #Author:斯文
import re






# target_url = 'https://bj.lianjia.com/ditiezufang/li651/'+'pg{}'+url  #三室10号线整租业主直租，8000-12000


def rel_url(num,html):

    print('[+ 正在爬取第{}页，请稍等'.format(num))  
    rel = Url(html)
    r = requests.get(rel)
    url_html = r.text

    return url_html

def page_up(html):
    patt_name = re.compile(u'<span>(.*?)</span></a>')
    patt_price = re.compile(u'<span class="price">(.*?)</span>元/月</p>')
    patt_big = re.compile(u'厅<span class="splitline">\|</span>(.*?)�O<span')
    patt_url = re.compile(u'<a href="(.*?)" data_channel=')

    # with open ('html.txt','w',encoding='utf-8') as y:
    #     y.write(html)  
    nam = re.findall(patt_name,html)
    pri = re.findall(patt_price,html)
    big = re.findall(patt_big,html)
    url = re.findall(patt_url,html)

    ref = len(pri)
    try:
        for i in range(ref):

            with open('house_info.txt','a',encoding='utf-8') as h:
                h.write('['+pri[i]+','+nam[i]+','+big[i]+','+'https://zu.fang.com'+url[i]+']'+'\n')
    except:
        print("[+ 爬取完毕!")
        exit()

def Url(html):

    patt_url1 = re.compile(u'1</a><a href="(.*?)">下一页</a><a href=')
    patt_url2 = re.compile(u'2</a><a href="(.*?)">下一页</a><a href=')
    patt_url3 = re.compile(u'3</a><a href="(.*?)">下一页</a><a href=')
    patt_url4 = re.compile(u'4</a><a href="(.*?)">下一页</a><a href=')
    patt_url5 = re.compile(u'5</a><a href="(.*?)">下一页</a><a href=')

    rel1 = re.findall(patt_url1,html)
    rel2 = re.findall(patt_url2,html)
    rel3 = re.findall(patt_url3,html)
    rel4 = re.findall(patt_url4,html)
    rel5 = re.findall(patt_url5,html)
    r = ''
    if len(rel1) < 45:
        try:
            r = rel1[0]
        except:
            pass
    if len(rel2) < 45:
        try:
            r = rel2[0]
        except:
            pass
    if len(rel3) < 45:
        try:
            r = rel3[0]
        except:
            pass
    if len(rel4) < 45:
        try:
            r = rel4[0]
        except:
            pass
    if len(rel5) < 45:
        try:
            r = rel5[0]
        except:
            pass
    # with open('list.txt','w',encoding='utf-8') as o :
    #     o.write(url)
    if len(r) < 2:
        print('[- 存在验证码，请手动清除后再执行本程序！')
        exit()
    else:
        rel = r

    ra = requests.get('https://zu.fang.com'+rel,timeout=10)
    patt_red_url = re.compile(u'href="(.*?)">点击跳转</a>')
    if patt_red_url:
        rel = re.findall(patt_red_url,ra.text)
    else:
        print('[- 存在验证码，请手动清除后再执行本程序！')
        exit()
    return rel[0]
def one_Url(html):

    patt_red_url = re.compile(u'href="(.*?)">点击跳转</a>')
    rel1 = re.findall(patt_red_url,html)


    if '验证码' in html:
        print('[- 房天下存在验证码，请更换ip或者手动清除后再执行本程序！')
        exit()
    else:
        rel =rel1[0]

    return rel

header={
    'Connection': 'close',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
    'Sec-Fetch-Dest': 'document',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Referer': 'https://zu.fang.com/house1/',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    "Cookie": "global_cookie=8plf433oplmi2cz3auyl5t2dv18k8n82uoo; integratecover=1; sfut=19F2E65CB98DA032BB58C8BFF9DFDD9E7192D8AD16610F6E71758B04B9CC020C1BD813BDFF1203F9B8326B22404FA001FC2578BC346886C74CFB48369FD251BA35837065A8ED9D60A9E22D6EFA674391529C00D74A9BF0422B8112F31EFD2E35; searchConN=1_1586442218_153%5B%3A%7C%40%7C%3A%5D7b4bcae7a36650bd817665135be711f3; city=www; ASP.NET_SessionId=1rtttu2xpgi1islawjcxzzfe; g_sourcepage=zf_fy%5Editielb_pc; __utma=147393320.391305424.1586101838.1586440504.1586500071.9; __utmc=147393320; __utmz=147393320.1586500071.9.9.utmcsr=search.fang.com|utmccn=(referral)|utmcmd=referral|utmcct=/captcha-424548cfc82232c4d6/; __utmt_t0=1; __utmt_t1=1; __utmt_t2=1; new_loginid=111851390; login_username=fang7827033465; Captcha=6F4F58486436307A704E4C63316C53526C456D33356F396E7451364E314E55496C583974354B6F547654337A4B5468772B334367465459593074725A373278393366706F4E4B74397975633D; __utmb=147393320.36.10.1586500071; unique_cookie=U_h0mw6n5zhe7spff2b51mxebml1ak8tt4p9r*9"
    }
def start(target,state):
    if state == True:
        pass
    else:
        return False
    print('——房天下已启动'+'\n')
    r = requests.get(target,timeout=10)

    html = one_Url(r.text)

    t = requests.get(html,headers=header,timeout=10)



    patt_name = re.compile(u'<span>(.*?)</span></a>')
    patt_price = re.compile(u'<span class="price">(.*?)</span>元/月</p>')
    patt_big = re.compile(u'厅<span class="splitline">\|</span>(.*?)�O<span')
    patt_url = re.compile(u'<a href="(.*?)" data_channel=')
    patt_page = re.compile(u'<span class="txt">共(.*?)页</span>')

    nam = re.findall(patt_name,t.text)
    pri = re.findall(patt_price,t.text)
    big = re.findall(patt_big,t.text)
    url = re.findall(patt_url,t.text)
    page = re.findall(patt_page,t.text)


    try:
        e = int(page[0])
    except:
        e = 1

    print('[+ 搜索结果共{}条,{}页,正在爬取第1页，请稍等'.format(page[0],e))
    i = 0
    mnk = len(pri)

    for m in range(mnk):
        with open('house_info.txt','a',encoding='utf-8') as h:
            
            h.write('['+pri[i]+','+nam[i+2]+','+big[i]+','+'https://zu.fang.com'+url[i]+']'+'\n')
            # h.write('--price--'+pri[i]+'--address--'+nam[i]+'--big--'+big[i]+'--big'+'\n')

        i = i + 1
    x = 2

    while True:
        if x <= e:
            yuan = rel_url(x,t.text)

            page_up(yuan)
            
            x = x + 1
        else:
            print("[+ 爬取完毕!"+'\n')
            break