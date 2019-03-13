import requests
import re
import webbrowser
import time
#定义加权值

#获取关键词并纠正关键词

#获取关键词下得10个厂商指标

#

#

def check_kw(s):
    if re.findall(aa, kw).__len__() != 0:
        return -1#输入汉字
    else:
        respone = requests.get(find_web)
        #print(find_web)
        #print(respone.status_code)
        #if respone.status_code==500:
        #    return -2#搜索没找到关键词
        if respone.status_code==200:
            nn=respone.text
            if(nn.find('class="nomatch"')==-1):
                mm = re.findall(r'Did you mean.*?\{\{text\}\}\'\"\>(.*?)\<',respone.text,re.S)
                #print(lit_web)
                if len(mm)!=0:
                    lit.append(mm)
                    kk = re.findall(r'Did you mean.*?class="word".*?class="num".*?\((.*?) Supplier\(s\)', respone.text, re.S)
                    supp.append(kk)
                    return -3#拼写错误
                else:
                    kk = re.findall(r'class="ui-breadcrumb ml".*?\<span\>(.*?) Supplier', respone.text, re.S)
                    if len(kk)!=0:
                        if str(kk[0])=='0':
                            return -2  # 搜索没找到关键词
                        else:
                            kk = re.findall(r'class="ui-breadcrumb ml".*?\<span\>(.*?)\<.*?Supplier\(s\)', respone.text, re.S)
                            supp.append(kk)
                            return 0#正常
                    else:
                        print('Error:发生未知错误！')
            else:
                return -2#搜索没找到关键词

aa = '[\u4e00-\u9fa5]'
lit=['']
supp=['']
kw='666'
respone = requests.get('http://www.baidu.com')


while(kw != 'quit'):
    lit.clear()
    supp.clear()
    kw=input('Notice:请输入需要检索的产品:\n')
    find_web = 'https://www.alibaba.com/trade/search?fsb=y&IndexArea=company_en&CatId=&SearchText=%s' % kw
    stp=check_kw(kw)
    if stp==-1:
        print('Error:主人输入不能包含汉字的！\n')
        continue
    elif stp == -2:
        print('Error:主人你输入的是什么鬼，根本查不到！\n')
        continue
    elif stp == -3:
        print('Warning：主人检查到拼写错误了！你要找的商品是不是这个:%s'%str(lit[0][0]))
        ch=''
        while ch!='y' or ch != 'n':
            ch = input('Notice:请输入(y/n)进行是否切换到%s\n'%str(lit[0][0]))
            if ch=='y':
                kw=str(lit[0][0])
                find_web = 'https://www.alibaba.com/trade/search?fsb=y&IndexArea=company_en&CatId=&SearchText=%s' % kw
                respone=requests.get(find_web)
                print('Notice:产品搜索已切换到%s'%kw)
                break
            elif ch=='n':
                print('Notice:主人选择仍然搜索%s\n'%kw)
                print('Notice:那~现在开始抓数据了哦！\n')
                break
            else:
                print('Warning:主人别乱输入！')
                continue
    elif stp==0:
        print('Notice:供应商检索到%s个'%supp[0][0])
        print('Notice:主人抓数据统计部分还么完成，现在仅支持检索功能！')
    print('Notice:供应商检索到%s个' % supp[0][0])
    print('五秒后就要打开浏览器了！')
    print('5')
    time.sleep(1)
    print('4')
    time.sleep(1)
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)
    webbrowser.open(find_web)


