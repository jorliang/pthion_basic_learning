import re
import requests

respose=requests.get('http://www.xiaohuar.com/v/')
# print(respose.status_code)# 响应的状态码
# print(respose.content)  #返回字节信息
# print(respose.text)  #返回文本内容
pagenum=1
pagemax=re.findall(r'class="page_num".*?b\>(.*?)\<',respose.text,re.S)
print(pagemax)

#urls=re.findall(r'class="items".*?href="(.*?)"',respose.text,re.S)  #re.S 把文本信息转换成1行匹配
#print(len(urls))
#url=urls[5]
#result=requests.get(url)
#mp4_url=re.findall(r'id="media".*?src="(.*?)"',result.text,re.S)[0]
#print(mp4_url)
#video=requests.get(mp4_url)

#with open('D:\\a.mp4','wb') as f:
#    f.write(video.content)