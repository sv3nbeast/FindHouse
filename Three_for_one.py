# coding=utf-8

from fangtianxia import fang
from lianjia import lian
from woaiwojia import woai
import baidu
banner='''
请确定Three_for_one文件已配置各租房平台URL后再开始执行
Usage:Python3 Three_for_one.py
'''


# 我爱我家
woaiwojia = 'https://bj.5i5j.com/zufang/subway/sl10/b12000e16000r4u1/?wscckey=7c6688760054afeb_1586500890'       #输入我爱我家网站配置好选项的链接，比如设置了   按地铁分配-10号线-3室-8000到12000-整租-及其他选项   最后复制当前URL填写到此处即可
w_config = True     #是否爬取

# 链家
lianjia = 'https://bj.lianjia.com/ditiezufang/li651/rt200600000001l3brp12000erp16000/'      #（同上）输入链家网站配置好选项的链接，比如设置了   按地铁分配-10号线-3室-8000到12000-整租-及其他选项   最后复制当前URL填写到此处即可
l_config = True     #是否爬取

# 房天下
fangtianxia = 'https://zu.fang.com/house1-j012/c212000-d216000-g24-n31-l310/'   #（同上）输入房天下网站配置好选项的链接，比如设置了   按地铁分配-10号线-3室-8000到12000-整租-及其他选项   最后复制当前URL填写到此处即可
f_config = False    #是否爬取


# 居住人工作地点，要求输入准确地点，请去百度地图定为目的地自行尝试

A = '快乐星球'          #有几个人填几个变量，多余变量就删除，也可增加
B = '海神岛'
C = '爱情公寓'
D = '灵剑派'
E = '六十中学'
F = '清华大学'

terminus = [A,B,C,D,E,F]        # 填入设置的居住人工作地点参数，有几个人设置填几个，多余的参数请自行删掉



print(banner)
fang.start(fangtianxia,f_config)
lian.start(lianjia,l_config)
woai.start(woaiwojia,w_config)

baidu.start(terminus)


