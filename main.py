import requests
import DirSearch
import SubDomain
import SourceCodeScan.SMain
import time

print('''
 _    _          _ 
| | _(_)_      _(_)
| |/ / \ \ /\ / / |
|   <| |\ V  V /| |
|_|\_\_| \_/\_/ |_|  v2.0

(1)目录扫描      （2）子域名探测    (3)网页源代码信息探测   
(4)nmap扫描      (5)cms识别      (6)漏洞利用      
(6)生成报告
''')

Ua = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv,2.0.1) Gecko/20100101 Firefox/4.0.1',
               'referer': 'https://www.baidu.com', "Connection": "close"}
option = input("请输入您要执行的操作：")
GetUrl = input("请输入url：")


if option == '1':
    # TODO 忽略大小写
    GetType = input("请输入类型（目前支持php，asp，jsp）：")
    stat200,stat300,stat403 = DirSearch.DirSearch(domain=GetUrl,ftype=GetType,ua=Ua)

    print("2xx的有：")
    for s200 in stat200:
        print(s200)

    print("3xx的有：")
    for s300 in stat300:
        print(s300)

    print("403的有：")
    for s403 in stat403:
        print(403)

elif option == '2':
    print("当前有大字典与小字典，您想要使用哪本字典。（1）小字典  （2）大字典")
    GetDicType = input("您是想使用哪本字典：")
    if GetDicType == '1':
        SubDomain.PingTest(url=GetUrl,header=Ua,option=1)
    elif GetDicType == '2':
        SubDomain.PingTest(url=GetUrl,header=Ua,option=2)

elif option == '3':
    print("即将开始网页源代码信息的提取")
    SourceCodeScan.SMain.SourceScan(GetUrl)

elif option == '4':
    print("您最好在kali linux下运行")
    time.sleep(5)




