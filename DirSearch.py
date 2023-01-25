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


def DirSearch(domain, ftype, ua):
    li200 = []
    li300 = []
    li403 = []

    # 读取文件
    if ftype == "php":
        lines = Read("dict/php.txt")
    elif ftype == "jsp":
        lines = Read("dict/jsp.txt")
    elif ftype == "asp":
        lines = Read("dict/asp.txt")
    elif ftype == "NONE":
        pass

    # 请求
    for i in lines:
        url = domain + i  # 拼接完整的url
        response = requests.get(url=url, headers=ua,verify=False,timeout=80).status_code  # 获取状态码
        print("%s状态为%d" % (url,response))
        if 200 <= response < 300:
            li200.append(url)
        elif 300 <= response < 400:
            li300.append(url)
        elif response == 403:
            li403.append(url)

    return li200, li300,li403
    #  print("状态码为200：")
    #  for a in li200:
    #      print(a)
#
#  print("状态码为300：")
#  for b in li300:
#      print(b)
#
#  print("状态码为400：")
#  for c in li400:
#      print(c)
#
#  print("状态码为500：")
#  for d in li500:
#      print(d)
