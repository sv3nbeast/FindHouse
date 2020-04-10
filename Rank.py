
#coding=utf-8


# config
num  = 10    #设置需要多少套房子，例如设置为10则先显示性价比前10的十套房子




def  pri_rank(arr):

    i = 0
    x = 0   #解决相同价格影响排序的参数
    contr = []
    for i in range(len(arr)):
        contrast_price_A = arr[i]['price']
        try:
            contrast_price_B = arr[i+1]['price']
        except:
            contrast_price_B = arr[i]['price']
            price_index = i + 1 - x
            arr[i]['price_rank'] = price_index
            contr.append(arr[i])
            break
        if contrast_price_A != contrast_price_B:
            price_index = i + 1 - x
            arr[i]['price_rank'] = price_index
            contr.append(arr[i])
        else:
            price_index = i + 1 - x
            x += 1
            arr[i]['price_rank'] = price_index
            contr.append(arr[i])
    return contr

def price_sort():
    o = []
    with open('house_result.txt','r',encoding='utf-8') as l:
        line = l.readlines()
        for fields in line:

            fields=fields.strip()
            # fields=fields.rstrip('\n')
            fields=fields.strip("[]")
            fields=fields.split(",")
            array = '{'+'"price":'+fields[0]+','+'"start_add":'+'"'+fields[1]+'"'+','+'"big":'+fields[2]+','+'"url":'+'"'+fields[3]+'"'+','+'"result":'+fields[4]+'}'
            o.append(eval(array))
    arr = sorted(o,key=lambda x:x["price"])
    return arr


def bigsmall_rank(arr):

    i = 0
    x = 0   #解决相同价格影响排序的参数
    contr = []
    for i in range(len(arr)):
        contrast_big_A = arr[i]['big']
        try:
            contrast_big_B = arr[i+1]['big']
        except:
            contrast_big_B = arr[i]['big']
            big_index = i + 1 - x
            arr[i]['big_rank'] = big_index
            contr.append(arr[i])
            break
        if contrast_big_A != contrast_big_B:
            big_index = i + 1 - x
            arr[i]['big_rank'] = big_index
            contr.append(arr[i])
        else:
            big_index = i + 1 - x
            x += 1
            arr[i]['big_rank'] = big_index
            contr.append(arr[i])
    return contr

def time_rank(arr):
    i = 0
    x = 0   #解决相同价格影响排序的参数
    contr = []
    for i in range(len(arr)):
        contrast_time_A = arr[i]['result']
        try:
            contrast_time_B = arr[i+1]['result']
        except:
            contrast_time_B = arr[i]['result']
            time_index = i + 1 - x
            arr[i]['result_rank'] = time_index
            contr.append(arr[i])
            break
        if contrast_time_A != contrast_time_B:
            time_index = i + 1 - x
            arr[i]['result_rank'] = time_index
            contr.append(arr[i])
        else:
            time_index = i + 1 - x
            x += 1
            arr[i]['result_rank'] = time_index
            contr.append(arr[i])

    return contr
    

def cost_sum(arr):
    contr = []
    for i in range(len(arr)):
        contrast_cost = arr[i]['price_rank'] + arr[i]['big_rank']+arr[i]['result_rank']
        arr[i]['xingjiabi'] = contrast_cost
        contr.append(arr[i])
    xingjiabi = sorted(contr,key=lambda x:x["xingjiabi"])
    return xingjiabi

def xingjiabi_rank(arr):
    i = 0
    x = 0   #解决相同价格影响排序的参数
    contr = []
    for i in range(len(arr)):
        contrast_time_A = arr[i]['xingjiabi']
        try:
            contrast_time_B = arr[i+1]['xingjiabi']
        except:
            contrast_time_B = arr[i]['xingjiabi']
            time_index = i + 1 - x
            arr[i]['xingjiabi_rank'] = time_index
            contr.append(arr[i])
            break
        if contrast_time_A != contrast_time_B:
            time_index = i + 1 - x
            arr[i]['xingjiabi_rank'] = time_index
            contr.append(arr[i])
        else:
            time_index = i + 1 - x
            x += 1
            arr[i]['xingjiabi_rank'] = time_index
            contr.append(arr[i])
    return contr

arr = price_sort() #获得价格排序后得数组+字典
p_rank = pri_rank(arr)   #获得价格排名的index下标加入字典内

big = sorted(p_rank,key=lambda x:x["big"],reverse=True)   #获得平方米排序后得数组+字典
big_rank = bigsmall_rank(big)   #获得平方米排名的index下标加入字典内

tongqin = sorted(big_rank,key=lambda x:x["result"])   #获得通勤时间排序后得数组+字典
tongqin_rank = time_rank(tongqin)   #获得平方米排名的index下标加入字典内

cost = cost_sum(tongqin_rank)   #获得价格，平方米，通勤时间3个结果之和，这个值放入新增加的xingjiabi键中后，获得数组+字典
cost_rank = xingjiabi_rank(cost)   #获得性价比排名的index下标加入字典内


print('''
[+ 最终结果，排名靠前则先输出，性价比按降序排列（如果有排名相同的，代表性价比相同，自己按照其他突出特点进行挑选即可）:

    price : 代表价格
    start_add : 代表小区名称
    big : 代表房屋面积
    url ：代表详情链接
    result : 代表居住人通勤时间的总和，以分钟为单位
    其余可以忽略
    
''')

with open('最终性价比排名.txt','a',encoding='utf-8') as v:
    for w in cost_rank:

        v.writelines(str(w)+'\n')
        j = w['xingjiabi_rank']
        if j <= 10:

            print('第{}名:{}'.format(str(j),w))
    # print(bigsmall_rank(p_rank))





    
        

    
