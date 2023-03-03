import os
import DirSearch
import SubDomain
import SourceCodeScan.SMain
import time
import public_function
from concurrent.futures import ThreadPoolExecutor, Future

print('''
 _    _          _ 
| | _(_)_      _(_)
| |/ / \ \ /\ / / |
|   <| |\ V  V /| |
|_|\_\_| \_/\_/ |_|  v2.2

(1)目录扫描      （2）子域名探测    (3)网页源代码信息探测   
(4)漏洞利用       (5)cms识别      (6)漏洞利用      
(6)免杀小工具
''')

Ua = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv,2.0.1) Gecko/20100101 Firefox/4.0.1',
      'referer': 'https://www.baidu.com', "Connection": "close"}
option = input("请输入您要执行的操作：")
GetUrl = input("请输入url：")

if option == '1':
    GetType = input("请输入类型（目前支持php，asp，jsp，目录扫描)：")
    GetThreadMax = int(input("请输入最大线程阈值："))
    GetListPar = int(input("请输入列表分割后每个列表的长度："))
    lines = DirSearch.Readfile(GetType)

    # threads = []
    pool = ThreadPoolExecutor(GetThreadMax)
    temp = public_function.List_con(lines, GetListPar)

    for elist in temp:  # 开始遍历
        pool.submit(DirSearch.DirSearch_main, GetUrl, Ua, elist)
    pool.shutdown(True)  # 等待所有子线程结束后，主线程才会结束

    print("ending")

    # threads.append(threading.Thread(target=DirSearch.DirSearch_main, args=(GetUrl, Ua, elist))
    #               )
    # for thread in threads:
    # thread.start()


elif option == '2':
    print("输入域名（去除www与http://）")
    GetDicType = input("当前有大字典与小字典，您想要使用哪本字典。（1）小字典  （2）大字典：")
    GetThreadMax = int(input("请输入最大线程阈值："))
    GetListPar = int(input("请输入列表分割后每个列表的长度："))

    pool = ThreadPoolExecutor(GetThreadMax)
    if GetDicType == '1':
        lines = SubDomain.Readfold(1)
        temp = public_function.List_con(lines, GetListPar)
        for elist in temp:
            pool.submit(SubDomain.PingTest, Ua, elist)

    elif GetDicType == '2':
        lines = SubDomain.Readfold(2)
        temp = public_function.List_con(lines, GetListPar)
        for elist in temp:
            pool.submit(SubDomain.PingTest, Ua, elist)

elif option == '3':
    print("即将开始网页源代码信息的提取")
    url,path=SourceCodeScan.SMain.SourceScan(GetUrl)
    print("url网站有：")
    for i in url:
        print(i)
    print("path：")
    for k in path:
        print(k)

elif option == '4':
    print("您最好在kali linux下运行")
    info = input("输入关键信息：")
    time.sleep(5)
    os.system("searchsploit "+ info)
elif option == '5':
    print("我们将开始运行CMSeek在你的kali linux当中")
    time.sleep(5)
    os.system("CMSeek")