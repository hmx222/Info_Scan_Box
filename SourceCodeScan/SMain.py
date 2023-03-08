import SourceCodeScan.SMF
import requests
import function

requests.packages.urllib3.disable_warnings()


def SourceScan(url, headers):
    urls = []  # url
    annotation = []  # 注释

    get = SourceCodeScan.SMF.Ping(url)  # 拿到网页源代码
    email = function.SearchEmail(get)  # 对email的查找
    phone = function.SearchPhone(get)  # 对电话号码查找
    geturl = function.extract_URL(get)  # 对于网页源代码当中url的筛选(初次)
    for a_url in geturl:
        geturl = function.check_url(a_url, url)
    path = function.SearchPath(get)  # 对于path内容的搜索
    ann = function.Searchann(url)  # 对注释的搜索

    print("以下是来自", url, "的url：")
    for url in geturl:
        try:
            response = requests.get(url, headers, verify=False, timeout=8).status_code
        except:
            print(url, "NullStatus")
        else:
            print(url, "-" * 20, response)

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
            function.SearchBlackList(i)  # 判断是否为黑名单网站，是的话主动抛出异常
        except:
            i = "error"
        else:
            geturl1 = SourceCodeScan.SMF.Ping(i)  # 对指定网站发起请求，拿到网页源代码
            geturl2 = function.extract_URL(geturl1)  # 更加详细的url搜索
            urls.extend(geturl2)
            pa = function.SearchPath(geturl1)  # 对于路径的搜索
            path.extend(pa)
            ann = function.Searchann(geturl1)  # 对注释的搜索
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
