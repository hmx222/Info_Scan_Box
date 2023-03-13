import SourceCodeScan.SMain, function, SubDomain, DirSearch
import os, tkinter, time
from tkinter.ttk import Separator
from concurrent.futures import ThreadPoolExecutor, Future
from tkinter import ttk

window = tkinter.Tk()
window.title("hi,记得按时吃饭")
window.geometry('800x600+200+200')
variable = tkinter.StringVar()

style = ttk.Style(window)
style.configure('left-tab.TNotebook', tabposition='ws')

notebook = tkinter.ttk.Notebook(window,style='left-tab.TNotebook')

tkinter.Entry(window).place(x=200,y=10,width=550,height=30)
tkinter.Button(window,text="开始执行",padx=50,pady=30).place(x=200,y=500)

sourceView = tkinter.Frame(notebook)
subDomain = tkinter.Frame(notebook)
folderScan = tkinter.Frame(notebook)
crtSearch = tkinter.Frame(notebook)

notebook.add(sourceView, text='源代码信息爬取')
notebook.add(subDomain, text='子域名扫描')
notebook.add(folderScan,text='目录扫描')
notebook.add(crtSearch,text='crt探测')

notebook.pack(anchor='w',fill='x')

# tkinter.OptionMenu(window,variable,*[threads for threads in range(1,50)]).place(x=500,y=500)

Separator(window,orient="vertical").pack(padx=200,pady=5,fill='y',expand=True,anchor='w')

tkinter.Button(window,text="结束执行",padx=50,pady=30).place(x=500,y=500)

window.mainloop()

Ua = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv,2.0.1) Gecko/20100101 Firefox/4.0.1',
      'referer': 'https://www.baidu.com',
      "Connection": "close"}
option = input("please input your option:")
getUrl = function.Read('urls.txt')


if option == '1':
    getType = input("请输入类型（目前支持php，asp，jsp，目录扫描)：")
    getThreadMax = int(input("请输入最大线程阈值："))
    getListPar = int(input("请输入列表分割后每个列表的长度："))
    lines = DirSearch.Readfile(getType)

    # threads = []
    pool = ThreadPoolExecutor(getThreadMax)
    temp = function.list_con(lines, getListPar)

    for e_list in temp:  # 开始遍历
        pool.submit(DirSearch.DirSearch_main, getUrl, Ua, e_list)
    pool.shutdown(True)  # 等待所有子线程结束后，主线程才会结束

    print("ending")

    # threads.append(threading.Thread(target=DirSearch.DirSearch_main, args=(GetUrl, Ua, elist))
    #               )
    # for thread in threads:
    # thread.start()


elif option == '2':

    getDicType = input("We prepare two diction,which do you want to chose?（1）simple diction  （2）comprehensive diction：")
    getThreadMax = int(input("请输入最大线程阈值："))
    getListPar = int(input("请输入列表分割后每个列表的长度："))

    pool = ThreadPoolExecutor(getThreadMax)
    if getDicType == '1':
        lines = SubDomain.Readfold(1)
        temp = function.list_con(lines, getListPar)
        for e_list in temp:
            pool.submit(SubDomain.PingTest, Ua, e_list)

    elif getDicType == '2':
        lines = SubDomain.Readfold(2)
        temp = function.list_con(lines, getListPar)
        for e_list in temp:
            pool.submit(SubDomain.PingTest, Ua, e_list)

elif option == '3':
    print("即将开始网页源代码信息的提取")
    while True:
        SourceCodeScan.SMain.SourceScan(getUrl, headers=Ua)
        if input("Could you want to stop it?(y/n)") == 'y':
            break
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
