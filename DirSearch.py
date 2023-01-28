import requests


# TODO 高速读取

# 为DirSearch保存文件
def Read(filename):
    lines = []
    file = open(filename, 'r')
    while True:
        text = file.readline().strip()
        if not text:
            break
        lines.append(text)
    file.close()
    return lines


def Readfile(type):
    # 读取文件
    if type == "php":
        lines = Read("dict/php.txt")
        return lines
    elif type == "jsp":
        lines = Read("dict/jsp.txt")
        return lines
    elif type == "asp":
        lines = Read("dict/asp.txt")
        return lines
    elif type == "NONE":
        return 0


def DirSearch_main(domain,ua,getlist):
    li200 = []
    li300 = []
    li403 = []

    #请求

    for i in getlist:
        url = domain + i  # 拼接完整的url
        response = requests.get(url=url, headers=ua, verify=False, timeout=8).status_code  # 获取状态码
        if response == 200:
            print(url,"------",response)
        elif 300 <= response < 400:
            print(url,"------",response)
        elif response == 403:
            print(url, "------", response)



        # print("%s状态为%d" % (url, response))


        '''
                if 200 <= response < 300:
            li200.append(url)
        elif 300 <= response < 400:
            li300.append(url)
        elif response == 403:
            li403.append(url)
            
        
        '''



'''
        print("2xx的有：")
        for s200 in li200:
            print(s200)

        print("3xx的有：")
        for s300 in li300:
            print(s300)

        print("403的有：")
        for s403 in li403:
            print(403)


'''





