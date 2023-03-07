import SourceCodeScan.SMF
import requests
import SourceCodeScan.MS

requests.packages.urllib3.disable_warnings()


def SourceScan(url):
    urls = []  # url
    annotation = []  # 注释

    get = SourceCodeScan.SMF.Ping(url)  # 拿到网页源代码
    email = SourceCodeScan.MS.SearchEmail(get) # 对email的查找
    phone = SourceCodeScan.MS.SearchPhone(get) # 对电话号码查找
    geturl = SourceCodeScan.MS.extract_URL(get)  # 对于网页源代码当中url的筛选(初次)
    for a_url in geturl:
        geturl = SourceCodeScan.MS.check_url(a_url, url)
    path = SourceCodeScan.MS.SearchPath(get)  # 对于path内容的搜索
    ann = SourceCodeScan.MS.Searchann(url)  # 对注释的搜索

    print("以下是来自", url, "的url：")
    for url in geturl:
        print(url)

    print("以下是来自", url, "的路径：")
    for pa1 in path:
        print(pa1)

    print("以下是来自", url, "的注释：")
    for ann1 in ann:
        print(ann1)

    print("以下是来自", url, "的email：")
    for em in email:
        print(em)

    print("以下是来自", url, "的phone：")
    for ph in phone:
        print(ph)

    # url is a list
    for i in geturl:
        try:
            SourceCodeScan.MS.SearchBlackList(i)  # 判断是否为黑名单网站，是的话主动抛出异常
        except:
            i = "error"
        else:
            geturl1 = SourceCodeScan.SMF.Ping(i)  # 对指定网站发起请求，拿到网页源代码
            geturl2 = SourceCodeScan.MS.extract_URL(geturl1)  # 更加详细的url搜索
            urls.extend(geturl2)
            pa = SourceCodeScan.MS.SearchPath(geturl1)  # 对于路径的搜索
            path.extend(pa)
            ann = SourceCodeScan.MS.Searchann(geturl1)  # 对注释的搜索
            annotation.extend(ann)

        if input("是否需要继续查找：") == 'y':
            geturl.extend(urls)
        print("以下是来自", i, "的url：")
        urls = list(set(urls))
        for url in urls:
            print(url)

        print("以下是来自", i, "的路径：")
        path = list(set(path))
        for pa1 in path:
            print(pa1)

        print("以下是来自", i, "的注释与汉字：")
        for ann1 in annotation:
            print(ann1)
