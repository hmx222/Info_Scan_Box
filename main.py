import SourceCodeScan.SMain,function,SubDomain,DirSearch
import os
import time
from concurrent.futures import ThreadPoolExecutor, Future

print('''
 _    _          _ 
| | _(_)_      _(_)
| |/ / \ \ /\ / / |
|   <| |\ V  V /| |
|_|\_\_| \_/\_/ |_|  v2.5

(1)目录扫描      （2）子域名探测    (3)网页源代码信息探测   
(4)crt搜索       (5)待添加      (6)待添加      
(6)待添加
''')

Ua = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv,2.0.1) Gecko/20100101 Firefox/4.0.1',
      'referer': 'https://www.baidu.com',
      "Connection": "close"}
option = input("请输入您要执行的操作：")
GetUrl = input("请输入url：")

if option == '1':
    GetType = input("请输入类型（目前支持php，asp，jsp，目录扫描)：")
    GetThreadMax = int(input("请输入最大线程阈值："))
    GetListPar = int(input("请输入列表分割后每个列表的长度："))
    lines = DirSearch.Readfile(GetType)

    # threads = []
    pool = ThreadPoolExecutor(GetThreadMax)
    temp = function.List_con(lines, GetListPar)

    for elist in temp:  # 开始遍历
        pool.submit(DirSearch.DirSearch_main, GetUrl, Ua, elist)
    pool.shutdown(True)  # 等待所有子线程结束后，主线程才会结束

    print("ending")

    # threads.append(threading.Thread(target=DirSearch.DirSearch_main, args=(GetUrl, Ua, elist))
    #               )
    # for thread in threads:
    # thread.start()


elif option == '2':

    GetDicType = input("当前有大字典与小字典，您想要使用哪本字典。（1）小字典  （2）大字典：")
    GetThreadMax = int(input("请输入最大线程阈值："))
    GetListPar = int(input("请输入列表分割后每个列表的长度："))

    pool = ThreadPoolExecutor(GetThreadMax)
    if GetDicType == '1':
        lines = SubDomain.Readfold(1)
        temp = function.List_con(lines, GetListPar)
        for elist in temp:
            pool.submit(SubDomain.PingTest, Ua, elist)

    elif GetDicType == '2':
        lines = SubDomain.Readfold(2)
        temp = function.List_con(lines, GetListPar)
        for elist in temp:
            pool.submit(SubDomain.PingTest, Ua, elist)

elif option == '3':
    print("即将开始网页源代码信息的提取")
    SourceCodeScan.SMain.SourceScan(GetUrl,headers=Ua)

elif option == '4':
    f = open("read.txt")
    result = function.Ana(f.read())
    f.close()
    for i in result:
        print(i)

elif option == '5':
    print("我们将开始运行CMSeek在你的kali linux当中")
    time.sleep(5)
    os.system("CMSeek")
