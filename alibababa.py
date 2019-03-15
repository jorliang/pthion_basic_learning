import requests
import re
import webbrowser
import time
import os
import xlwt
#定义加权值

#获取关键词并纠正关键词

#获取关键词下得10个厂商指标

#

#

def get_supp_dicts(res,name,href,r):
    table = re.findall(r'class="company-basicInfo"\>(.*?)\<\/table\>',res.text, re.S)
    title=[]
    title_txt=[]
    title = re.findall(r'class="field-title".*?\>(.*?)\<',str(table), re.S)
    title_txt = re.findall(r'class="content-value".*?\>(.*?)\<',str(table), re.S)

    title_dic = {'author': 'jorliang'}
    title_dic.clear()
    if len(title_txt)!=len(title):
        markit=re.findall(r'class="market-item"\>(.*?)\<',str(table), re.S)
        title_txt.insert(len(title_txt)-1,str(markit))
    if len(title_txt)==len(title):
        i = 0
        j = len(title)
        # fp.write('Company Name:'+str(name) +'\tHome Page:'+str(href)+ '\t\n')
        while i<j:
            title_dic[title[i]]=title_txt[i]
            i+=1
        c=0
        worksheet.write(r, c, name)
        worksheet.write(r, c + 1, href)
        c=0
        for dd in title_dic:
            if dd.strip()!='' and dd.strip()!='-':
                worksheet.write(r, c+2, title_dic[dd])
                c += 1
        #         fp.write(dd+'<<<----->>>'+title_dic[dd]+'\t\n')
        # fp.write('-------------------cut line--------------------\t\n')
        # fp.flush()
        #print(j)
        # print(title)
        # print(title_txt)
        #print(title_dic)
        title_dic.clear()
    else:
        print('Warning:主人发现不良数据~、\n')
        print(title,len(title))
        print(title_txt,len(title_txt))
        title_dic.clear()


def find_supp(res,r):
    href=re.findall(r'h2 class="title ellipsis".*?href="(.*?)"',res.text,re.S)
    name =re.findall(r'h2 class="title ellipsis".*?href=.*?\>(.*?)\&',res.text,re.S)
    #print(href,len(href))
    #webbrowser.open(res.url)
    i=0
    for ak in href:
        subreq=requests.get(ak)
        print('Notice:主人找到一家，正在爬取~')
        #webbrowser.open(subreq.url)
        c=0
        for koo in hea:
            worksheet.write(0, c, koo)
            c+=1
        get_supp_dicts(subreq,name[i],href[i],r)
        i+=1
        r+=1

        #ha.append())




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
hea=['Company Name','Home Page','Business Type','Location','Main Products','Ownership','Total Employees','Total Annual Revenue','Year Established','Certifications','Product Certifications','Patents','Main Markets','Trademarks']
#respone = requests.get('http://www.baidu.com')
print('''
        -----------------------------------------------------
        -----------------------------------------------------
        -----欢迎使用Souring Robot For Bethany In Aliba------
        ------------------Version 1.0------------------------
        -----------------------------------------------------
        -----------------------------------------------------
''')
#fp = open('tst.txt', 'w+', encoding='utf-8')
workbook = xlwt.Workbook(encoding='ascii')
worksheet = workbook.add_sheet('My Worksheet',cell_overwrite_ok=True)
r=0
while(kw != 'quit'):
    r = 0
    lit.clear()
    supp.clear()
    kw=input('Notice:Bethany请输入需要检索的产品，输入quit退出:\n>>>')
    find_web = 'https://www.alibaba.com/trade/search?fsb=y&IndexArea=company_en&CatId=&SearchText=%s&n=50&rd=1,2,3,4&f1=y&country=CN' % kw
    respone=requests.get(find_web)
    stp=check_kw(kw)
    if stp==-1:
        print('Error:主人输入不能包含汉字的！\n')
        continue
    elif stp == -2:
        print('Error:主人你输入的是什么鬼，根本查不到！')
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
                print('Notice:主人选择仍然搜索%s'%kw)
                print('Notice:那~现在开始抓数据了哦！\n')
                break
            else:
                print('Warning:主人别乱输入！')
                continue
    #elif stp==0:
        #print('Notice:供应商检索到%s个'%supp[0][0])
    print('Notice:主人抓数据统计分析部分还么完成，现在仅支持检索提取到Excel功能！')
    print('Notice:供应商检索到大约%s个,计划先抓个50个' % supp[0][0])
    # print('五秒后就要打开浏览器了！')
    # print('5')
    # time.sleep(1)
    # print('4')
    # time.sleep(1)
    # print('3')
    # time.sleep(1)
    # print('2')
    # time.sleep(1)
    # print('1')
    # time.sleep(1)
    # webbrowser.open(find_web)
    find_supp(respone,r)
    # fp.close()
    # os.startfile('tst.txt')
    workbook.save('Excel_Workbook.xls')
    os.startfile('Excel_Workbook.xls')
