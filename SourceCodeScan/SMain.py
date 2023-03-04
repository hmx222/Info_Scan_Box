import re
import SourceCodeScan.SMF
import requests
import SourceCodeScan.MS

requests.packages.urllib3.disable_warnings()


def SourceScan(url):
    All_list = []
    urls = []  # url
    path = []  # 路径
    annotation = []  # 注释

    get = SourceCodeScan.SMF.Ping(url)  # 拿到网页源代码
    geturl = SourceCodeScan.MS.extract_URL(get)  # 对于网页源代码当中url的筛选(初次)
    path = SourceCodeScan.MS.SearchPath(get)
    for i in geturl:
        try:
            SourceCodeScan.MS.SearchBlackList(i)  # 判断是否为黑名单网站，是的话主动抛出异常
            geturl1 = SourceCodeScan.SMF.Ping(i)  # 对指定网站发起请求，拿到网页源代码
        except:
            i = "error"
        else:
            path1 = SourceCodeScan.MS.SearchPath(geturl1)  # 对于path内容的搜索
            All_list.extend(path1)
            geturl2 = SourceCodeScan.MS.extract_URL(geturl1)  # 更加详细的url搜索
            All_list.extend(geturl2)
            pa = SourceCodeScan.MS.SearchOtherPa(geturl1)  # 对于路径的搜索
            All_list.extend(pa)
            ann = SourceCodeScan.MS.Searchann(geturl1)
            All_list.extend(ann)

            rex = 'https?\://'
            rex2 = '(<!-- .*? -->)'
            for k in All_list:
                if re.match(rex, k):
                    urls.append(k)
                elif re.match(rex2, k):
                    annotation.append(k)
                else:
                    path.append(k)

            All_list = []  # 释放变量
            urls = []  # url
            path = []  # 路径
            annotation = []  # 注释

    return urls, path,annotation
