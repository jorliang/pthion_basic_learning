import requests
import re

urls = 'https://freedom-gifts.en.alibaba.com/company_profile.html?spm=a2700.supplier-normal.35.3.929760d8OwY5Wl#top-nav-bar#'
response = requests.get(urls)

title=re.findall(r'class="field-title".*?\>(.*?)\<',response.text,re.S)
title_txt=re.findall(r'class="content-value".*?\>(.*?)\<',response.text,re.S)
title_dic={'author':'jorliang'}
i=0
j=len(title)
while i<j:
    title_dic[title[i]]=title_txt[i]
    i+=1
for dd in title_dic:
    print(dd,'-----',title_dic[dd])